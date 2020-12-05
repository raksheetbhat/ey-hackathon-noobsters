from airflow.operators.dummy_operator import DummyOperator

from operators.data_source_operators import TwitterDataCollector, FBDataCollector, \
    LinkedinDataCollector, SearchDataCollector, WebDataCollector, NewsDataCollector, YouTubeDataCollector

from operators.data_science_operators import TwitterAnalyzer, FBAnalyzer, \
    LinkedinAnalyzer, SearchAnalyzer, WebAnalyzer, NewsAnalyzer, YouTubeAnalyzer


import os
import requests
import json


data_source_operator_map = {
    "facebook": FBDataCollector,
    "twitter": TwitterDataCollector,
    "search": SearchDataCollector,
    "linkedin": LinkedinDataCollector,
    "website": WebDataCollector,
    "news": NewsDataCollector,
    "youtube": YouTubeDataCollector
}


data_analyzer_operator_map = {
    "facebook": FBAnalyzer,
    "twitter": TwitterAnalyzer,
    "search": SearchAnalyzer,
    "linkedin": LinkedinAnalyzer,
    "website": WebAnalyzer,
    "news": NewsAnalyzer,
    "youtube": YouTubeAnalyzer
}


# data_analytics_operators = {
#     "sentiment": SentimentAnalyzer,
#     "keyword": KeywordAnalyzer
# }


def construct_dag(task, dag):

    data_source_operators = []

    insights_aggregator = DummyOperator(
        task_id="insights_aggregator",
        retries=3,
        dag=dag)

    end_operator = DummyOperator(
        task_id="end_flow",
        retries=3,
        dag=dag)

    for data_source in task["data_sources"]:

        source_operator = data_source_operator_map.get(data_source)

        if source_operator is not None:
            source_operator_instance = source_operator(
                                    task_id=data_source + "_data_fetcher_" + str(task["job_id"]),
                                    data=task,
                                    retries=3,
                                    dag=dag)

            analyzer_operator = data_analyzer_operator_map.get(data_source)

            if analyzer_operator is not None:
                analyzer_operator_instance = analyzer_operator(
                    task_id=data_source + "_analyzer_" + str(task["job_id"]),
                    parent_task_id=data_source + "_data_fetcher_" + str(task["job_id"]),
                    data="some_value",
                    retries=3,
                    dag=dag)

                # analytics_operator_instances = construct_analytics_operators(data_source, dag)

                source_operator_instance >> analyzer_operator_instance >> insights_aggregator >> end_operator

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

    if not os.path.exists('/opt/airflow/data/'+str(task["job_id"])):
        os.makedirs('/opt/airflow/data/'+str(task["job_id"]))

    if not os.path.exists('/opt/airflow/data/'+str(task["job_id"])+'/source'):
        os.makedirs('/opt/airflow/data/'+str(task["job_id"])+'/source')

    if not os.path.exists('/opt/airflow/data/'+str(task["job_id"])+'/insights'):
        os.makedirs('/opt/airflow/data/'+str(task["job_id"])+'/insights')


def fetch_tasks():
    r = requests.get('http://ey_hack_backend-service_1:5000/fetch_new_tasks')

    if r.status_code == 200:
        tasks = json.loads(r.text)

        return tasks

    return []
