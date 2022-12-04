from src.prediction import predict
import settings
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from PIL import Image
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(content="status ok")


@app.post("/score")
async def score(file: UploadFile = File(...)):
    """Scoring endpoint
    Returns:
        dict: predicted data
    """

    image = Image.open(file.file)
    label = await predict(image=image)
    return {"label": label}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=settings.PORT,
    )
