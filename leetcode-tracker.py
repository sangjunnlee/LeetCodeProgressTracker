import requests
import json
import argparse
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import sys
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

NOTION_BASE_URL = "https://api.notion.com/"
LEETCODE_INFO_URL = "https://lcid.cc/info/"
LEETCODE_URL = "https://leetcode.com/problems/"

urlDatabase = f"{NOTION_BASE_URL}v1/databases/{DATABASE_ID}"
urlQueryPages = f"{NOTION_BASE_URL}v1/database/{DATABASE_ID}/query"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_leetcode_info_by_id(id):
    try:
        leetcode_url = f"{LEETCODE_INFO_URL}{id}"
        resInfo = requests.get(leetcode_url, timeout=3)
        resInfo = resInfo.json()
        if "code" in resInfo:
            if resInfo["code"] != 200:
                raise RequestException(resInfo["message"])
            resInfo.raise_for_status()
        return resInfo
    except HTTPError as errh:
        sys.exit(errh)
    except ConnectionError as errc:
        sys.exit(errc)
    except Timeout as errt:
        sys.exit(errt)
    except RequestException as err:
        sys.exit(err)

def update_page(page_id: str, data:dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    return res

def main():
    parser = argparse.ArgumentParser(
        description = "Generate leetcode question to fill up Notion for tracking of questions")
    parser.add_argument("leetcode_number", type=int, help="leetcode question number")
    parser.add_argument(
        "comment", nargs="?", default="", help="optional comment for the question"
    )
    args = parser.parse_args()

    leetcode_number_input_by_user = args.leetcode_number
    leetcode_comment_input_by_user = args.comment

    leet_code = get_leetcode_info_by_id(leetcode_number_input_by_user)

    print(leet_code)

