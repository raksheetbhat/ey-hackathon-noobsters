from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

import helper

# output = [
#     {
#         "id": 3,
#         "version": 0,
#         "created": "2020-12-06T18:14:51",
#         "jobName": "BCG blochchain Job",
#         "startDate": "2020-12-31T00:00:00",
#         "endDate": "2021-01-09T00:00:00",
#         "goal": "1",
#         "dataSources": ["twitter","news","linkedin"],
#         "domain": "Blockchain",
#         "companyName": "BCG",
#         "companyUrl": "",
#         "status": 1
#     }
# ]


def create_dag(task):

    dag = DAG(
            str(task["jobName"]).replace(" ", "_") + "_" + str(task["id"]),
            is_paused_upon_creation=False,
            description=task["jobName"],
            schedule_interval='@once',
            start_date=datetime(2020, 12, 1),
            catchup=False)

    initiate_operator = DummyOperator(
                            task_id="begin_flow",
                            retries=3,
                            dag=dag)

    create_data_repository = PythonOperator(task_id='initialize_repositories',
                                            python_callable=helper.create_repos, op_kwargs={'task': task})

    operators = helper.construct_dag(task, dag)

    initiate_operator >> create_data_repository >> operators

    return dag


output = helper.fetch_tasks()

# Get request from server
for task in output:
    dag_id = str(task["jobName"]).replace(" ","_") + str(task["id"])
    globals()[dag_id] = create_dag(task)

    # helper.update_task_status(task["id"],2)

