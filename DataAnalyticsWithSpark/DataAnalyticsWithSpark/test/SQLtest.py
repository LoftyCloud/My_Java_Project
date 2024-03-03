# coding=gbk
"""
hive mySQL连接测试
"""
import findspark

findspark.init()

from pyspark import SparkConf, SparkContext, HiveContext
from pyspark.sql.session import SparkSession

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
    .getOrCreate()
hive_context = HiveContext(spark)
hive_context.sql("use pyspark")


# 生成查询的SQL语句，这个跟hive的查询语句一样，所以也可以加where等条件语句
def data_read(hive_table):
    """
    读取表数据，打印前五行
    @param hive_table:表名
    @return:
    """
    hive_table = "data0"
    hive_read = "select * from {}".format(hive_table)
    # 通过SQL语句在hive中查询的数据直接是dataframe的形式
    read_df = hive_context.sql(hive_read)
    read_df.show(5)
    return read_df


def write_data(hive_table, df):
    """
    写入表数据
    @param hive_table: 表名
    @param df: 数据流
    @return:
    """
    hive_create_table = """
        create external table if not exists {} (
        ProductBrand string,
        Price int,
        NumImages int,
        PrimaryColor string,
        Sexuality int,
        Adult int,
        Disc_len int,
        Name_len int
    ) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
    """.format(hive_table)
    hive_context.sql(hive_create_table)
    df.write.saveAsTable(hive_table)


df1 = data_read("data0")
write_data("data_test", df1)
df2 = data_read("data_test")


# def read_table():
#     sql_cmd = """SELECT * FROM data0 where gender = 'Unisex'"""
#     df = spark.sql(sql_cmd)
#     df2 = spark.table('data0')
#     df.show(5)
#     df2.show(5)
#
#
# def show_databases():
#     sql_cmd = """show databases"""
#     spark.sql(sql_cmd).show()


# show_databases()
