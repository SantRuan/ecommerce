

from fastapi import FastAPI
from routers.router import router



app = FastAPI()
app.include_router(router=router)







if __name__ == "__main__":
    # Iniciar o servidor usando uvicorn
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
