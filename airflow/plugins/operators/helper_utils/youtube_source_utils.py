from youtubesearchpython import SearchVideos
from youtube_transcript_api import YouTubeTranscriptApi

import copy
import json

YOUTUBE_SCHEMA = {
    "id": "",
    "link": "",
    "title": "",
    "channel": "",
    "duration": "",
    "views": "",
    "published": "",
    "transcript": ""
}


def get_youtube_videos(keyword):

    print("Fetching videos for : " + keyword)
    output = []

    try:
        search = SearchVideos(keyword, offset=1, mode="json", max_results=10)
        raw_results = search.result()
        results = json.loads(raw_results)
        # print(results)

    except Exception as e:
        print(e)
        return []

    print("Fetched videos")

    if results.get("search_result") is not None:

        for result in results["search_result"]:
            video = copy.deepcopy(YOUTUBE_SCHEMA)
            try:

                print("Processing : " + str(result["id"]))

                transcript = get_transcript(result["id"])

                video["id"] = result["id"]
                video["link"] = result["link"]
                video["title"] = result["title"]
                video["channel"] = result["channel"]
                video["duration"] = result["duration"]
                video["views"] = result["views"]
                video["published"] = result["publishTime"]
                video["transcript"] = transcript

                output.append(video)

            except Exception as e:
                print(e)
                continue

    return output


def get_transcript(video_id):
    output = ""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        for video_slice in transcript:
            output += " " + video_slice["text"]

    except Exception as e:
        print(e)
        return None

    return output


# get_transcript('wwjzxHI92Eg')
#

# print(get_youtube_videos("latest supply chain"))
