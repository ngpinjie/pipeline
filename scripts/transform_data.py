import pandas as pd
from pyspark.sql import SparkSession

def transform_etf_data():
    spark = SparkSession.builder.appName("ETL").getOrCreate()
    df = pd.read_csv('data/etfs.csv')
    spark_df = spark.createDataFrame(df)
    # Perform transformations
    transformed_df = spark_df.withColumn('expense_ratio', spark_df['expense_ratio'] / 100)
    transformed_df.write.csv('data/transformed_etfs.csv', header=True)
    return transformed_df

def transform_economic_data():
    spark = SparkSession.builder.appName("ETL").getOrCreate()
    data_types = ['leading', 'coincident', 'lagging']
    for data_type in data_types:
        df = pd.read_csv(f'data/{data_type}_indicators.csv')
        spark_df = spark.createDataFrame(df)
        # Perform transformations
        transformed_df = spark_df.withColumn('value', spark_df['value'] * 1.0)
        transformed_df.write.csv(f'data/transformed_{data_type}_indicators.csv', header=True)
        print(f"Transformed {data_type} indicators successfully.")

if __name__ == "__main__":
    transform_etf_data()
    transform_economic_data()
    print("Data transformation complete.")