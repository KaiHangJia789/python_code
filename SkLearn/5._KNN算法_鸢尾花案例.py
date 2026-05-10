"""
机器学习的研发流程:
1. 数据获取
2. 数据预处理
3. 特征选择
4. 模型训练
5. 模型评估
6. 模型预测
"""

#导入工具包
from sklearn.datasets import load_iris                  #数据集鸢尾花
import seaborn as sns                                   #画图
import pandas as pd                                     #数据处理
import matplotlib.pyplot as plt                         #画图
from sklearn.model_selection import train_test_split    #数据集切分
from sklearn.preprocessing import StandardScaler        #数据预处理标准化
from sklearn.neighbors import KNeighborsClassifier      #KNN算法 分类 
from sklearn.metrics import accuracy_score              #模型评估

#1. 定义函数，加载鸢尾花数据集，并查看数据集

def dm01_load_iris():
    iris_data = load_iris()
    print("数据集的描述:", iris_data.DESCR)
    print("数据集的标签:", iris_data.target_names)
    print("数据集的标签值:", iris_data.target)
    print("数据集的属性:", iris_data.feature_names)
    print("数据集的属性值:", iris_data.data)
    print("数据集的属性值形状:", iris_data.data.shape)
    print("数据集的属性值类型:", iris_data.data.dtype)
    

#2. 绘制数据集的散点图
def dm02_show_iris():
    #1.加载数据集
    iris_data = load_iris()
    #2. 把鸢尾花数据集封装成 DataFrame对象
    iris_df = pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
    #3. 给df 添加标签列
    iris_df['label'] = iris_data.target
    #print(iris_df)

    #4. 通过seaborn 绘制数据集的散点图
    #参一: data: 数据集 参二: x: x轴 参三: y: y轴 参四: hue: 标签列 参五: fit_reg: 是否画出回归线
    sns.lmplot(data=iris_df,x='sepal length (cm)',y = 'sepal width (cm)',hue='label',fit_reg=True)
    
    #5. 设置标题 显示
    plt.title('iris_data')
    plt.tight_layout() #自动调整子图参数，使之填充整个图像区域
    plt.show()

#3. 切分训练集和测试机
def dmo3_split_train_test():
    #1. 加载数据集
    iris_data = load_iris()

    #2. 数据集的预处理 切分训练集和测试集
    #参1: 测试集特征 参2: 测试集标签 参3: 测试集占比 参4: 随机种子
    x_train,x_test,y_train,y_test = train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=22)

    #3. 打印结果
    print(f"训练集特征值:{x_train},个数:{len(x_train)}")    
    print(f"训练集标签值:{y_train},个数:{len(y_train)}")
    print(f"测试集特征值:{x_test},个数:{len(x_test)}")
    print(f"测试集标签值:{y_test},个数:{len(y_test)}")

#4. 实现鸢尾花完整案例-->加载数据，数据预处理，切分训练集和测试集，训练模型，评估模型，预测结果
def dm04_iris_evaluate_test():
    #1. 加载数据集
    iris_data = load_iris()
    #2. 数据集的预处理
    x_train,x_text,y_train,y_test = train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=22)
    #3. 特征提取,预处理
    #3.1 创建标准化对象
    tranfer = StandardScaler()
    #3.2 调用 fit_transform() 方法, 对数据集进行标准化处理
    x_train_std = tranfer.fit_transform(x_train) #fit_transform() 方法(训练，转换), 第一次对数据集进行标准化处理时使用
    x_test_std = tranfer.transform(x_text) #transform() 方法(只有转换), 重复对数据集进行标准化处理时使用
    
    #4. 训练模型
    #4.1创建模型对象
    estimator = KNeighborsClassifier(n_neighbors=3)
    #4.2 调用 fit() 方法, 训练模型
    estimator.fit(x_train_std,y_train) 

    #5 预测结果
    #5.1 调用 predict() 方法, 预测结果
    y_pre = estimator.predict(x_test_std)
    print(f"预测结果:   {y_pre}")

    #5.2 对新的数据集(源数据150个 之外的数据)进行测试
    # 自定义测试集
    my_data= [[5.1,3.5,1.4,0.2]]
    # 对测试集进行标准化处理
    my_data_std = tranfer.transform(my_data)
    # 模型预测
    my_y_pre = estimator.predict(my_data_std)
    print(f"预测结果:   {my_y_pre}")

    #5.4查看上述数据集,每种分类的预测概率
    y_pre_proba = estimator.predict_proba(my_data_std)
    print(f"预测概率:   {y_pre_proba}")

    #6. 评估模型
    #方式一:直接评分
    print(f"正确率: {estimator.score(x_test_std,y_test)}")
    #方式二:基于测试机的标签和预测结果评估
    print(f"准确率: {accuracy_score(y_test,y_pre)}")

if __name__ == '__main__':
    #dm01_load_iris()
    #dm02_show_iris()
    #dmo3_split_train_test()
    dm04_iris_evaluate_test()
