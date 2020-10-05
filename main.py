from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from models.main import DecryptRequest, DecryptResponse 
from service import process_data
app = FastAPI()


@app.get('/hello', name="return Hello world")
async def demo():
    return {"Hello": "world"}


@app.post('/decrypt', name="Encrypt name, decrypt hash")
async def handle_decryption(req : DecryptRequest ) -> DecryptResponse:
    print(f'Request : {req.dict()}')
    result = process_data(req.dict())
    return result







# serving static files

@app.get("/{html_file}", include_in_schema=False)
def index_file(html_file: str):
    return FileResponse('./static/{}'.format(html_file))


@app.get("/", include_in_schema=False)
def index_assetfile():
    return RedirectResponse(url="/index.html")
