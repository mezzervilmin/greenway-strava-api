import json
import requests

write_file = open("segments.json", "a")

with open('segmentsToCheck.json') as f:
    segments = json.load(f)['segments']
    headers =  {"Content-Type": "application/json", "Authorization": "Bearer 61967b1c4c076129d3f2e276058a02c047139603"}
    url = "https://www.strava.com/api/v3/segments/{id}"
    write_data = {"segments": []}
    
    for segment in segments:
        request_url = url.format(id=segment['id'])
        r = requests.get(url=request_url, headers=headers)
        write_data["segments"].append(r.json())
    json.dump(write_data, write_file)

write_file.close()