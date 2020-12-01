from airflow.operators.dummy_operator import DummyOperator

from operators.data_source_operators \
    import TwitterDataCollector, FBDataCollector, LinkedinDataCollector, SearchDataCollector, WebDataCollector

from operators.data_parser_operators \
    import TwitterDataParser, FBDataParser, LinkedinDataParser, SearchDataParser, WebDataParser

from operators.data_science_operators \
    import SentimentAnalyzer, KeywordAnalyzer


data_source_operator_map = {
    "facebook": FBDataCollector,
    "twitter": TwitterDataCollector,
    "search": SearchDataCollector,
    "linkedin": LinkedinDataCollector,
    "website": WebDataCollector
}

data_parser_operator_map = {
    "facebook": FBDataParser,
    "twitter": TwitterDataParser,
    "search": SearchDataParser,
    "linkedin": LinkedinDataParser,
    "website": WebDataParser
}

data_analytics_operators = {
    "sentiment": SentimentAnalyzer,
    "keyword": KeywordAnalyzer
}


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
                                    task_id=data_source + "_source_" + str(task["job_id"]),
                                    data="some_value",
                                    retries=3,
                                    dag=dag)

            parser_operator = data_parser_operator_map.get(data_source)

            if parser_operator is not None:
                parser_operator_instance = parser_operator(
                    task_id=data_source + "_parser_" + str(task["job_id"]),
                    data="some_value",
                    retries=3,
                    dag=dag)

                analytics_operator_instances = construct_analytics_operators(data_source, dag)

                source_operator_instance >> parser_operator_instance >> analytics_operator_instances >> insights_aggregator >> end_operator


            data_source_operators.append(source_operator_instance)

    return data_source_operators


def construct_analytics_operators(data_source, dag):

    data_analytics_operator_instances = []

    for analytics_module in data_analytics_operators.keys():

        operator = data_analytics_operators.get(analytics_module)

        operator_instance = operator(task_id=data_source + "_"+ analytics_module,
                                    data="some_value",
                                    retries=3,
                                    dag=dag)

        data_analytics_operator_instances.append(operator_instance)

    return data_analytics_operator_instances




