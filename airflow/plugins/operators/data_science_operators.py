from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import sys
sys.path.append('/opt/airflow/plugins/operators/')

from helper_utils.nlp_utils import analyze_tweets, analyze_news, analyze_videos
from helper_utils.data_write_utils import write_data

import copy
import logging
import json

log = logging.getLogger(__name__)


INSIGHTS_SCHEMA = {
    "source": "",
    "count": "",
    "sentiment": "",
    "keywords": [],
    "items": []
}


def get_content(path):

    with open(path,"r") as file:
        file_json = file.read()

    if file_json is not None or file_json != "":
        return json.loads(file_json)

    return []


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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/'+str(self.data["job_id"])+'/source/twitter.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "Twitter"
        insights["count"] = len(value)

        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.extend(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_tweets(value, insights, stop_words)

            except Exception as e:
                print(e)

            if insights is not None:
                write_data(insights, self.data["job_id"], "insights", "twitter")

        return ""


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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/' + str(self.data["job_id"]) + '/source/linkedin.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "Linkedin"

        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.extend(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_news(value, insights, stop_words)

            except Exception as e:
                print(e)

            if insights is not None:
                write_data(insights, self.data["job_id"], "insights", "linkedin")

        return ""


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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/' + str(self.data["job_id"]) + '/source/fb.json')

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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/' + str(self.data["job_id"]) + '/source/website.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "Website"
        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.extend(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_news(value, insights, stop_words)

            except Exception as e:
                print(e)

            if insights is not None:
                write_data(insights, self.data["job_id"], "insights", "website")

        return ""


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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/' + str(self.data["job_id"]) + '/source/search.json')

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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/' + str(self.data["job_id"]) + '/source/youtube.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "YouTube"
        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.extend(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_videos(value, insights, stop_words)

            except Exception as e:
                print(e)

            if insights is not None:
                write_data(insights, self.data["job_id"], "insights", "youtube")

        return ""


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

        # value = context["task_instance"].xcom_pull(
        #     task_ids=self.parent_task_id)

        value = get_content('/opt/airflow/data/' + str(self.data["job_id"]) + '/source/news.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "News"

        stop_words = []

        domain = self.data["domain"]

        if domain is not None or domain != "":
            stop_words.extend(domain.lower().split(" "))

        if value is not None:
            log.info(value)

            try:
                insights = analyze_news(value, insights, stop_words)

            except Exception as e:
                print(e)

            if insights is not None:
                write_data(insights, self.data["job_id"], "insights", "news")

        return ""