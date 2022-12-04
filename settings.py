import os
from pathlib import Path
import pathlib

PORT = int(os.getenv("PORT", "8000"))
DATA_PATH = pathlib.Path(Path().absolute(), "data")

prediction_options = {
    "Shoe": ["cleat", "sneaker", "shoe"],
    "Boot": ["clog", "boot"],
    "Sandal": ["slipper", "sandal"],
}

DEFAULT_PREDICTION = "Shoe"
