from fastapi import FastAPI #type: ignore

app = FastAPI(title="AI prep Platform1")

@app.get("/")
def welcom():
    return {"status":"ok"}