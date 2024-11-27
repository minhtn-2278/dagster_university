from dagster import ScheduleDefinition
from ..jobs import trip_update_job, weekly_update_job

# cron syntaz: min hour dayOfMonth month dayOfWeek
trip_update_schedule = ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *"
)

week_update_schedule = ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1"
)
