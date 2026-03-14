# databricks-ecommerce-project
End-to-end E-Commerce Data Pipeline using Databricks Lakehouse Architecture
# Databricks E-Commerce Lakehouse Project

## Project Overview
This project demonstrates the **Databricks Lakehouse Medallion Architecture** using an E-Commerce dataset.

The pipeline processes raw sales data and transforms it into business insights using **Bronze, Silver, and Gold layers**.

## Dataset
Online Retail Dataset

Source:
https://archive.ics.uci.edu/ml/datasets/online+retail

Note:
Due to GitHub size limits, a sample dataset is included.

---

## Architecture

Bronze Layer → Raw data ingestion  
Silver Layer → Cleaned and filtered data  
Gold Layer → Business analytics tables

---

## Pipeline

### Bronze Layer
Raw dataset stored as Delta table.

Table:

**bronze_online_retail**


---

### Silver Layer
Data cleaning operations performed:

• Remove cancelled orders  
• Remove null customer IDs

Table:

**silver_online_retail**


---

### Gold Layer
Business analytics generated:

• Country-wise revenue  
• Top selling products

Tables:

**gold_country_sales
gold_top_products**


---

## Technologies Used

- Databricks
- PySpark
- Delta Lake
- GitHub

---

## Sample Insights

Top Revenue Countries:
- Germany
- France
- Japan

Top Products:
- WORLD WAR 2 GLIDERS ASSTD DESIGNS
- CREAM HEART CARD HOLDER
- BLACK HEART CARD HOLDER

---

## Lakehouse Architecture

Raw Data → Bronze → Silver → Gold

