import requests
import json
import argparse
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import sys
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABSE_ID")

NOTION_BASE_URL = "https://api.notion.com/"
GROKKING_URL = "https://www.designgurus.io/api/course/getLessonsList/grokking-the-coding-interview"

def get_topic_and_lessons():
    try:
        response = requests.get(GROKKING_URL)
        response = response.json()
        if "code" in response:
            if response["code"] != 200:
                raise RequestException(response["message"])
            response.raise_for_status()

        topics = response['data']

        topic_to_lesson_map = {}

        for topic in topics:
            title = topic['title']
            lesson_titles = [doc['documentTitle'] for doc in topic['documents']]
            topic_to_lesson_map[title] = lesson_titles

        return topic_to_lesson_map      

    except HTTPError as errh:
        sys.exit(errh)
    except ConnectionError as errc:
        sys.exit(errc)
    except Timeout as errt:
        sys.exit(errt)
    except RequestException as err:
        sys.exit(err)

def get_topics():
    response = requests.get(GROKKING_URL)
    response = response.json()
    topics = []

    for topic in response['data']:
        topics.append(topic['title'])
    return topics


def main():
    print(get_topics())
    return get_topic_and_lessons()

if __name__ == '__main__':
    main()