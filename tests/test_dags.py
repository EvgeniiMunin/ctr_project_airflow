import os
import sys
import pytest
from airflow.models import DagBag

sys.path.append("dags")


@pytest.fixture()
def dag_bag():
    os.environ["DATA_VOLUME_PATH"] = "/tmp"
    return DagBag(dag_folder="dags/", include_examples=False)


def test_train_val_imports(dag_bag):
    assert dag_bag.dags is not None
    assert "airflow_download_data_from_s3" in dag_bag.dags
    assert "airflow_train_val" in dag_bag.dags


def test_train_val_dag(dag_bag):
    dag = dag_bag.dags["airflow_train_val"]

    dag_flow = {
        "wait-for-data": ["preprocess"],
        "preprocess": ["split"],
        "split": ["train"],
        "train": ["notify"],
        "notify": []
    }

    for name, task in dag.task_dict.items():
        assert task.downstream_task_ids == set(dag_flow[name])