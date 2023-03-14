from fastapi import FastAPI


app = FastAPI()


@app.get("/api/healthchecker", name="Ababgalamaga")
def root():
    return {"message": "Kuku"}