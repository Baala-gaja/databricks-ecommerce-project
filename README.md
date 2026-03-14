# databricks-ecommerce-project
End-to-end E-Commerce Data Pipeline using Databricks Lakehouse Architecture
# Databricks E-Commerce Lakehouse Project

## Project Overview

This project demonstrates an end-to-end data pipeline using the Databricks Lakehouse architecture and the Medallion (Bronze, Silver, Gold) pattern.

The pipeline processes raw e-commerce transaction data and transforms it into business insights.

---

## Dataset

Online Retail Dataset

Source:
https://archive.ics.uci.edu/ml/datasets/online+retail

Note: Due to GitHub file size limits, a sample dataset is included.

---

## Architecture

Medallion Architecture:

Raw Data
   ↓
Bronze Layer (Raw Delta Table)
   ↓
Silver Layer (Cleaned Data)
   ↓
Gold Layer (Business Analytics)

---

## Pipeline

### Bronze Layer
Raw dataset ingested into Delta Lake.

Table:
bronze_online_retail

---

### Silver Layer
Data cleaning operations performed:

• Removed cancelled orders  
• Removed null CustomerID values

Table:
silver_online_retail

---

### Gold Layer
Business analytics tables generated.

Tables:
gold_country_sales

---

## Technologies Used

Databricks  
PySpark  
Delta Lake  
GitHub  

---

## Sample Insights

Top Revenue Countries:

Germany  
France  
Japan  

Top Products:

WORLD WAR 2 GLIDERS ASSTD DESIGNS  
CREAM HEART CARD HOLDER  
BLACK HEART CARD HOLDER  

---

## Lakehouse Architecture

Raw Data → Bronze → Silver → Gold
