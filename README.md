# End-to-End Databricks Data Engineering Project — Digital Marketing Analytics

![Cover](images/cover.png)

An end-to-end Data Engineering portfolio project built on **Databricks**, following the **Medallion Architecture** (Bronze → Silver → Gold), with a **Genie Agent** on top for natural-language Q&A over the data.

---

## 📌 Project Overview

![Business Problem](images/business-problem--and--data-sources.png)

This project simulates a **Digital Marketing Analytics** platform — tracking ad campaigns, daily ad performance, customer conversions, and customer profiles — and builds a complete pipeline from raw files to business-ready aggregated tables, finished off with a Genie Agent that lets anyone ask questions in plain English.

**Why this project:** built as a portfolio/interview-ready showcase of core Data Engineering skills — ingestion, data modeling (star schema + SCD Type 1), aggregation design, and AI-powered self-serve analytics.

---

## 🏗️ Architecture

![Complete Pipeline DAG](images/complete-pipeline-dag.png)
![Ingestion Architecture](images/ingestion-architecture-overview.png)

### Medallion Architecture Breakdown

#### Bronze Layer
![Bronze Layer](images/bronze-layer.png)

#### Silver Layer
![Silver Layer](images/silver-layer.png)
![Star Schema](images/star-schema.png)
![SCD Type 1 with CDC](images/scd-type-1-with-cdc.png)

#### Gold Layer
![Gold Layer](images/gold-layer.png)
![Marketing Funnel Metrics](images/marketing-funnel-metrics.png)
![Customer Segmentation](images/customer-segmentation.png)

---

## 📂 Data Sources

Raw files land in Databricks **Volumes** before ingestion.

![Handling CSV and Nested JSON](images/handling-csv-and-nested-json.png)
![PySpark JSON Parsing](images/pyspark-json-parsing.png)

| File | Description |
|---|---|
| `campaign_master.csv` | Campaign reference data — `campaign_id`, `campaign_name`, `channel`, `start_date`, `budget_usd` |
| `ad_performance.csv` | Daily, per-campaign ad metrics — `campaign_id`, `date`, `impressions`, `clicks`, `spend_usd`, `device` |
| `conversions.json` | Nested conversion events per campaign/day — each record has a `conversion` array of `{customer_id, conversion_type, revenue_usd}` |
| `customer_profile.csv` | Customer dimension — `customer_id`, `signup_date`, `region`, `segment` |

Sample data: 5 campaigns, 25 customers, ~118 rows of ad performance, ~107 top-level conversion records spanning ~70 days.

---

## 🛠️ Tech Stack

![Technology Stack](images/technology-stack.png)

- **Platform:** Databricks (Unity Catalog, Auto Loader, Delta Lake, Genie)
- **Languages:** PySpark, SQL
- **Architecture pattern:** Medallion (Bronze → Silver → Gold)
- **Data modeling:** Star schema with Slowly Changing Dimensions (SCD Type 1)

---

## 🧞 Databricks Genie

![Databricks Genie](images/databricks-genie.png)

Natural language Q&A over the gold layer tables, enabling self-serve analytics.

---

## 🙋 About

Built by **Nisha**

![Thank You](images/thank-you.png)
