from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging

log = logging.getLogger(__name__)


class DataAggregator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(DataAggregator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('DataAggregator Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class InsightsPersistor(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(InsightsPersistor, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('InsightsPersistor Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"