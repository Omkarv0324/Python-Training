"""Session 3.4 demo — fetching JSON from an HTTP API with `requests`.

NOTE: requests is a third-party package: pip install requests
This demo works OFFLINE too — if requests isn't installed or there's no
network, it falls back to parsing a sample JSON payload so the lesson
always runs.
"""

import json

SAMPLE = '{"id": 1, "title": "automate the boring stuff", "completed": false}'


def fetch_todo():
    try:
        import requests  # imported lazily so the fallback works without it
        url = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()      # raises on 4xx/5xx
        print("Fetched live from the API")
        return response.json()
    except Exception as e:
        print(f"(Live fetch unavailable: {e}) — using offline sample")
        return json.loads(SAMPLE)


data = fetch_todo()
print("id:", data["id"])
print("title:", data["title"])
print("completed:", data["completed"])
