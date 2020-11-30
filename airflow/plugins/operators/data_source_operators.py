from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging


log = logging.getLogger(__name__)


class TwitterDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(TwitterDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('TwitterDataCollector Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class FBDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(FBDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('FBDataCollector Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class LinkedinDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(LinkedinDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('LinkedinDataCollector Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class SearchDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(SearchDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('SearchDataCollector Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"