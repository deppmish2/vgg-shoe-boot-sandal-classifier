from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
from src.post_processing import post_processing


async def predict(image: any) -> str:
    """Small example function that will take some data and returns a response.
    Right now everything is with fixed values.

    Args:
        image : prediction data

    Returns:
        str: predicted response
    """
    model = VGG16()

    # size as expected in vgg model
    size = (224, 224)
    image = np.array(image.resize(size))

    # reshape data for the VGG model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    # preprocess the image for the model
    image = preprocess_input(image)

    # predict the probability across all output classes
    yhat = model.predict(image)

    # convert the probabilities to labels
    label = decode_predictions(yhat)

    # get the result after post processing
    label = label[0][0]
    return await post_processing(label[1])
