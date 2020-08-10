from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def demo():
    return {"Hello":"world"}