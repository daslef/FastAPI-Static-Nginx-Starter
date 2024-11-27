from fastapi import FastAPI


# Create an instance of FastAPI
app = FastAPI()


@app.get("/api/")
async def hello_world():
  return { "message": "Hello, World!" }


@app.get("/api/health")
async def healthcheck():
  return "OK"