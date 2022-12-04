from settings import prediction_options, DEFAULT_PREDICTION


async def post_processing(prediction: str) -> str:
    """
    Args:
        prediction : prediction from the model
    Returns:
        str: filtering predicted response as needed by application
    """

    # Since it is a generic model, choosing synonyms and options based on common scenarios
    for filtered_prediction in prediction_options.keys():
        if prediction.lower() in prediction_options.get(filtered_prediction):
            return filtered_prediction
        else:
            continue

    return DEFAULT_PREDICTION
