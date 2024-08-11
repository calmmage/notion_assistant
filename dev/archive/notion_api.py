"""
Attempt at raw replication of Notion API as is
Without fancy features and extensions, e.g. autocompletion
"""

from enum import Enum
import requests
import json


class RequestType(Enum):
    post = "POST"
    get = "GET"


class ApiHandle(Enum):
    database = "databases"


def send_notion_request(request_type: RequestType, api_handle: ApiHandle, item_id: str, headers, data: dict = None):
    pass
    url = f"https://api.notion.com/v1/{api_handle.value}/{item_id}"
    res = requests.request(request_type.value, url, headers=headers, data=json.dumps(data)).json()
    return res
