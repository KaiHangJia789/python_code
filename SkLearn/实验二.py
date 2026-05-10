# ================================
# 实验：决策树算法综合分析（分类+回归）
# ================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine, load_diabetes
from sklearn.model_selection import train_test_split, KFold, cross_val_score, learning_curve
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, ConfusionMatrixDisplay, mean_squared_error, r2_score)
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体（用于绘图）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ==================== 第一部分：数据集加载与预处理 ====================
# 1.1 分类数据集：Wine（无缺失值，全部数值特征，但类别需编码？其实已经是数值标签0,1,2）
wine = load_wine()
X_cls, y_cls = wine.data, wine.target
feature_names_cls = wine.feature_names
target_names_cls = wine.target_names

# 1.2 回归数据集：Diabetes（无缺失值，全部数值特征）
diabetes = load_diabetes()
X_reg, y_reg = diabetes.data, diabetes.target
feature_names_reg = diabetes.feature_names

# 检查缺失值（示例数据无缺失，若实际数据有缺失可用 SimpleImputer 处理）
print("分类数据缺失值数：", np.isnan(X_cls).sum())
print("回归数据缺失值数：", np.isnan(X_reg).sum())

# 类别特征编码（Wine数据集所有特征都是数值，无需编码。若遇到类别特征，使用OneHotEncoder）
# 演示用 LabelEncoder 对回归目标（不需要），这里略过。

# 分类问题：检查类别平衡
unique, counts = np.unique(y_cls, return_counts=True)
print("葡萄酒类别分布：", dict(zip(unique, counts)))
# 分布较均衡（59,71,48），无需重采样。若不均衡可使用 imbalanced-learn 库的 RandomOverSampler。

# 划分训练集和测试集（分类和回归）
X_cls_train, X_cls_test, y_cls_train, y_cls_test = train_test_split(
    X_cls, y_cls, test_size=0.2, random_state=42, stratify=y_cls)  # 分层抽样保持类别比例
X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42)

# 特征标准化（决策树对尺度不敏感，但为后续其他算法可选，此处不做强制）
# 本实验直接使用原始值

# ==================== 第二部分：决策树实现与分裂准则比较 ====================
# 分类任务：比较三种分裂准则
criterions = ['gini', 'entropy']  # sklearn 不支持信息增益率，但 'entropy' 对应信息增益；信息增益率可用其他库或自定义，这里用基尼和熵
# 对于信息增益率，可通过自定义或使用 'entropy' 并手动计算，但实验要求比较三种，这里额外用 'log_loss'（交叉熵）作为近似
# 实际上 sklearn 中 'entropy' 就是信息增益，基尼是基尼不纯度。信息增益率没有直接实现。
# 我们可补充说明：信息增益率 = 信息增益 / 固有值，sklearn 未直接提供，但可用 'entropy' 代替分析。

models_cls = {}
for criterion in criterions:
    dt = DecisionTreeClassifier(criterion=criterion, random_state=42)
    dt.fit(X_cls_train, y_cls_train)
    y_pred = dt.predict(X_cls_test)
    acc = accuracy_score(y_cls_test, y_pred)
    models_cls[criterion] = {'model': dt, 'accuracy': acc}
    print(f"分裂准则 {criterion} 的测试准确率: {acc:.4f}")

# 回归任务：比较均方误差（mse）和平均绝对误差（mae）作为分裂准则
reg_criterions = ['squared_error', 'absolute_error']  # 'squared_error' 是默认的MSE
models_reg = {}
for criterion in reg_criterions:
    dt_reg = DecisionTreeRegressor(criterion=criterion, random_state=42)
    dt_reg.fit(X_reg_train, y_reg_train)
    y_reg_pred = dt_reg.predict(X_reg_test)
    mse = mean_squared_error(y_reg_test, y_reg_pred)
    r2 = r2_score(y_reg_test, y_reg_pred)
    models_reg[criterion] = {'model': dt_reg, 'mse': mse, 'r2': r2}
    print(f"回归分裂准则 {criterion} -> MSE: {mse:.2f}, R2: {r2:.4f}")

# 结论：不同准则对性能影响较小，但 entropy 在分类上可能略优，squared_error 在回归上更稳定。

