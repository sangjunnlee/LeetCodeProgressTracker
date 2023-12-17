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
GROKKING_URL = "https://www.designgurus.io/course/grokking-the-coding-interview"

def get_grokking_info():
    response = requests.get(GROKKING_URL)
    print(response)


def main():
    get_grokking_info()
    return None

if __name__ == '__main__':
    main()