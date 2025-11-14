# Example Daily ETL Pipeline

This document describes the `example_daily_etl` DAG used in the Airflow data platform project.

## Goal

Simulate a production-style **daily batch ETL** job:
- Extract raw data from a source
- Transform / clean it
- Load it into an analytics-friendly table

## DAG: `example_daily_etl`

**Schedule:** `@daily`  
**Owner:** `riddhi_jain`  
**Tasks:**  

1. `extract_raw_data`
   - Simulates pulling data from a CSV/API/object storage.
   - In a real system, this might read from S3, a database, or a REST endpoint.

2. `transform_data`
   - Represents business logic: cleaning, casting types, filtering bad rows.
   - This is where Python + SQL transformations would normally live.

3. `load_into_target`
   - Simulates writing the transformed data into a warehouse table.
   - In a real setup, this could be PostgreSQL, Redshift, BigQuery, etc.

## Reliability Features

- **Retries:** each task is configured with a retry (5-minute delay).
- **No backfill:** `catchup=False` so only new scheduled runs are executed.
- **Tags:** the DAG is tagged with `etl`, `example`, and `data-platform` for easy filtering in the Airflow UI.

## How this maps to a real project

- Shows a clear `extract -> transform -> load` pattern.
- Uses Python callables with `PythonOperator` to keep logic modular.
- Can be extended to:
  - read real files
  - validate schema
  - integrate with PostgreSQL / S3 / warehouses