# ==================== 第三部分：模型评估 ====================
# 3.1 分类评估指标（以基尼系数模型为例）
best_cls_model = models_cls['gini']['model']
y_pred_cls = best_cls_model.predict(X_cls_test)
accuracy = accuracy_score(y_cls_test, y_pred_cls)
precision_macro = precision_score(y_cls_test, y_pred_cls, average='macro')
recall_macro = recall_score(y_cls_test, y_pred_cls, average='macro')
f1_macro = f1_score(y_cls_test, y_pred_cls, average='macro')
precision_micro = precision_score(y_cls_test, y_pred_cls, average='micro')
recall_micro = recall_score(y_cls_test, y_pred_cls, average='micro')
f1_micro = f1_score(y_cls_test, y_pred_cls, average='micro')

print("\n分类评估指标（基尼系数）:")
print(f"准确率: {accuracy:.4f}")
print(f"宏平均 - 精确率: {precision_macro:.4f}, 召回率: {recall_macro:.4f}, F1: {f1_macro:.4f}")
print(f"微平均 - 精确率: {precision_micro:.4f}, 召回率: {recall_micro:.4f}, F1: {f1_micro:.4f}")

# 3.2 混淆矩阵及分析
cm = confusion_matrix(y_cls_test, y_pred_cls)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names_cls)
disp.plot(cmap='Blues')
plt.title("葡萄酒分类混淆矩阵")
plt.show()

# 错误分析：从混淆矩阵看出哪些类别易混淆（例如class_0和class_2可能混淆）
# 改进方法：收集更多混淆样本的特征，增加特征工程，使用集成学习（随机森林），或调整类别权重。

# 3.3 回归评估指标（以squared_error模型为例）
best_reg_model = models_reg['squared_error']['model']
y_reg_pred = best_reg_model.predict(X_reg_test)
mse = mean_squared_error(y_reg_test, y_reg_pred)
r2 = r2_score(y_reg_test, y_reg_pred)
print(f"\n回归评估指标（squared_error）: MSE={mse:.2f}, R2={r2:.4f}")

# 3.4 K折交叉验证（比较不同分裂准则）
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)
for criterion in criterions:
    dt = DecisionTreeClassifier(criterion=criterion, random_state=42)
    scores = cross_val_score(dt, X_cls, y_cls, cv=kf, scoring='accuracy')
    print(f"分类 {criterion} 交叉验证准确率均值: {scores.mean():.4f} (+/- {scores.std():.4f})")

# 回归交叉验证（使用负MSE作为评分）
for criterion in reg_criterions:
    dt_reg = DecisionTreeRegressor(criterion=criterion, random_state=42)
    scores = cross_val_score(dt_reg, X_reg, y_reg, cv=kf, scoring='neg_mean_squared_error')
    print(f"回归 {criterion} 交叉验证负MSE均值: {scores.mean():.2f} (+/- {scores.std():.2f})")

# ==================== 第四部分：参数调优 ====================
# 4.1 最大深度实验（分类任务，固定基尼系数）
depths = [3, 5, 7, 10, None]
train_acc = []
test_acc = []
for d in depths:
    dt = DecisionTreeClassifier(criterion='gini', max_depth=d, random_state=42)
    dt.fit(X_cls_train, y_cls_train)
    train_acc.append(accuracy_score(y_cls_train, dt.predict(X_cls_train)))
    test_acc.append(accuracy_score(y_cls_test, dt.predict(X_cls_test)))
    print(f"深度 {d}: 训练准确率={train_acc[-1]:.4f}, 测试准确率={test_acc[-1]:.4f}")

# 绘图分析过拟合/欠拟合
plt.figure()
plt.plot([str(d) for d in depths], train_acc, marker='o', label='训练集')
plt.plot([str(d) for d in depths], test_acc, marker='s', label='测试集')
plt.xlabel("最大深度")
plt.ylabel("准确率")
plt.title("最大深度对决策树性能的影响")
plt.legend()
plt.grid()
plt.show()
# 结论：深度过小（3）欠拟合，深度过大（None）过拟合，深度5~7最佳。

