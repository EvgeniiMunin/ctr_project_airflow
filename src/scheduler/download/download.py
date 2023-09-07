import logging
import sys

import click
from data.s3_storage import download_file

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@click.command("download")
@click.option("--s3-bucket")
@click.option("--remote-path")
@click.option("--output-path")
def download_dataset():
    s3_bucket = "sem5-airflow"
    remote_path = "remote_tests/sampled_train_50k.csv"
    output_local_path = "data/sampled_train_50k.csv"

    download_file(
        bucket_name=s3_bucket, remote_path=remote_path, local_path=output_local_path,
    )


if __name__ == "__main__":
    download_dataset()
