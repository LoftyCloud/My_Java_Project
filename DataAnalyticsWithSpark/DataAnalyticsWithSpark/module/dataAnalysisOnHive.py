# -*- coding: UTF-8 -*-
# 数据分析
import re

import findspark

findspark.init()

from pyspark import SparkConf, SparkContext, HiveContext
from pyspark.sql.functions import when, size, split
from pyspark.sql.session import SparkSession


def data_read(hive_table):
    """
    读取表数据，打印前五行
    @return:
    """
    hive_read = "select * from {}".format(hive_table)
    # 通过SQL语句在hive中查询的数据直接是dataframe的形式
    read_df = hive_context.sql(hive_read)
    # read_df.show(5)
    return read_df

def read_table(table_name):
    hive_read = "select * from {}".format(table_name)
    # 通过SQL语句在hive中查询的数据直接是dataframe的形式
    read_df = hive_context.sql(hive_read)
    read_df.show(5)


def data_num(df):
    """
    统计数据数目
    @param df:
    @return:
    """
    # df_num = spark.createDataFrame([df.count()]) \
    #     .toDF("num")
    # df_num.write.saveAsTable("data_num")
    return df.count()


def data_gender(df):
    """
    性别数据计数
    @param df:
    @return:
    """
    rdd_gender = df.rdd \
        .map(lambda x: x.sexuality) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortByKey(ascending=True)
    rdd_gender.foreach(print)
    # print(type(df_gender))
    df_gender = spark.createDataFrame(rdd_gender).toDF("gender", "num")
    df_gender.write.saveAsTable("data_gender", mode="overwrite")

    read_table("data_gender")


def data_adult(df):
    rdd_adult = df.rdd \
        .map(lambda x: x.adult) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortByKey(ascending=True)
    rdd_adult.foreach(print)
    spark.createDataFrame(rdd_adult) \
        .toDF("age", "num") \
        .write.saveAsTable("data_adult", mode="overwrite")


def data_price(df):
    step = 500
    max_limit = 10000
    rdd_price = df \
        .rdd \
        .map(lambda x: x.price) \
        .filter(lambda x: x is not None) \
        .map(lambda x: max_limit if x > max_limit else x) \
        .map(lambda price: (int(price / step), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[0] * step, x[1])) \
        .sortByKey(ascending=True)
    rdd_price.foreach(print)
    spark.createDataFrame(rdd_price).toDF("price", "num") \
        .write.saveAsTable("data_price", mode="overwrite")


def data_color(df):
    """
    颜色分布
    @param df:
    @return:
    """
    rdd_color = df.rdd \
        .map(lambda x: x.primarycolor) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y).filter(lambda x: x[1] > 5) \
        .sortByKey(ascending=True)
    # rdd_color.foreach(print)
    spark.createDataFrame(rdd_color).toDF("type/color", "num") \
        .write.saveAsTable("data_color", mode="overwrite")
    read_table("data_color")


def data_color_2(df):
    """
    各价格区间最多的color分布，color总数大于50
    @param df:
    @return:
    """
    step = 500
    max_limit = 10000
    rdd_color_2 = df \
        .rdd \
        .map(lambda x: (x.price, x.primarycolor)) \
        .filter(lambda x: x[0] is not None and len(x[1]) > 0) \
        .map(lambda x: (max_limit if x[0] > max_limit else x[0], x[1])) \
        .map(lambda x: (int(x[0] / step), x[1])) \
        .map(lambda x: ((x[0] * 500, x[1]), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[1], x[0])) \
        .filter(lambda x: x[0] > 50) \
        .sortByKey(ascending=False).map(lambda x: (x[1][0], x[1][1], x[0]))
    # print(rdd_color_2.take(5))
    # rdd_color_2.foreach(print)
    spark.createDataFrame(rdd_color_2).toDF("price", "type/color","num") \
        .write.saveAsTable("data_color_2", mode="overwrite")
    read_table("data_color_2")


def data_brand(df):
    """
    各品牌销量对比
    @param df:
    @return:
    """
    rdd_brand = df.rdd \
        .map(lambda x: x.productbrand) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .filter(lambda x: x[1] > 100) \
        .sortByKey(ascending=True)
    # rdd_brand.foreach(print)
    spark.createDataFrame(rdd_brand).toDF("brand_name", "num") \
        .write.saveAsTable("data_brand", mode="overwrite")
    read_table("data_brand")


