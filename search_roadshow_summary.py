import os
import requests
import json

# Configuration - set these via environment variables
ES_HOST = os.environ.get("ES_HOST", "http://localhost:9200")
ES_AUTH = os.environ.get("ES_AUTH", "")  # Base64-encoded "username:password"

url = f"{ES_HOST}/rabyte_saas_reading_roadshow_summary_index/_search"

payload = json.dumps({
    "_source": [
        "id",
        "title",
        "date",
        "summary",
        "institution.name",
        "recorder",
        "doc_name"
    ],
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "fields": [
                            "title",
                            "content",
                            "auto_srh_word"
                        ],
                        "query": "半导体 技术壁垒",
                        "type": "best_fields"
                    }
                },
                {
                    "term": {
                        "is_deleted": 0
                    }
                },
                {
                    "term": {
                        "is_private": 0
                    }
                },
                {
                    "term": {
                        "recorder": "AI"
                    }
                },
                {
                    "range": {
                        "date": {
                            "gte": "2025-04-07 00:00:00",
                            "lte": "2026-04-07 23:59:59"
                        }
                    }
                }
            ]
        }
    },
    "size": 20,
    "sort": [
        {
            "date": "desc"
        }
    ]
})

headers = {
    "Content-Type": "application/json",
}
if ES_AUTH:
    headers["Authorization"] = f"Basic {ES_AUTH}"

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
