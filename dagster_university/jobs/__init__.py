from dagster import AssetSelection, define_asset_job

trip_update_job = define_asset_job(
    name="trip_update_job",
    selection=AssetSelection.assets("taxi_trips_file", "taxi_zones_file", "taxi_trips", "taxi_zones")
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    selection=AssetSelection.assets("trips_by_week_answer", "trips_by_week_practice"),
)
