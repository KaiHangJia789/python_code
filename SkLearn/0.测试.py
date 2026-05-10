from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split,KFold,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,recall_score,f1_score ,precision_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA  # 用于降维画决策边界
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示
# 1.加载数据
digits_data = load_digits()
X, y = digits_data.data, digits_data.target

# 2.数据的预处理
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

# 3.特征标准化
tranfer = StandardScaler()
x_train_std = tranfer.fit_transform(x_train)
x_test_std = tranfer.transform(x_test)



# =================== 寻找最优K值 ==============================
def find_best_k(k_range=range(1,31),fold=5):
    k_scores = []
    kf = KFold(n_splits=fold,shuffle=True,random_state=22)
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, x_train_std, y_train, cv=kf)
        k_scores.append(scores.mean())
    best_score = max(k_scores)
    best_k = k_range[k_scores.index(best_score)]
    return best_k,best_score, k_scores

best_k, best_score, k_scores = find_best_k()
print("="*50)
print(f"K值: {best_k}\n最佳得分: {best_score:.4f}")
print("="*50)

# =================== 可视化 2：K值-准确率性能曲线 ===================
def plot_k_performance_curve(k_range=range(1,31)):
    plt.figure(figsize=(10, 5))
    plt.plot(k_range, k_scores, 'o-', color='blue', linewidth=2, markersize=8)
    plt.xlabel('K值')
    plt.ylabel('交叉验证准确率')
    plt.title('K值与模型性能关系曲线')
    plt.axvline(x=best_k, color='red', linestyle='--', label=f'最优K={best_k}')
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

# =================== 构建KNN模型 ======================
def sklearn_knn(k, distance_metric="euclidean", weights="uniform", average="micro"):
    knn = KNeighborsClassifier(n_neighbors=k, metric=distance_metric, weights=weights)
    knn.fit(x_train_std, y_train)
    y_predict = knn.predict(x_test_std)
    acc  = accuracy_score(y_test, y_predict)
    prec = precision_score(y_test, y_predict, average=average)
    rec  = recall_score(y_test, y_predict, average=average)
    f1   = f1_score(y_test, y_predict, average=average)
    return acc, prec, rec, f1, knn

# =================== 可视化 3：KNN决策边界 ===================
def plot_knn_decision_boundary():
    # 高维数据无法直接画边界，先用PCA降到2维
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(x_train_std)
    
    # 生成网格点
    h = 0.1
    x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
    y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # 测试不同K值的决策边界
    k_list = [1, 3, 5, 9, 15]
    plt.figure(figsize=(15, 10))
    
    for i, k in enumerate(k_list):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_pca, y_train)
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
        plt.subplot(2, 3, i+1)
        plt.contourf(xx, yy, Z, alpha=0.6, cmap=plt.cm.Spectral)
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.Spectral)
        plt.title(f'K={k} 决策边界')
        plt.axis('off')
    
    plt.suptitle('不同K值下KNN决策边界对比（PCA降维至2D）', fontsize=16)
    plt.tight_layout()
    plt.show()

# =================== 距离与权重测试 ===================
distance_list = ["euclidean", "manhattan", "chebyshev"]
weight_list = ["uniform", "distance"]
average_list = ["micro", "macro"]

print("="*50)
print(f"使用最优K进行测试: K  ={best_k}")
print("="*50)
for dist in distance_list:
    for weight in weight_list:
        for average in average_list:
            acc_sk, prec_sk, rec_sk, f1_sk, _ = sklearn_knn(
                k=best_k, distance_metric=dist, weights=weight, average=average
            )
            print(f"\n距离:{dist:10} | 权重:{weight:8} | 平均:{average:5}")
            print(f"准确率:{acc_sk:.4f}   | 精确率:{prec_sk:.4f} | 召回率:{rec_sk:.4f} | F1:{f1_sk:.4f}")   
print("="*50)

# =================== 执行所有可视化 ===================

plot_k_performance_curve()        # 2. K值性能曲线
plot_knn_decision_boundary()     # 3. KNN决策边界