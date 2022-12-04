import pytest

from src.post_processing import post_processing


@pytest.mark.parametrize(
    "prediction_unfiltered,expected_prediction",
    [
        ("Cleat", "Shoe"), ("Shoe", "Shoe"),
        ("Clog", "Boot"), ("Boot", "Boot"),
        ("Slipper", "Sandal"), ("Sandal", "Sandal"),
        ("Rubber", "Shoe")
    ],
)
@pytest.mark.asyncio
async def test_get_filtered_customer_name(prediction_unfiltered, expected_prediction):
    actual_prediction = await post_processing(prediction_unfiltered)
    assert actual_prediction == expected_prediction
