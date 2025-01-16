import json
import requests

write_file = open("segments.json", "a")

with open('segmentsToCheck.json') as f:
    segments = json.load(f)['segments']
    headers =  {"Content-Type": "application/json", "Authorization": "Bearer 856afca7900aa8e703abd0221c1cb5c2a291001c"}
    url = "https://www.strava.com/api/v3/segments/{id}"
    write_data = {"segments": []}
    
    for segment in segments:
        url = url.format(id=segment['id'])
        r = requests.get(url=url, headers=headers)
        write_data["segments"].append(r.json())
    json.dump(write_data, write_file)

write_file.close()