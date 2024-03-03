import findspark

findspark.init()
from pyspark import SparkConf, SparkContext
from pyspark.sql.session import SparkSession


def count_line(streamdf):  # 计数，并打印出第一行数据
    streamrdd = streamdf.rdd  # 所得RDD由ROW对象组成
    numlines = streamrdd.count()  # 12491

    # print(streamdf.take(1))
    # streamdf.show(10)

    print(numlines)

    # 期望：12492 输出：12762,2184,12491


def write_data(streamdf):  # 写为csv
    save_path = "../data/save_file.csv"
    # rdd.saveAsTextFile(save_path)
    streamdf.write.csv(save_path, header=True)


def data_extract(streamdf):  # 数据清洗
    # streamdf.columns:
    # ['ProductID', 'ProductName', 'ProductBrand', 'Gender',
    # 'Price (INR)', 'NumImages', 'Description', 'PrimaryColor']
    extractdf = streamdf \
        .distinct() \
        .filter(streamdf['Price (INR)'] > 1000) \
        .drop(streamdf.Description) \
        .select('ProductName', 'Price (INR)') \
        # .show(10)
    return extractdf


def show_gender(streamdf):  # 根据性别统计
    # genderrdd = streamdf.select(streamdf.Gender).rdd \
    #     .map(lambda gender: (gender, 1))    # 转成（gender,1）的形式
    # print(genderrdd.count())  # 2184
    # print(streamdf.rdd.count())  # 12491

    genderrdd = streamdf \
        .rdd \
        .map(lambda x: x.Gender) \
        .map(lambda gender: (gender, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .sortByKey(ascending=True)
    genderrdd.foreach(print)  # 计算每个性别的人数，共6种
    # print(1)


def show_price(streamdf):  # 500为一个区间，计算每个区间的数量
    # a = streamdf.rdd.map(lambda x: x[4]).take(10)
    # print(a)
    # 前十个值：[11745, 5810, 899, 5599, 759, 791, 719, 899, 664, 17360]
    # 以500为区间，计算各价格区间的数量，大于10000的统一计算
    step = 500
    max_limit = 10000
    pricerdd = streamdf \
        .rdd \
        .map(lambda x: x[4]) \
        .map(lambda x: max_limit if x > max_limit else x) \
        .map(lambda price: (int(price / step), 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .map(lambda x: (x[0] * step, x[1])) \
        .sortByKey(ascending=True)
    # .collect() 返回RDD中元素组成的列表
    pricerdd.foreach(print)


if __name__ == '__main__':
    '''
    1、驱动器程序通过对象SparkContext（即sc）连接spark集群,在spark shell中会自动初始化sc，这里需要自定义一个sc
    2、setMaster为集群URL：即让spark连接到指定集群上，local指的是单机单线程运行，而不必运行在集群上
    3、链接到本地spark
    '''
    conf = SparkConf().setMaster("local[2]").setAppName("DataAnalysis").set('spark.executor.memory', '10G')
    sc = SparkContext(conf=conf)  # 定义驱动器对象，sparksession的子对象
    sc.setLogLevel("ERROR")  # OFF.FATAL.ERROR.WARN.INFO.DEBUG.TRACE.ALL，设置日志级别
    spark = SparkSession(sc)
    # print(conf.toDebugString())  # 打印配置项

    # 读取文件，返回一个RDD
    file_path = "F:/Study/spark/dataset/myntra_products_catalog.csv"
    # rdd = sc.textFile(file_path)  # 无法多行读取
    # data = sc.textFile(file_path)  # <class 'pyspark.rdd.RDD'>

    dataf = spark.read.csv(file_path, multiLine=True, inferSchema=True, header=True)  # dataframe
    # print(type(dataf))  # <class 'pyspark.sql.dataframe.DataFrame'>
    print(dataf.describe)

    # 对读取的RDD进行操作
    # count_line(dataf)
    # write_data(dataf)
    # dataf = data_extract(dataf)
    # show_gender(dataf)
    # show_price(dataf)

    # 防止程序运行后无法访问4040端口
    # while True:
    #     pass

