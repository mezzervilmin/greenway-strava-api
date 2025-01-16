from fastapi import FastAPI, Response
import json

app = FastAPI()


@app.get("/getSegments")
async def get_segments():
    with open("segments.json", "r") as file:
        data = json.load(file)
    return Response(content=json.dumps(data), media_type="application/json")