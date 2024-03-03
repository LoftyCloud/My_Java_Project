# -*- coding: UTF-8 -*-
# 数据清洗
import findspark

findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import when, size, split
from pyspark.sql.session import SparkSession


class DataExtract:
    """
    数据清洗类，将数据读取为dataframe传入后作为成员变量，对其进行修改
    """

    def __init__(self, data, savePath):
        """
        @param data: <class 'pyspark.sql.dataframe.DataFrame'>
        @param savePath: 保存路径
        """
        self.savePath = savePath  # 写文件路径
        self.data = data

    def show_col(self):
        """
        打印前十行
        @return:
        """
        self.data.show(10)

    def delete(self, col_list):
        """
        去除不需要的列
        @param col_list:列名组成的列表
        @return:
        """
        for i in col_list:
            self.data = self.data.drop(i)

    def rename_col(self):
        """
        对列名进行重命名
        @param data:
        @return:
        """
        self.data = self.data.withColumnRenamed("Price (INR)", "Price")

    def distinct(self):
        """
        删除重复值
        @return:
        """
        self.data = self.data.distinct()

    def setDefulatColor(self):
        """
        缺失值处理，颜色有7%的缺失值，将PrimaryColor中的空值替换为"Unknown"
        @return:
        """
        # 缺失值处理，将
        self.data = self.data.withColumn("PrimaryColor",
                                         when(self.data.PrimaryColor.isNull(), "Unknown").otherwise(
                                             self.data.PrimaryColor))
        # self.data.show(10)

    def harnomy(self):
        """
        一致化处理，主要将数据格式统一并将gender拆分为gender和age，方便后续分析
        新增desc_len和name_len列
        @return:
        """
        self.data = self.data.withColumn("Sexuality",
                                         when(self.data.Gender == "Men", 0)
                                         .when(self.data.Gender == "Women", 1)
                                         .when(self.data.Gender == "Boys", 0)
                                         .when(self.data.Gender == "Girls", 1)
                                         .otherwise(2)) \
            .withColumn("Adult",
                        when(self.data.Gender == "Men", 1)
                        .when(self.data.Gender == "Women", 1)
                        .when(self.data.Gender == "Unisex", 1)
                        .otherwise(0)) \
            .withColumn("Disc_len", size(split(dataDf.Description," ")))\
            .withColumn("Name_len", size(split(dataDf.ProductName," ")))

    def writeCsv(self):
        """
        打印前10行数据，并保存修改后的数据
        @return:
            """
        self.data.show(10)
        # print(type(self.data))
        self.data\
            .repartition(1) \
            .write \
            .csv(self.savePath, mode="overwrite",header=True)

    def washData(self):
        self.distinct()
        self.harnomy()
        list = ['ProductID', 'ProductName', 'Description', 'Gender']
        self.delete(list)
        self.setDefulatColor()  # 颜色空缺值填写
        self.rename_col()
        self.show_col()
        self.writeCsv()


if __name__ == "__main__":
    filePath = "F:/Study/spark/dataset/myntra_products_catalog.csv"  # 读文件路径
    savePath = "./data/save_file.csv"
    # 定义spark驱动器
    conf = SparkConf()\
        .setMaster("local[2]")\
        .setAppName("DataWash")\
        .set('spark.executor.memory', '20G')
    sc = SparkContext(conf=conf)  # 定义驱动器对象，sparksession的子对象
    sc.setLogLevel("ERROR")  # OFF.FATAL.ERROR.WARN.INFO.DEBUG.TRACE.ALL，设置日志级别
    spark = SparkSession(sc)
    # 读取文件
    dataDf = spark.read.csv(filePath, multiLine=True, inferSchema=True, header=True)  # dataframe
    # 创建数据清洗类
    dataFxtract = DataExtract(dataDf, savePath)

    dataFxtract.washData()

    # while True:
    #     pass

    sc.stop()
