from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import sys
sys.path.append('/opt/airflow/plugins/operators/')

from helper_utils.nlp_utils import analyze_tweets, analyze_news

import copy
import logging

log = logging.getLogger(__name__)


INSIGHTS_SCHEMA = {
    "source": "",
    "count": "",
    "sentiment": "",
    "keywords": [],
    "items": []
}


class TwitterAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        self.parent_task_id = parent_task_id

        super(TwitterAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('TwitterAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "Twitter"
        insights["count"] = len(value)

        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.append(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_tweets(value, insights, stop_words)

            except Exception as e:
                print(e)

        return insights


class LinkedinAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        self.parent_task_id = parent_task_id

        super(LinkedinAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('LinkedinAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        if value is not None:
            log.info(value)

        return "response"


class FBAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):
        self.data = data
        self.parent_task_id = parent_task_id

        super(FBAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('FBAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        if value is not None:
            log.info(value)

        return "response"


class WebAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):
        self.data = data
        self.parent_task_id = parent_task_id

        super(WebAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('WebAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        if value is not None:
            log.info(value)

        return "response"


class SearchAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        self.parent_task_id = parent_task_id

        super(SearchAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('SearchAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        if value is not None:
            log.info(value)

        return "response"


class YouTubeAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        self.parent_task_id = parent_task_id

        super(YouTubeAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('YouTubeAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        if value is not None:
            log.info(value)

        return "response"


class NewsAnalyzer(BaseOperator):

    @apply_defaults
    def __init__(self,
                 parent_task_id,
                 data,
                 *args,
                 **kwargs):
        self.data = data
        self.parent_task_id = parent_task_id

        super(NewsAnalyzer, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('NewsAnalyzer Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        value = context["task_instance"].xcom_pull(
            task_ids=self.parent_task_id)

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "News"

        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.append(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_news(value, insights, stop_words)

            except Exception as e:
                print(e)

        return insights