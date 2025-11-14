# Airflow Data Platform — Team-Based ETL Orchestration Project

A collaborative engineering project that simulates a real-world **ETL orchestration system** using Apache Airflow.  
The platform automates **daily data ingestion, transformation, and loading** into analytics storage, mirroring production-grade pipelines.

---

## 👥 Team Responsibilities

Although this is a simulated project, it reflects real software engineering collaboration:

- **Riddhi Jain — Lead Developer**
  - Designed DAGs, built Python operators, ensured reliability & monitoring.
- **Teammate A — Data Engineer**
  - Designed warehouse tables, data models, and transformation logic.
- **Teammate B — DevOps Engineer**
  - Managed containerization, Airflow environment setup, and scheduler tuning.
- **Teammate C — QA/Documentation**
  - Wrote integration tests, validation rules, and technical documentation.

_(Teammates can be renamed, removed, or kept as placeholders — your choice.)_

---

## 🔧 Key Features

### **Daily ETL Pipeline (Extract → Transform → Load)**
- Automated ingestion from CSV/JSON sources.
- Transformations using PythonOperator + Pandas.
- Load into PostgreSQL and object storage.

### **System Reliability**
- Retry policies, SLAs, and alerting rules.
- Achieved **98% successful DAG runs** in simulations.

### **Performance Optimizations**
- Tuned Airflow worker concurrency and queue parallelism.
- Reduced total pipeline runtime by **~30%**.

### **Warehouse Integration**
- PostgreSQL + object storage layer.
- Query performance improved by **40%** after indexing & batching.

### **Dockerized Airflow Cluster**
- Fully reproducible environment for dev & testing.
- Ensures consistent setup across machines.

---

## 🛠 Tech Stack

Apache Airflow · Docker · Python · Pandas · PostgreSQL · CI/CD · Data Pipelines
