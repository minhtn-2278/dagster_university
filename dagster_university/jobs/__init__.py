from dagster import AssetSelection, define_asset_job
from ..partitions import monthly_partition, weekly_partition

trip_update_job = define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partition,
    selection=AssetSelection.assets("taxi_trips_file", "taxi_zones_file", "taxi_trips", "taxi_zones")
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    partitions_def=weekly_partition,
    selection=AssetSelection.assets("trips_by_week_answer", "trips_by_week_practice"),
)
