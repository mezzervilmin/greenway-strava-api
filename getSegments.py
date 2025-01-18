import json
import requests

write_file = open("segments.json", "a")

with open('segmentsToCheck.json') as f:
    segments = json.load(f)['segments']
    headers =  {"Content-Type": "application/json", "Authorization": "Bearer 9b733afbfa6fb3a8dd6e125acfca844bbdaec856"}
    url = "https://www.strava.com/api/v3/segments/{id}"
    write_data = {"segments": []}
    
    for segment in segments:
        request_url = url.format(id=segment['id'])
        r = requests.get(url=request_url, headers=headers)
        write_data["segments"].append(r.json())
    json.dump(write_data, write_file)

write_file.close()