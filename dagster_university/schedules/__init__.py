import dagster


class WeekUpdateConfig(dagster.Config):
    date: str


@dagster.op(
    name="week_update_op",
)
def week_update_op(
    context: dagster.OpExecutionContext, config: WeekUpdateConfig
) -> None:
    """Check if output file exists in s3."""
    context.log.info(f"Date: {config.date}")


@dagster.job(
    config={
        "ops": {
            "week_update_op": {
                "config": WeekUpdateConfig(
                    date="20230604",
                ).model_dump()
            }
        }
    },
)
def week_update_job() -> None:
    """Dagster job to trigger coop_deli_check_output_file_op."""
    week_update_op()


@dagster.schedule(
    job=week_update_job,
    cron_schedule="*/2 * * * *",  # 16:30pm every Friday
)
def week_update_schedule(
    context: dagster.ScheduleEvaluationContext,
) -> dagster.RunRequest:
    """Schedule to create job sequence."""
    output_date = context.scheduled_execution_time.strftime("%Y%m%d")
    return dagster.RunRequest(
        run_key=None,
        run_config={
            "ops": {
                "week_update_op": {
                    "config": WeekUpdateConfig(
                        date=output_date,
                    ).model_dump()
                },
            },
        },
    )
