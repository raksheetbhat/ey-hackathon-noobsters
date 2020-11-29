from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

from operators.data_source_operators import TwitterDataCollector

from datetime import datetime, timedelta


# REst end point for fetching metadata
# {}


dag = DAG('first_flow',
                        description='Dynamically load, transform, analyse, persist and predict trends',
                        schedule_interval='0 12 * * *',
                        start_date=datetime(2020, 11, 26),
                        catchup=False)

# if else

initiate_operator = DummyOperator(
                        task_id="flow_begin",
                        retries=3,
                        dag=dag)


source = TwitterDataCollector(task_id="twitter_collector",
                          data="some_value",
                        retries=3,
                        dag=dag)

source1 = TwitterDataCollector(task_id="twitter_collector1",
                          data="some_value1",
                        retries=3,
                        dag=dag)


end_operator = DummyOperator(
                        task_id="flow_end",
                        retries=3,
                        dag=dag)


initiate_operator >> [source, source1] >> end_operator