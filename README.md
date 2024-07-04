# Real-Time Financial Data Pipeline

## Overview
This project builds a real-time data pipeline to gather and analyze data on the top three low-expense S&P 500 ETFs and the top three economic indicators. It uses Watsonx.data, Apache Spark, Pandas, MySQL, and OpenShift Container Platform (OCP) for an end-to-end solution.

## Tools and Technologies
- **Watsonx.data**: For managing and analyzing data.
- **Apache Spark**: For distributed data processing.
- **Pandas**: For initial data exploration and transformation.
- **MySQL**: As the target database for storing processed data.
- **OCP**: For deploying and managing the data pipeline.

## Directory Structure
- `data/`: Directory for storing sample and intermediate data files.
- `scripts/`: Python scripts for data ingestion, transformation, and loading.
- `docker/`: Docker-related files for containerization.
- `notebooks/`: Jupyter notebooks for exploratory data analysis.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignore file to exclude unnecessary files from version control.

## Setup
1. Clone the repository:
```
git clone https://github.com/ngpinjie/real-time-financial-data-pipeline.git
cd real-time-financial-data-pipeline
```

2. Install Python dependencies:
```
pip install -r requirements.txt
```

3. Build and run the Docker containers:
```
docker-compose up --build
```

## Usage
1. Run the ETF ingestion script:
```
python scripts/ingest_etfs.py
```

2. Run the economic indicators ingestion script:
```
python scripts/ingest_economic_indicators.py
```

3. Transform the data:
```
python scripts/transform_data.py
```

4. Load the data into MySQL:
```
python scripts/load_to_mysql.py
```

## License
This project is licensed under the MIT License.
