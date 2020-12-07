from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import sys
sys.path.append('/opt/airflow/plugins/operators/')

from helper_utils.nlp_utils import analyze_tweets, analyze_news, analyze_videos
from helper_utils.data_write_utils import write_data

import copy
import logging
import json
import requests

log = logging.getLogger(__name__)


INSIGHTS_SCHEMA = {
    "source": "",
    "count": 0,
    "sentiment": {"positive": 0, "negative": 0, "neutral": 0},
    "keywords": {},
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

        value = get_content('/opt/airflow/data/'+str(self.data["id"])+'/source/twitter.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "twitter"

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
                write_data(insights, self.data["id"], "insights", "twitter")
                update_backend(self.data["id"], "twitter", insights)
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

        value = get_content('/opt/airflow/data/' + str(self.data["id"]) + '/source/linkedin.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "linkedin"

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
                write_data(insights, self.data["id"], "insights", "linkedin")
                update_backend(self.data["id"], "linkedin", insights)
        return ""


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

        value = get_content('/opt/airflow/data/' + str(self.data["id"]) + '/source/website.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "website"
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
                write_data(insights, self.data["id"], "insights", "website")
                update_backend(self.data["id"], "website", insights)

        return ""


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

        value = get_content('/opt/airflow/data/' + str(self.data["id"]) + '/source/youtube.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "youtube"
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
                write_data(insights, self.data["id"], "insights", "youtube")
                update_backend(self.data["id"], "youtube", insights)

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

        value = get_content('/opt/airflow/data/' + str(self.data["id"]) + '/source/news.json')

        insights = copy.deepcopy(INSIGHTS_SCHEMA)

        insights["source"] = "news"

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
                write_data(insights, self.data["id"], "insights", "news")
                update_backend(self.data["id"], "news", insights)

        return ""


class InsightsAggregator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):
        self.data = data

        super(InsightsAggregator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('InsightsAggregator Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        insights = copy.deepcopy(INSIGHTS_SCHEMA)
        insights["source"] = "aggregated"

        data_sources = self.data["dataSources"].split(",")

        count = 0

        sentiment = {
            "positive":0,
            "negative":0,
            "neutral":0
        }

        keywords = {}

        for data_source in data_sources:

            value = get_content('/opt/airflow/data/{}/insights/{}.json'.format(str(self.data["id"]), data_source))

            count += value.get("count",0)

            sentiment["positive"] += value.get("sentiment",0).get("positive",0)
            sentiment["negative"] += value.get("sentiment", 0).get("negative", 0)
            sentiment["neutral"] += value.get("sentiment", 0).get("neutral", 0)

            for key in value.get("keywords",[]).keys():
                if keywords.get(key) is None:
                    keywords[key] = value.get("keywords").get(key)

                else:
                    keywords[key] += value.get("keywords").get(key)

        insights["count"] = count
        insights["keywords"] = keywords
        insights["sentiment"] = sentiment
        insights["items"] = []

        update_backend(self.data["id"], "aggregated", insights)

        return ""


def update_backend(id, source, insights):

    post_body = {"jobId": id, "source": source, "jsonText": json.dumps(insights)}
    r = requests.post('http://backend:8081/job/insights', json=post_body)
    print(r.status_code)