def data_brand_2(df):
    """
    品牌与非品牌对比，牌子数量与销量
    @param df:
    @return:
    """
    rdd_brand_2 = df.rdd \
        .map(lambda x: x.productbrand) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: ("famous" if x[1] > 100 else "not_famous", (1, x[1]))) \
        .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])).map(lambda x:(x[0],x[1][0],x[1][1]))
    # rdd_brand_2.foreach(print)
    spark.createDataFrame(rdd_brand_2).toDF("brand", "num","sell") \
        .write.saveAsTable("data_brand_2", mode="overwrite")
    read_table("data_brand_2")


def data_disc(df):
    """
    描述长度分布
    @param df:
    @return:
    """
    step = 10
    max_limit = 50
    rdd_disc = df \
        .rdd \
        .map(lambda x: x.disc_len) \
        .filter(lambda x: x is not None) \
        .map(lambda x: max_limit if x > max_limit else x) \
        .map(lambda disc_len: (int(disc_len / step), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[0] * step, x[1])) \
        .sortByKey(ascending=True)
    # rdd_disc.foreach(print)
    spark.createDataFrame(rdd_disc).toDF("len", "num") \
        .write.saveAsTable("data_disc", mode="overwrite")
    read_table("data_disc")


def data_disc_2(df):
    """
    统计长度大于3的单词频数
    @param df:
    @return:
    """
    rdd_disc_2 = df.rdd \
        .map(lambda x: x.description) \
        .filter(lambda x: x is not None) \
        .flatMap(lambda x: re.split("\W+", x)) \
        .filter(lambda x: len(x) > 3) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[1], x[0])) \
        .sortByKey(ascending=False) \
        .map(lambda x: (x[1], x[0])).take(50)
    # print(rdd_disc_2.take(25))
    spark.createDataFrame(rdd_disc_2).toDF("word", "num") \
        .write.saveAsTable("data_disc_2", mode="overwrite")
    read_table("data_disc_2")


def data_name(df):
    """
    name长度分布
    @param df:
    @return:
    """
    step = 5
    max_limit = 20
    rdd_name = df \
        .rdd \
        .map(lambda x: x.name_len) \
        .filter(lambda x: x is not None) \
        .map(lambda x: max_limit if x > max_limit else x) \
        .map(lambda name_len: (int(name_len / step), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[0] * step, x[1])) \
        .sortByKey(ascending=True)
    rdd_name.foreach(print)
    spark.createDataFrame(rdd_name).toDF("len", "num") \
        .write.saveAsTable("data_name", mode="overwrite")
    read_table("data_name")


def data_name_2(df):
    """
        统计长度大于3的单词频数
        @param df:
        @return:
        """
    rdd_name_2 = df.rdd \
        .map(lambda x: x.productname) \
        .filter(lambda x: x is not None) \
        .flatMap(lambda x: re.split("\W+", x)) \
        .filter(lambda x: len(x) > 3) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[1], x[0])) \
        .sortByKey(ascending=False) \
        .map(lambda x: (x[1], x[0])).take(20)
    # print(rdd_name_2.take(15))
    spark.createDataFrame(rdd_name_2).toDF("word", "num") \
        .write.saveAsTable("data_name_2", mode="overwrite")
    read_table("data_name_2")


def data_img(df):
    """
        name长度分布
        @param df:
        @return:
        """
    rdd_img = df \
        .rdd \
        .map(lambda x: x.numimages) \
        .filter(lambda x: x is not None) \
        .filter(lambda x: x < 15) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortByKey(ascending=True)
    rdd_img.foreach(print)
    spark.createDataFrame(rdd_img).toDF("img_num", "num") \
        .write.saveAsTable("data_img", mode="overwrite")
    read_table("data_img")


if __name__ == "__main__":
    # 定义spark驱动器
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

    df = data_read("data_washed")  # 读取清洗后的数据
    df.persist()
    # print(df.dtypes)
    # [('productname', 'string'), ('productbrand', 'string'), ('price', 'int'), ('numimages',
    # 'int'), ('description', 'string'), ('primarycolor', 'string'), ('sexuality', 'int'), ('adult', 'int'),
    # ('disc_len', 'int'), ('name_len', 'int')]

    # data_num(df)
    # print(num)  # 12502
    data_gender(df)
    data_adult(df)
    data_price(df)
    data_color(df)
    data_color_2(df)
    data_brand(df)
    data_brand_2(df)
    data_disc(df)
    data_disc_2(df)
    data_name(df)
    data_name_2(df)
    data_img(df)
