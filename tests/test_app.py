import pytest
from starlette.testclient import TestClient


@pytest.mark.asyncio
async def test_root(
        client: TestClient,
):
    response = await client.get("/")
    assert response.status_code == 200
