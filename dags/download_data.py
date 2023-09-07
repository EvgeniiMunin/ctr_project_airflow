import os

import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount


with DAG(
    dag_id="airflow_download_data_from_s3",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
) as dag:

    get_data = DockerOperator(
        image="download",
        command="--output-dir data/raw/{{ ds }",
        task_id="download",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=f"{os.environ['DATA_VOLUME_PATH']}data",
                target="/output",
                type="bind",
            )
        ],
    )

    notify = BashOperator(
        task_id="notify", bash_command=f"echo new rows of data generated ...",
    )

    get_data >> notify
