from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

import helper

output = [{

        "job_id": 1,
        "job_name": "BCG Analysis",
        "start_date": "2020-11-25",
        "end_date": "",
        "goal": "competitive_analysis",
        "data_sources": ["twitter","website","news","youtube"],
        "domain": "supply chain",
        "company_name": "BCG",
        "company_url": "www.bcg.com",
        "status": "submitted"
    }, {
        "job_id": 2,
        "job_name": "Trends in Supply chain",
        "start_date": "2020-11-25",
        "end_date": "",
        "goal": "emerging_trends",
        "data_sources": ["twitter","search","news","youtube"],
        "domain": "Blockchain",
        "status": "submitted"
    }
]


def create_dag(task):

    dag = DAG(
            str(task["job_name"]).replace(" ", "_") + "_" +str(task["job_id"]),
            is_paused_upon_creation=False,
            description=task["job_name"],
            schedule_interval='@once',
            start_date=datetime(2020, 12, 1),
            catchup=False)

    initiate_operator = DummyOperator(
                            task_id="begin_flow",
                            retries=3,
                            dag=dag)

    create_data_repository = PythonOperator(task_id='python_task',
                                            python_callable=helper.create_repos, op_kwargs={'task': task})

    operators = helper.construct_dag(task, dag)

    initiate_operator >> create_data_repository >> operators

    return dag


# Get request from server
for task in output:
    dag_id = str(task["job_name"]).replace(" ","_") + str(task["job_id"])
    globals()[dag_id] = create_dag(task)

    # update server that task is in progress
