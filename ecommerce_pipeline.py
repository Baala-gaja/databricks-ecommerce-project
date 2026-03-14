# Databricks notebook source
df = spark.table("workspace.default.data_sample")

display(df)

# COMMAND ----------

df.write.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.bronze_online_retail")

# COMMAND ----------

bronze_df = spark.table("workspace.default.bronze_online_retail")

display(bronze_df)

# COMMAND ----------

silver_df = bronze_df.filter("Quantity > 0") \
.dropna(subset=["CustomerID"])

display(silver_df)

# COMMAND ----------

silver_df.write.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.silver_online_retail")

# COMMAND ----------

from pyspark.sql.functions import col

gold_df = silver_df.withColumn(
    "Revenue",
    col("Quantity") * col("UnitPrice")
)

display(gold_df)

# COMMAND ----------

country_sales = gold_df.groupBy("Country") \
.sum("Revenue") \
.orderBy("sum(Revenue)", ascending=False)

display(country_sales)

# COMMAND ----------

top_products = gold_df.groupBy("Description") \
.sum("Quantity") \
.orderBy("sum(Quantity)", ascending=False)

display(top_products)

# COMMAND ----------

from pyspark.sql.functions import sum, col

country_sales = gold_df.groupBy("Country") \
    .agg(sum("Revenue").alias("Total_Revenue")) \
    .orderBy(col("Total_Revenue").desc())

display(country_sales)

# COMMAND ----------

country_sales.write.format("delta") \
.mode("overwrite") \
.saveAsTable("workspace.default.gold_country_sales")