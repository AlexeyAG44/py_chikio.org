import requests
from urllib.parse import quote
from random import choice
import csv
import pandas as pd
from pyspark.sql.session import SparkSession
import os

CSV = 'test_request.csv'


def check_request(url, retry=10):
    try:
        response = requests.get(url=url, headers=random_headers(), verify=False)
        # print(f"[STATUS CODE]: {response.status_code}, сonnection complete => URL: {quote(url)}")
    except Exception as ex:
        if retry:
            # print(f"[INFO] retry = {retry} => URL: {quote(url)}")
            return check_request(url, retry=(retry - 1))
        else:
            raise
    else:
        return response


def get_data_subjects():
    url_all_subjects = "https://pkk.rosreestr.ru/server/rest/services/Hosted/tbl_data_18_19_20/FeatureServer/0/query?f=json&where=(val%3C%3E0)%20AND%20(deal_q_num%3D%27I%20%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B0%D0%BB%27)%20AND%20(deal_year%3D%272018%27)%20AND%20(deal_type%3D%27%D0%92%D1%81%D0%B5%D0%B3%D0%BE%20%D1%81%D0%B4%D0%B5%D0%BB%D0%BE%D0%BA%27)&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&groupByFieldsForStatistics=subj_name&orderByFields=value%20desc&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22val%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&resultType=standard"
    result_list_subjects = []
    response_all_subjects = check_request(url_all_subjects)
    data_subj = response_all_subjects.json()
    for item in data_subj["features"]:
        result_list_subjects.append(item.get('attributes').get('subj_name'))
    return result_list_subjects


def get_data_quarter():
    url_quarter = "https://pkk.rosreestr.ru/server/rest/services/Hosted/tbl_data_18_19_20/FeatureServer/0/query?f=json&where=(deal_year%3D%272018%27)%20AND%20(deal_type%3D%27%D0%92%D1%81%D0%B5%D0%B3%D0%BE%20%D1%81%D0%B4%D0%B5%D0%BB%D0%BE%D0%BA%27)%20AND%20(subj_name%3D%27%D0%90%D0%BB%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D1%80%D0%B0%D0%B9%27)&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&groupByFieldsForStatistics=deal_q_num&orderByFields=deal_q_num%20asc&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22val%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&resultType=standard"
    result_list_quarter = []
    response_quarter = check_request(url_quarter)
    data_quarter = response_quarter.json()
    for item in data_quarter["features"]:
        result_list_quarter.append(item.get('attributes').get('deal_q_num'))
    return result_list_quarter


def get_data_types_contract():
    url_types_contract = "https://pkk.rosreestr.ru/server/rest/services/Hosted/tbl_data_18_19_20/FeatureServer/0/query?f=json&where=deal_type%3C%3E%27%D0%9A%D1%83%D0%BF%D0%BB%D1%8F%5C%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&groupByFieldsForStatistics=deal_type&orderByFields=deal_type%20asc&outStatistics=%5B%7B%22statisticType%22%3A%22count%22%2C%22onStatisticField%22%3A%22deal_type%22%2C%22outStatisticFieldName%22%3A%22count_result%22%7D%5D&resultType=standard"
    result_list_type_contract = []
    response_types_contract = check_request(url_types_contract)
    data_types_contract = response_types_contract.json()
    for item in data_types_contract["features"]:
        result_list_type_contract.append(item.get('attributes').get('deal_type'))
    return result_list_type_contract


def get_data_year():
    url_year = "https://pkk.rosreestr.ru/server/rest/services/Hosted/tbl_data_18_19_20/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&groupByFieldsForStatistics=deal_year&orderByFields=deal_year%20asc&outStatistics=%5B%7B%22statisticType%22%3A%22count%22%2C%22onStatisticField%22%3A%22deal_year%22%2C%22outStatisticFieldName%22%3A%22count_result%22%7D%5D&resultType=standard"
    result_list_year = []
    response_year = check_request(url_year)
    data_year = response_year.json()
    for item in data_year["features"]:
        result_list_year.append(item.get('attributes').get('deal_year'))
    result_list_year.reverse()
    return result_list_year


def random_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
    return {'User-Agent': choice(user_agents), "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}


def save_doc(items, path):
    with open(path, "w", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['deal_type', 'period', 'subject', 'count_of_deals'])
        for item in items:
            writer.writerow([item['deal_type'], item['period'], item['subject'], item['count_of_deals']])


def create_pd_df(csv):
    df = pd.read_csv(csv, index_col=False, delimiter=';')
    return df.sort_values(['period', 'deal_type'], ascending=[False, True])


def create_spark_df(df_new):
    os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-11-openjdk-amd64"  # /usr/lib/jvm/java-8-openjdk-amd64
    os.environ['SPARK_HOME'] = "/opt/spark"
    os.environ['PYSPARK_PYTHON'] = "/home/sa/PycharmProjects/pythonProject/venv/bin/python3"
    os.environ['HADOOP_HOME'] = "/home/hadoopuser/hadoop"
    os.environ['PYSPARK_DRIVER_PYTHON'] = "/home/sa/PycharmProjects/pythonProject/venv/bin/python3"

    spark = SparkSession \
        .builder \
        .appName("spark_session1") \
        .config("spark.jars", "/home/sa/PycharmProjects/pythonProject/postgresql-42.4.1.jar") \
        .getOrCreate()
    df_spark = spark.createDataFrame(df_new)
    df_spark.write.save("/tmp/test/", format='parquet', mode='overwrite')
    spark.read.parquet("/tmp/test/")

    df_spark.write.format('jdbc') \
        .mode('overwrite') \
        .option('url', "jdbc:postgresql://localhost:5432/postgres") \
        .option('dbtable', "public.smartphones") \
        .option('user', "postgres") \
        .option('password', "1Qwerty") \
        .option('driver', "org.postgresql.Driver") \
        .option("stringtype", "unspecified") \
        .save()


def main():
    result_list_type_contract = get_data_types_contract()
    result_list_year = get_data_year()
    result_list_year.reverse()
    result_list_quarter = get_data_quarter()
    result_list_subjects = get_data_subjects()

    result_list = []
    for type_contract in result_list_type_contract:
        for quarter in result_list_quarter:
            for year in result_list_year:
                for subject in result_list_subjects:
                    url = f"""https://pkk.rosreestr.ru/server/rest/services/Hosted/tbl_data_18_19_20/FeatureServer/0/query?f=json&where=(deal_q_num='{quote(quarter)}') AND (deal_year='{quote(year)}') AND (deal_type='{quote(type_contract)}') AND (subj_name='{quote(subject)}')&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=[{{"statisticType":"sum","onStatisticField":"val","outStatisticFieldName":"value"}}]&resultType=standard"""
                    response_quarter = check_request(url)
                    data_quarter = response_quarter.json()
                    for item in data_quarter["features"]:
                        check_request(url)
                        if item.get('attributes').get('value') != None:
                            result_list.append(
                                {
                                    "deal_type": type_contract,
                                    "period": year + " " + quarter,
                                    "subject": subject,
                                    "count_of_deals": item.get('attributes').get('value')
                                }
                            )
                    save_doc(result_list, CSV)
    pd_df = create_pd_df(CSV)
    create_spark_df(pd_df)


if __name__ == "__main__":
    main()
