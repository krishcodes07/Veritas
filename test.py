# Testimg Code

import requests

def test_research():
    url = "http://127.0.0.1:8000/research"
    payload = {
        "query": "Is nuclear energy safer than fossil fuels?"
    }
    response = requests.post(url, json=payload)
    print(response.json())

if __name__ == "__main__":
    test_research()