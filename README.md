# ETL-Framework

# Enterprise Metadata-Driven ETL Framework

## Overview

The Enterprise Metadata-Driven ETL Framework is a configurable Python application that extracts data from multiple REST APIs, transforms the data using metadata-driven mappings, and loads the processed data into Amazon S3.

The framework is designed to support multiple source systems without changing the application code. New APIs can be integrated by simply adding a new metadata JSON configuration.

---

## Features

- Metadata-driven ETL
- REST API Integration
- OAuth 2.0 Authentication
- Basic Authentication
- API Key Authentication
- Dynamic JSON Configuration
- Page-Based Pagination
- Offset-Based Pagination
- Cursor/Token-Based Pagination
- Automatic JSON Flattening
- Dynamic Column Mapping
- Data Validation
- Data Transformation
- Amazon S3 Loader
- Enterprise Logging
- Airflow Scheduling
- Exception Handling
- Unit Testing
- Configuration-Driven Processing

---

## Architecture

```
                +-----------------------+
                | Metadata JSON Files   |
                +-----------+-----------+
                            |
                            v
                    Config Reader
                            |
                            v
                    Authentication
                            |
                            v
                      API Client
                            |
                            v
                      Pagination
                            |
                            v
                   JSON Flattener
                            |
                            v
                    Mapping Engine
                            |
                            v
                     Transformer
                            |
                            v
                      Validation
                            |
                            v
                       Amazon S3
                            |
                            v
                Logs & Monitoring
```

---

## Project Structure

```text
metadata_etl_framework/
│
├── main.py
├── requirements.txt
├── README.md
├── config/
├── src/
├── airflow/
├── tests/
├── logs/
├── output/
└── docs/
```

---

## Technology Stack

- Python 3.12
- Requests
- Pandas
- SQLAlchemy
- Boto3
- PyArrow
- PyYAML
- Apache Airflow
- JSON
- REST API
- Amazon S3

---

## Workflow

1. Read metadata JSON files.
2. Authenticate with the API.
3. Retrieve data using pagination.
4. Flatten nested JSON.
5. Apply metadata-driven mappings.
6. Perform transformations.
7. Validate data quality.
8. Save output to Amazon S3.
9. Write logs for monitoring.

---

## Supported Authentication

- OAuth 2.0
- Basic Authentication
- API Key Authentication

---

## Supported Pagination

- Page Number Pagination
- Offset Pagination
- Cursor Pagination
- Token-Based Pagination

---

## Configuration

The framework reads all JSON files placed inside the `config/` folder automatically.

Example:

```
config/
├── cloudiq.json
├── puppet.json
├── rubrik.json
└── vrops.json
```

No code changes are required when a new source configuration is added.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/metadata_etl_framework.git
```

Navigate to the project directory:

```bash
cd metadata_etl_framework
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python main.py
```

---

## Logging

Application logs are written to the `logs/` directory.

Example:

```
2026-07-14 10:30:15 INFO ETL Framework Started
2026-07-14 10:30:20 INFO Reading cloudiq.json
2026-07-14 10:30:30 INFO Authentication Successful
2026-07-14 10:31:10 INFO Data Loaded Successfully to Amazon S3
```

---

## Future Enhancements

- GraphQL API Support
- Parallel API Processing
- Delta Lake Integration
- AWS Lambda Deployment
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline using GitHub Actions

---

## Author

**Shaik Rahamat**

Senior Data Engineer

Python | REST API | Metadata-Driven ETL | Amazon S3 | Airflow | SQL | Pandas | Enterprise Data Engineering
