from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split,KFold,cross_val_score    #数据集切分
from sklearn.preprocessing import StandardScaler        #数据预处理标准化
from sklearn.neighbors import KNeighborsClassifier #KNN算法 分类
from sklearn.metrics import accuracy_score,recall_score,f1_score ,precision_score#模型评估
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示
# 1.加载数据
def load_and_preprocess_data(load=load_digits()):
    digits_data = load
    # print(f"数据集的基本阐述:\n{digits_data.DESCR}")
    # print(f"特征名称:\n{digits_data.feature_names}")
    # print(f"数据集的标签:\n{digits_data.target}")
    print(f"数据集总类:{len(digits_data.target_names)}")
    print(f"所有类别:{digits_data.target_names}")
    print('*'*50)
    print(f"【数据集总样本数】: {digits_data.data.shape[0]} 个")  # 总数据量
    print(f"【每个样本的特征数】: {digits_data.data.shape[1]} 个") # 特征
    print("="*50)
    #2.数据的预处理
    x_train, x_test, y_train, y_test = train_test_split(digits_data.data, digits_data.target, test_size=0.2, random_state=22)

    #3.特征标准化
    tranfer = StandardScaler()
    x_train_std = tranfer.fit_transform(x_train)
    x_test_std = tranfer.transform(x_test)
    return x_train_std, x_test_std, y_train, y_test

#===================寻找最优K值==============================
def find_best_k(x_train_std=None, y_train=None, k_range=range(1,31),fold=5):
    """
    自动遍历K值,用k折交叉验证找最优K值
    k_range: 遍历的K值范围
    fold: 交叉验证的折数
    """
    k_scores = []#存储结果
    kf = KFold(n_splits=fold,shuffle=True,random_state=22)#创建K折交叉验证对象
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)#创建KNN分类器
        scores = cross_val_score(knn, x_train_std, y_train, cv=kf)#用K折交叉验证评估模型
        k_scores.append(scores.mean())#记录结果
    #找到最优K值和最优分数
    best_score = max(k_scores)#最优分数
    best_k = k_range[k_scores.index(best_score)]#最优K值
    return best_k,best_score,k_scores

#=================== 可视化1：类别分布统计图 ==================
def plot_class_distribution(y=None):
    plt.figure(figsize=(8, 4))
    classes, counts = np.unique(y, return_counts=True)
    plt.bar(classes, counts, color='skyblue', edgecolor='black')
    plt.xlabel('数字类别')
    plt.ylabel('样本数量')
    plt.title('手写数字数据集类别分布')
    plt.xticks(classes)
    plt.grid(axis='y', alpha=0.3)
    plt.show()

#=================== 可视化2：部分特征分布直方图 ==================
def plot_all_features_distribution(x_train_std=None):
    """
    绘制 8x8 网格，展示所有 64 个特征的分布直方图
    """
    plt.figure(figsize=(16, 16))
    for i in range(64):
        plt.subplot(8, 8, i + 1)
        plt.hist(x_train_std[:, i], bins=15, color='steelblue', alpha=0.7)
        plt.title(f"特征 {i+1}", fontsize=9)
        plt.xticks([])  # 隐藏x轴刻度，更整洁
        plt.yticks([])
    plt.suptitle("手写数字数据集 64 个特征（像素）分布直方图", fontsize=20, y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    plt.show()


# =================== 可视化 2：K值-准确率性能曲线 ===================
def plot_k_performance_curve(k_range=range(1,31), k_score=None, best_k=None):
    
    plt.figure(figsize=(10, 5))
    plt.plot(k_range, k_score, 'o-', color='blue', linewidth=2, markersize=8)
    plt.xlabel('K值')
    plt.ylabel('交叉验证准确率')
    plt.title('K值与模型性能关系曲线')
    plt.axvline(x=best_k, color='red', linestyle='--', label=f'最优K={best_k}')
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

#========================构建skllearn的KNN模型======================
def sklearn_knn(k=3, x_train_std=None, y_train=None, x_test_std=None, y_test=None, distance_metric="euclidean", weights="uniform", average="micro"):
    knn = KNeighborsClassifier(n_neighbors=k, metric=distance_metric, weights=weights)#创建KNN分类器
    knn.fit(x_train_std, y_train)#训练
    y_predict = knn.predict(x_test_std)#预测
    acc  = accuracy_score(y_test, y_predict)#评估
    prec = precision_score(y_test, y_predict,average=average)
    rec  = recall_score(y_test, y_predict,average=average)
    f1   = f1_score(y_test, y_predict,average=average)
    return acc,prec,rec,f1

def main(best_k=3, x_train_std=None, y_train=None, x_test_std=None, y_test=None):
    
    distance_list = ["euclidean", "manhattan", "chebyshev"]
    weight_list = ["uniform", "distance"]
    average_list = ["micro", "macro"]

    labels = []
    acc_list = []
    f1_list = []

    print("="*60)
    print(f"最优K = {best_k} 模型对比结果")
    print("="*60)

    for dist in distance_list:
        for weight in weight_list:
            for average in average_list:
                acc, prec, rec, f1 = sklearn_knn(
                    k=best_k, distance_metric=dist, weights=weight, average=average,
                    x_train_std=x_train_std, y_train=y_train, x_test_std=x_test_std, y_test=y_test
                )
                # 构造标签
                label = f"{dist[:3]}\n{weight}\n{average}"
                labels.append(label)
                acc_list.append(acc)
                f1_list.append(f1)

                print(f"距离:{dist:10} | 权重:{weight:8} | 平均:{average:5}")
                print(f"准确率:{acc:.4f} | 精确率:{prec:.4f} | 召回率:{rec:.4f} | F1:{f1:.4f}\n")

    print("="*60)

    # =================== 绘制对比图 ===================
    x = np.arange(len(labels))
    width = 0.35

    plt.figure(figsize=(16, 8))
    plt.bar(x - width/2, acc_list, width, label='准确率', color='skyblue')
    plt.bar(x + width/2, f1_list, width, label='F1分数', color='orange')

    plt.xlabel('模型组合（距离/权重/平均）')
    plt.ylabel('分数')
    plt.title(f'最优K={best_k} 不同参数模型对比图')
    plt.xticks(x, labels, fontsize=9)
    plt.ylim(0.92, 1.0)  # 放大看差异
    plt.legend()
    plt.grid(alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    x_train_std, x_test_std, y_train, y_test = load_and_preprocess_data(load = load_digits())#加载数据并预处理
    best_k,best_score,k_score = find_best_k(x_train_std, y_train)#寻找最优K值
    print("="*50)
    print(f"K值: {best_k}\n最佳得分: {best_score:.4f}")
    print("="*50)

    main(best_k, x_train_std, y_train, x_test_std, y_test)
    plot_class_distribution(y=y_train)
    plot_all_features_distribution(x_train_std=x_train_std)
    plot_k_performance_curve(k_range=range(1,31), k_score=k_score, best_k=best_k)        # 2. K值性能曲线






    