from src.prediction import predict
import pytest
from PIL import Image
from settings import DATA_PATH
import pathlib


@pytest.mark.asyncio
async def test_predict(
        filepath: str
):
    upload_img_filepath = str(pathlib.Path(DATA_PATH, filepath))
    image = Image.open(upload_img_filepath)
    label = await predict(image=image)

    assert label == "Shoe"
