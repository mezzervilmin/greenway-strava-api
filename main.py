from fastapi import FastAPI, Response
import json
import polyline

app = FastAPI()


@app.get("/getSegments")
async def get_segments():
    with open("segments.json", "r") as file:
        data = json.load(file)
    for segment in data["segments"]:
        segment["map"]["polyline"] = [(y, x) for (x, y) in polyline.decode(segment["map"]["polyline"])]
    return Response(content=json.dumps(data), media_type="application/json")