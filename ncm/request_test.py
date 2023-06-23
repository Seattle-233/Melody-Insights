import requests
import json

url = "http://localhost:3000/song/wiki/summary?id=1971144922"

response = requests.get(url)
data = json.loads(response.text)

# 提取曲风信息
creatives = data["data"]["blocks"][1]["creatives"]
for creative in creatives:
    if creative["creativeType"] == "songTag":
        resources = creative["resources"]
        for resource in resources:
            if resource["resourceType"] == "melody_style":
                title = resource["uiElement"]["mainTitle"]["title"]
                print("曲风:", title)