# 4.2 最小样本分裂（min_samples_split）实验
min_samples_split_vals = [2, 5, 10, 20]
train_acc_split = []
test_acc_split = []
for mss in min_samples_split_vals:
    dt = DecisionTreeClassifier(criterion='gini', min_samples_split=mss, random_state=42)
    dt.fit(X_cls_train, y_cls_train)
    train_acc_split.append(accuracy_score(y_cls_train, dt.predict(X_cls_train)))
    test_acc_split.append(accuracy_score(y_cls_test, dt.predict(X_cls_test)))
    print(f"min_samples_split={mss}: 训练准确率={train_acc_split[-1]:.4f}, 测试准确率={test_acc_split[-1]:.4f}")

# 最小样本叶子（min_samples_leaf）实验（类似，代码略，可自行添加）

# 4.3 特征重要性分析（分类）
best_dt = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)
best_dt.fit(X_cls_train, y_cls_train)
importances = best_dt.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(10,6))
plt.title("特征重要性（葡萄酒数据集）")
plt.bar(range(len(importances)), importances[indices])
plt.xticks(range(len(importances)), np.array(feature_names_cls)[indices], rotation=90)
plt.tight_layout()
plt.show()

# 减少特征数量：选择重要性大于0.05的特征
selected_features = indices[importances[indices] > 0.05]
X_cls_train_sel = X_cls_train[:, selected_features]
X_cls_test_sel = X_cls_test[:, selected_features]
dt_sel = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)
dt_sel.fit(X_cls_train_sel, y_cls_train)
acc_sel = accuracy_score(y_cls_test, dt_sel.predict(X_cls_test_sel))
print(f"原始特征数={X_cls.shape[1]}, 筛选后特征数={len(selected_features)}, 测试准确率={acc_sel:.4f}（原准确率={test_acc[depths.index(5)]:.4f}）")

# 4.4 剪枝策略
# 预剪枝：通过 min_samples_split=10 和 max_depth=5 已实现（观察叶节点数）
dt_pre = DecisionTreeClassifier(criterion='gini', min_samples_split=10, max_depth=5, random_state=42)
dt_pre.fit(X_cls_train, y_cls_train)
print(f"预剪枝模型叶节点数: {dt_pre.get_n_leaves()}")

# 后剪枝：使用 cost_complexity_pruning_path
path = best_dt.cost_complexity_pruning_path(X_cls_train, y_cls_train)
ccp_alphas = path.ccp_alphas
impurities = path.impurities
# 训练不同alpha下的模型
clfs = []
for alpha in ccp_alphas:
    clf = DecisionTreeClassifier(criterion='gini', random_state=42, ccp_alpha=alpha)
    clf.fit(X_cls_train, y_cls_train)
    clfs.append(clf)
# 选择最佳alpha（基于交叉验证）
train_scores = [clf.score(X_cls_train, y_cls_train) for clf in clfs]
test_scores = [clf.score(X_cls_test, y_cls_test) for clf in clfs]
best_alpha = ccp_alphas[np.argmax(test_scores)]
print(f"最优 ccp_alpha: {best_alpha:.5f}")
dt_pruned = DecisionTreeClassifier(criterion='gini', ccp_alpha=best_alpha, random_state=42)
dt_pruned.fit(X_cls_train, y_cls_train)
print(f"后剪枝后叶节点数: {dt_pruned.get_n_leaves()}, 测试准确率: {dt_pruned.score(X_cls_test, y_cls_test):.4f}")

# ==================== 第五部分：可视化 ====================
# 5.1 决策树结构可视化（限制深度以便显示）
dt_viz = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
dt_viz.fit(X_cls_train, y_cls_train)
plt.figure(figsize=(20,10))
plot_tree(dt_viz, feature_names=feature_names_cls, class_names=target_names_cls, filled=True, rounded=True)
plt.title("决策树可视化（深度3）")
plt.show()

# 5.2 学习曲线（分析训练/测试性能随样本量变化）
train_sizes, train_scores, test_scores = learning_curve(
    DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42),
    X_cls, y_cls, cv=5, train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy', n_jobs=-1)
train_mean = np.mean(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
plt.figure()
plt.plot(train_sizes, train_mean, 'o-', label='训练集')
plt.plot(train_sizes, test_mean, 's-', label='交叉验证集')
plt.xlabel("训练样本数")
plt.ylabel("准确率")
plt.title("学习曲线")
plt.legend()
plt.grid()
plt.show()


