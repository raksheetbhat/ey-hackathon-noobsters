from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime
import requests

import helper

output = [{

        "task_id" : 1,
        "task_name" : "EY task",
        "data_sources": ["twitter","facebook","linkedin", "search"],
        "goal": "goal_1",
},
{

        "task_id" : 2,
        "task_name" : "EY task for something",
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

    data_sources = helper.data_source_translator(task["data_sources"], task["task_id"], dag)

    goal_operator = DummyOperator(
        task_id=task["goal"],
        retries=3,
        dag=dag)

    end_operator = DummyOperator(
        task_id="end_flow",
        retries=3,
        dag=dag)

    initiate_operator >> data_sources >> goal_operator >> end_operator

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
