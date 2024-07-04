from pyspark.sql import SparkSession

def load_to_mysql():
    spark = SparkSession.builder.appName("LoadToMySQL").getOrCreate()
    
    # Load transformed ETF data
    etf_df = spark.read.csv('data/transformed_etfs.csv', header=True, inferSchema=True)
    etf_df.write.format('jdbc').options(
        url='jdbc:mysql://hostname:port/dbname',
        driver='com.mysql.jdbc.Driver',
        dbtable='etfs',
        user='username',
        password='password'
    ).mode('append').save()
    
    # Load transformed economic indicators
    data_types = ['leading', 'coincident', 'lagging']
    for data_type in data_types:
        df = spark.read.csv(f'data/transformed_{data_type}_indicators.csv', header=True, inferSchema=True)
        df.write.format('jdbc').options(
            url='jdbc:mysql://hostname:port/dbname',
            driver='com.mysql.jdbc.Driver',
            dbtable=f'{data_type}_indicators',
            user='username',
            password='password'
        ).mode('append').save()
        print(f"Loaded {data_type} indicators to MySQL successfully.")

if __name__ == "__main__":
    load_to_mysql()
    print("Data loaded into MySQL successfully.")
