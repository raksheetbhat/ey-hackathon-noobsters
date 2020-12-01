from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators.data_aggregation_operators import DataAggregator

from datetime import datetime
import requests

import helper

output = [{

        "task_id": 3,
        "task_name": "EY tasks ",
        "data_sources": ["twitter","facebook","linkedin", "search"],
        "goal": "goal_1",
},
{
        "task_id": 4,
        "task_name": "EY tasks for something",
        "data_sources": ["linkedin", "search"],
        "goal": "goal_2",
}]


def create_dag(task):

    dag = DAG(
            task["task_name"].replace(" ","_")+"_"+str(task["task_id"]),
            is_paused_upon_creation=False,
            description=task["task_name"],
            schedule_interval='@once',
            start_date=datetime(2020, 11, 26),
            catchup=False)

    initiate_operator = DummyOperator(
                            task_id="begin_flow",
                            retries=3,
                            dag=dag)

    operators = helper.construct_dag(task, dag)

    initiate_operator >> operators

    return dag


# Get request from server
for task in output:
    dag_id = str(task["task_id"])
    globals()[dag_id] = create_dag(task)

    # update server that task is in progress

# search optimization
    # keywords recommendation

# # Data source
# Facebook
# Twitter
# Youtube
# Google search results
# News
# Stock
# competitor publications
# Disqus?
# Linkedin


# # Goal values
# search ranking
# keywords trending
# topics trending
# sentiment analysis