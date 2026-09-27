# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

df_conv = (
    spark.read.table('marketing_analytics_project.`02_silver`.fact_conversions')
    .groupBy('campaign_id', 'date')
    .agg(
        sum('revenue_usd').alias('revenue_usd'),
        sum('add_to_cart').alias('add_to_cart'),
        sum('wishlist').alias('wishlist'),
        sum('purchase').alias('purchase'),
        sum(col('add_to_cart') + col('wishlist') + col('purchase')).alias('total_no_of_conv')
    )
    .withColumn('revenue_usd', round(col('revenue_usd'), 2))
)

df_ad_perf = (
    spark.read.table('marketing_analytics_project.`02_silver`.fact_ad_performance')
    .groupBy('campaign_id', 'date')
    .agg(
        sum('impressions').alias('impressions'),
        sum('clicks').alias('clicks'),
        sum('spend_usd').alias('spend_usd')
    )
    .withColumn('spend_usd', round(col('spend_usd'), 2))
)

df_join = (
    df_ad_perf
    .join(df_conv, ['campaign_id', 'date'], 'full_outer')
    .fillna(0)
    .fillna('NA')
)

df_camp = spark.read.table('marketing_analytics_project.`02_silver`.dim_campaign')

df_final = (
    df_join
    .join(df_camp, 'campaign_id', 'left')
    .select("date", "campaign_id", "campaign_name", "channel", "impressions", "clicks", "spend_usd", "revenue_usd", "add_to_cart", "wishlist", "purchase", "total_no_of_conv")
    .orderBy('date', 'campaign_id')
)

display(df_final)

# COMMAND ----------

df_conv = (
    spark.read.table('marketing_analytics_project.`02_silver`.fact_conversions')
    .groupBy('customer_id')
    .agg(
        sum('revenue_usd').alias('revenue_usd'),
        sum('add_to_cart').alias('add_to_cart'),
        sum('wishlist').alias('wishlist'),
        sum('purchase').alias('purchase'),
        sum(col('add_to_cart') + col('wishlist') + col('purchase')).alias('total_no_of_conv')
    )
    .withColumn('revenue_usd', round(col('revenue_usd'), 2))
)

df_cust = spark.read.table('marketing_analytics_project.`02_silver`.dim_customer')

df_join = (
    df_conv
    .join(df_cust, 'customer_id', 'left')
    .withColumn('customer_tier', expr("CASE WHEN revenue_usd < 100 OR total_no_of_conv < 10 THEN 'Bronze' WHEN revenue_usd >= 500 OR total_no_of_conv >= 15 THEN 'Gold' ELSE 'Silver' END"))
    .select('customer_id', 'region', 'customer_tier', 'revenue_usd', "add_to_cart", "wishlist", "purchase", "total_no_of_conv")
    .orderBy('customer_id')
)

display(df_join)

# COMMAND ----------

