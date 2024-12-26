# fmt: off
from dagster import Definitions, load_assets_from_modules, sensor

from .assets import metrics, trips, requests
from .resources import database_resource
from .jobs import trip_update_job, adhoc_request_job
from .schedules import week_update_schedule, week_update_job
from .sensors import adhoc_request_sensor

trip_assets = load_assets_from_modules([trips])
metric_assets = load_assets_from_modules([metrics])
request_assets = load_assets_from_modules([requests])

all_jobs = [trip_update_job, adhoc_request_job, week_update_job]
all_schedules = [week_update_schedule]
all_sensors = [adhoc_request_sensor]


defs = Definitions(
    assets=[*trip_assets, *metric_assets, *request_assets],
    resources={
        "database": database_resource,
    },
    jobs=all_jobs,
    schedules=all_schedules,
    sensors=all_sensors,
)
