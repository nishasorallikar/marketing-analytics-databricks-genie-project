from pyspark import pipelines as dp

# Step 1: Create the target streaming table for SCD Type 1
dp.create_streaming_table(
    name="02_silver.dim_customer"
)

# Step 2: Define the Auto CDC flow from bronze to silver
dp.create_auto_cdc_flow(
    target="02_silver.dim_customer",
    source="marketing_analytics_project.`01_bronze`.customer",
    keys=["customer_id"],
    sequence_by="customer_id",
    stored_as_scd_type=1
)