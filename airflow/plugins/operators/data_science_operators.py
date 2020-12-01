from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging


log = logging.getLogger(__name__)


class SentimentAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(SentimentAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('SentimentAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class KeywordAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(KeywordAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('KeywordAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"