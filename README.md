<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

<!-- START Apache Airflow, please keep comment here to allow auto update of PyPI readme.md -->
# Apache Airflow Data Platform (Maintained by Riddhi Jain)

This repository is an **end-to-end data-pipeline orchestration system** built using Apache Airflow.  
It automates **ETL workflows, task scheduling, and data quality monitoring** in a modular, cloud-ready architecture.

### 🚀 Key Highlights
- **End-to-end orchestration:** Designed scalable DAGs for multi-source ETL (CSV → PostgreSQL → S3).  
- **Containerized deployment:** Configured Airflow via Docker Compose with isolated dev/prod environments.  
- **CI/CD automation:** Implemented GitHub Actions pipeline for automated DAG linting + deployment.  
- **Monitoring & Alerts:** Integrated email + Slack notifications for task failures and SLA breaches.  
- **Semantic versioning & release workflow:** Published initial release v0.1.0 following OSS standards.

### 🧰 Tech Stack
Python · Apache Airflow · Docker · PostgreSQL · AWS S3 · GitHub Actions · CI/CD · Bash

## Attribution
This platform is built **using** the open-source project **Apache Airflow**.  
- Upstream: https://github.com/apache/airflow  
- License: Apache-2.0 (upstream license header retained at top)  
- Maintainer of this platform repo: **Riddhi Jain**
