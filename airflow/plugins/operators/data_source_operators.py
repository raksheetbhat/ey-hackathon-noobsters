from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging

import sys

sys.path.append('/opt/airflow/plugins/operators/')

from helper_utils.news_source_utils import get_news_articles
from helper_utils.twitter_utils import get_tweets
from helper_utils.data_write_utils import write_data
from helper_utils.search_utils import get_custom_search_results, get_linkedin_results
from helper_utils.youtube_source_utils import get_youtube_videos

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

        keyword = ""

        company_name = ""
        domain = self.data.get("domain")

        if company_name is not None and company_name != "":
            keyword += company_name + " "

            if domain is not None and domain != "":
                keyword += domain

        else:
            keyword += domain

        output = get_tweets(keyword, "")

        if output is not None:
            write_data(output, self.data["id"], "source", "twitter")

        log.info(output)
        return ""


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

        keyword = ""

        company_name = self.data.get("companyName")
        domain = self.data.get("domain")

        if company_name is not None and company_name != "":
            keyword += company_name + " "

            if domain is not None and domain != "":
                keyword += domain

        else:
            keyword += domain

        output = get_linkedin_results(keyword)

        if output is not None:
            write_data(output, self.data["id"],"source", "linkedin")

        log.info(output)
        return ""


class WebDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(WebDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('WebDataCollector Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        if self.data["domain"] is "":
            domain = "latest"
        else:
            domain = self.data["domain"]

        output = get_custom_search_results(self.data["companyName"], domain)

        if output is not None:
            write_data(output, self.data["id"], "source", "website")

        log.info(output)
        return ""


class YouTubeDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(YouTubeDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('YouTubeDataCollector Initiated')
        log.info("Some process happens here")
        log.info(self.data)

        keyword = ""

        company_name = self.data.get("companyName")
        domain = self.data.get("domain")

        if company_name is not None and company_name != "":
            keyword += company_name + " "

            if domain is not None and domain != "":
                keyword += domain

        else:
            keyword += domain

        output = get_youtube_videos(keyword)

        if output is not None:
            write_data(output, self.data["id"], "source", "youtube")

        log.info(output)

        return ""


class NewsDataCollector(BaseOperator):

    @apply_defaults
    def __init__(self,
                 data,
                 *args,
                 **kwargs):

        self.data = data
        super(NewsDataCollector, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('NewsDataCollector Initiated')

        log.info(self.data)

        keyword = ""

        company_name = self.data.get("companyName")
        domain = self.data.get("domain")

        if company_name is not None and company_name != "":
            keyword += company_name + " "

            if domain is not None and domain != "":
                keyword += domain

        else:
            keyword += domain

        output = get_news_articles(keyword)

        if output is not None:
            write_data(output, self.data["id"],"source", "news")

        log.info(output)
        return ""