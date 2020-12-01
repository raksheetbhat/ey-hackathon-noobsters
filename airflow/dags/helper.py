from airflow.operators.dummy_operator import DummyOperator

from operators.data_source_operators \
    import TwitterDataCollector, FBDataCollector, LinkedinDataCollector, SearchDataCollector

from operators.data_aggregation_operators import DataAggregator, InsightsPersistor


data_source_operator_map = {
    "facebook" : FBDataCollector,
    "twitter" : TwitterDataCollector,
    "search" : SearchDataCollector,
    "linkedin" : LinkedinDataCollector
}


def construct_dag(task, dag):

    data_source_operators = []

    goal_operator = DummyOperator(
        task_id=task["goal"],
        retries=3,
        dag=dag)

    insights_persistor = InsightsPersistor(
                                    task_id="Insights_Persistor_" + str(task["task_id"]),
                                    data="some_value",
                                    retries=3,
                                    dag=dag)

    end_operator = DummyOperator(
        task_id="end_flow",
        retries=3,
        dag=dag)


    for data_source in task["data_sources"]:
        operator = data_source_operator_map.get(data_source)

        if operator is not None:

            operator_instance = operator(
                                    task_id=data_source + "_" + str(task["task_id"]),
                                    data="some_value",
                                    retries=3,
                                    dag=dag)

            data_aggregator = DataAggregator(
                                    task_id=data_source + "_aggregator_" + str(task["task_id"]),
                                    data="some_value",
                                    retries=3,
                                    dag=dag)

            operator_instance >> data_aggregator >> goal_operator >> insights_persistor >> end_operator

            data_source_operators.append(operator_instance)

    return data_source_operators


def goal_translator(data_sources, dag):

    data_source_operators = []

    for data_source in data_sources:
        operator = data_source_operator_map.get(data_source)

        if operator is not None:
            operator_instance = operator(
                task_id="twitter_collector",
                data="some_value",
                retries=3,
                dag=dag)

            data_source_operators.append(operator_instance)

    return data_source_operators




