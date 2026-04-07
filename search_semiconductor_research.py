import os
import requests
import json

url = "http://192.168.15.64:9200/rabyte_saas_reading_roadshow_summary_index/_search"

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
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + os.environ.get('ES_AUTH_TOKEN', '')
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
