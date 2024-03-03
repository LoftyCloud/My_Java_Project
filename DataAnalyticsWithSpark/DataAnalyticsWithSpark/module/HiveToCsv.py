# -*- coding: UTF-8 -*-
# 读取hive数据库，存入csv文件
# 数据分析
import re

import findspark
findspark.init()

from pyspark import SparkConf, SparkContext, HiveContext
from pyspark.sql.session import SparkSession

conf = SparkConf().setMaster("local[5]") \
    .setAppName("DataAnalysis").set('spark.executor.memory', '100G')
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


def data_read(hive_table):
    """
    读取表数据，打印前五行
    @return:
    """
    hive_read = "select * from {}".format(hive_table)
    # 通过SQL语句在hive中查询的数据直接是dataframe的形式
    read_df = hive_context.sql(hive_read)
    # read_df.show(5)
    # print(1)
    return read_df


def writeCsv(df, savePath):
    """
    并保存修改后的数据
    @return:
        """
    df.repartition(1) \
        .write \
        .csv(savePath, mode="overwrite", header=True)
    df.show(5)
    # print(2)


def read_and_write(table_name, path):
    """
    读出hive数据库、写入路径
    @param table_name:
    @param path:
    @return:
    """
    df = data_read(table_name)
    writeCsv(df, path)
    # print(3)


# read_and_write("data_gender", "file:/F:///Study/spark/DataAnalyticsWithSpark/data")
# read_and_write("data_adult", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_adult")
# read_and_write("data_price", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_price")
# read_and_write("data_color", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_color")
# read_and_write("data_color_2", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_color_2")
# read_and_write("data_brand", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_brand")
# read_and_write("data_brand_2", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_brand_2")
# read_and_write("data_disc", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_disc")
# read_and_write("data_disc_2", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_disc_2")
# read_and_write("data_name", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_name")
# read_and_write("data_name_2", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_name_2")
# read_and_write("data_img", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_img")
read_and_write("data0", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data0")
read_and_write("data_washed", "file:/F:///Study/spark/DataAnalyticsWithSpark/data/data_washed")
