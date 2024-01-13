from service_layer import bootstrap
from typing import Union

from fastapi import FastAPI

from scripts import create_database


app = FastAPI()


bus = bootstrap.bootstrap()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    # Iniciar o servidor usando uvicorn
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
