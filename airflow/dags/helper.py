from airflow.operators.dummy_operator import DummyOperator

from operators.data_source_operators import TwitterDataCollector, \
    LinkedinDataCollector, WebDataCollector, NewsDataCollector, YouTubeDataCollector

from operators.data_science_operators import TwitterAnalyzer, \
    LinkedinAnalyzer, WebAnalyzer, NewsAnalyzer, YouTubeAnalyzer, InsightsAggregator

from airflow.operators.python_operator import PythonOperator

import os
import requests
import json


data_source_operator_map = {
    "twitter": TwitterDataCollector,
    "linkedin": LinkedinDataCollector,
    "website": WebDataCollector,
    "news": NewsDataCollector,
    "youtube": YouTubeDataCollector
}


data_analyzer_operator_map = {
    "twitter": TwitterAnalyzer,
    "linkedin": LinkedinAnalyzer,
    "website": WebAnalyzer,
    "news": NewsAnalyzer,
    "youtube": YouTubeAnalyzer
}


INSIGHTS_SCHEMA = {
    "source": "",
    "count": "",
    "sentiment": "",
    "keywords": [],
    "items": []
}


def construct_dag(task, dag):

    data_source_operators = []

    end_flow = DummyOperator(
        task_id="end_flow",
        retries=3,
        dag=dag)

    update_status = PythonOperator(task_id='update_status',
                                            python_callable=update_task_status, op_kwargs={'id': task["id"], 'status': 3})

    insights_aggregator = InsightsAggregator(
                    task_id="insights_aggregation" + str(task["id"]),
                    data=task,
                    retries=3,
                    dag=dag)

    data_sources = task["dataSources"].split(",")

    print(data_sources)

    for data_source in data_sources:

        source_operator = data_source_operator_map.get(data_source)

        if source_operator is not None:
            source_operator_instance = source_operator(
                                    task_id=data_source + "_data_fetcher_" + str(task["id"]),
                                    data=task,
                                    retries=3,
                                    dag=dag)

            analyzer_operator = data_analyzer_operator_map.get(data_source)

            if analyzer_operator is not None:
                analyzer_operator_instance = analyzer_operator(
                    task_id=data_source + "_analyzer_" + str(task["id"]),
                    parent_task_id=data_source + "_data_fetcher_" + str(task["id"]),
                    data=task,
                    retries=3,
                    dag=dag)

                # analytics_operator_instances = construct_analytics_operators(data_source, dag)

                source_operator_instance >> analyzer_operator_instance >> insights_aggregator >> update_status >> end_flow

            data_source_operators.append(source_operator_instance)

    return data_source_operators


# def construct_analytics_operators(data_source, dag):
#
#     data_analytics_operator_instances = []
#
#     for analytics_module in data_analytics_operators.keys():
#
#         operator = data_analytics_operators.get(analytics_module)
#
#         operator_instance = operator(task_id=data_source + "_"+ analytics_module,
#                                     data="some_value",
#                                     retries=3,
#                                     dag=dag)
#
#         data_analytics_operator_instances.append(operator_instance)
#
#     return data_analytics_operator_instances


def create_repos(**kwargs):

    task = kwargs["task"]

    if not os.path.exists('/opt/airflow/data/'+str(task["id"])):
        os.makedirs('/opt/airflow/data/'+str(task["id"]))

    if not os.path.exists('/opt/airflow/data/'+str(task["id"])+'/source'):
        os.makedirs('/opt/airflow/data/'+str(task["id"])+'/source')

    if not os.path.exists('/opt/airflow/data/'+str(task["id"])+'/insights'):
        os.makedirs('/opt/airflow/data/'+str(task["id"])+'/insights')


def fetch_tasks():

    r = requests.get('http://backend:8081/job/status/1')

    if r.status_code == 200:
        tasks = json.loads(r.text)
        print(tasks)

        return tasks

    return []


def update_task_status(**kwargs):

    id = kwargs["id"]
    status = kwargs["status"]

    url = 'http://backend:8081/job/{}/status/{}'.format(id,status)
    print(url)
    response = requests.put(url)
    print(response.status_code)