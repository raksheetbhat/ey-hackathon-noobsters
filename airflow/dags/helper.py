
from operators.data_source_operators \
    import TwitterDataCollector, FBDataCollector, LinkedinDataCollector, SearchDataCollector


data_source_operator_map = {
    "facebook" : FBDataCollector,
    "twitter" : TwitterDataCollector,
    "search" : SearchDataCollector,
    "linkedin" : LinkedinDataCollector
}


def data_source_translator(data_sources, task_id, dag):

    data_source_operators = []

    for data_source in data_sources:
        operator = data_source_operator_map.get(data_source)

        if operator is not None:

            operator_instance = operator(
                                    task_id=data_source + "_" + str(task_id),
                                    data="some_value",
                                    retries=3,
                                    dag=dag)


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




