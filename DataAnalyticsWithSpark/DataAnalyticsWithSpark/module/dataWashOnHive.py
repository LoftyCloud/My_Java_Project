# -*- coding: UTF-8 -*-
# 数据清洗
import findspark
findspark.init()

from pyspark import SparkConf, SparkContext, HiveContext
from pyspark.sql.functions import when, size, split
from pyspark.sql.session import SparkSession


class DataExtract:
    """
    数据清洗类，将数据读取为dataframe传入后作为成员变量，对其进行修改
    """

    def __init__(self, data):
        """
        @param data: <class 'pyspark.sql.dataframe.DataFrame'>
        @param savePath: 保存路径
        """
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
        pass

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
        self.data = self.data.withColumn("primarycolor",
                                         when(self.data.primarycolor.isNull(), "Unknown")
                                         .otherwise(self.data.primarycolor))
        # self.data.show(10)

    def harnomy(self):
        """
        一致化处理，主要将数据格式统一并将gender拆分为gender和age，方便后续分析
        新增desc_len和name_len列
        @return:
        """
        self.data = self.data.withColumn("sexuality",
                                         when(self.data.gender == "Men", 0)
                                         .when(self.data.gender == "Women", 1)
                                         .when(self.data.gender == "Boys", 0)
                                         .when(self.data.gender == "Girls", 1)
                                         .otherwise(2)) \
            .withColumn("adult",
                        when(self.data.gender == "Men", 1)
                        .when(self.data.gender == "Women", 1)
                        .when(self.data.gender == "Unisex", 1)
                        .otherwise(0)) \
            .withColumn("disc_len", size(split(self.data.description, " "))) \
            .withColumn("name_len", size(split(self.data.productname, " ")))

    # def writeCsv(self):
    #     """
    #     打印前10行数据，并保存修改后的数据
    #     @return:
    #         """
    #     self.data.show(10)
    #     # print(type(self.data))
    #     self.data \
    #         .repartition(1) \
    #         .write \
    #         .csv(self.savePath, mode="overwrite", header=True)

    def write_data(self, table_name):
        """
        数据写入hive表
        @return:
        """
        self.data.write.saveAsTable(table_name, mode="overwrite")

    def washData(self):
        self.distinct()
        self.harnomy()
        list = ['productid', 'gender']
        self.delete(list)
        self.setDefulatColor()  # 颜色空缺值填写
        self.rename_col()
        # self.show_col()
        # self.writeCsv()
        self.write_data("data_washed")


def data_read(hive_table):
    """
    读取表数据，打印前五行
    @return:
    """
    hive_read = "select * from {}".format(hive_table)
    # 通过SQL语句在hive中查询的数据直接是dataframe的形式
    read_df = hive_context.sql(hive_read)
    read_df.show(5)
    return read_df


def write_data(data, table_name):
    """
    数据写入hive表
    @return:
    """
    data.write.saveAsTable(table_name, mode="overwrite")


if __name__ == "__main__":
    # 定义spark驱动器
    conf = SparkConf().setMaster("local[2]") \
        .setAppName("DataAnalysis").set('spark.executor.memory', '10G')
    sc = SparkContext(conf=conf)  # 定义驱动器对象，sparksession的子对象
    sc.setLogLevel("ERROR")  # OFF.FATAL.ERROR.WARN.INFO.DEBUG.TRACE.ALL，设置日志级别

    _SPARK_HOST = "spark://spark-master:7077"
    _APP_NAME = "test"

    spark = SparkSession \
        .builder \
        .appName("name") \
        .enableHiveSupport() \
        .getOrCreate()  # 启用hive支持
    hive_context = HiveContext(spark)
    hive_context.sql("use pyspark")

    # 读取文件
    dataDF = data_read("data0")
    # 创建数据清洗类
    dataFxtract = DataExtract(dataDF)
    dataFxtract.washData()
    df2 = data_read("data_washed")

    # while True:
    #     pass

