from pyspark import pipelines as dp

# Step 1: Create the target streaming table for SCD Type 1
dp.create_streaming_table(
    name="02_silver.dim_campaign"
)

# Step 2: Define the Auto CDC flow from bronze to silver
dp.create_auto_cdc_flow(
    target="02_silver.dim_campaign",
    source="marketing_analytics_project.`01_bronze`.campaign",
    keys=["campaign_id"],
    sequence_by="start_date",
    stored_as_scd_type=1
)