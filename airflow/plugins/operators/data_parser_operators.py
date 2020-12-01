from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging

log = logging.getLogger(__name__)


class TwitterDataParser(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(TwitterDataParser, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('TwitterDataParser Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class LinkedinDataParser(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(LinkedinDataParser, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('LinkedinDataParser Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"



class FBDataParser(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(FBDataParser, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('FBDataParser Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class WebDataParser(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(WebDataParser, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('WebDataParser Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class SearchDataParser(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(SearchDataParser, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('SearchDataParser Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"


class NewsDataParser(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(NewsDataParser, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('NewsDataParser Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        return "response"