from dagster import AssetSelection, define_asset_job
from ..partitions import monthly_partition

trip_update_job = define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partition,
    selection=AssetSelection.assets("taxi_trips_file", "taxi_zones_file", "taxi_trips", "taxi_zones")
)

adhoc_request = AssetSelection.assets(["adhoc_request"])

adhoc_request_job = define_asset_job(
    name="adhoc_request_job",
    selection=adhoc_request,
)
