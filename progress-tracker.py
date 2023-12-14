import requests

NOTION_TOKEN = "secret_cntS6HgntEcYu5ZbqjmOTCImx2aYJpgUgoOfTWdivY0"
DATABASE_ID = "2468f412c6f34e5689004aa283d568ae?pvs=4"
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_pages(num_pages=None):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    get_all = num_pages is None
    page_size = 100 if get_all else num_pages
    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print(data)
    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])
    return results

pages = get_pages()
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    print(props)
    exit()