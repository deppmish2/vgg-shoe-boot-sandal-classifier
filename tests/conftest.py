import pytest_asyncio
from httpx import AsyncClient
from app import app as test_app


@pytest_asyncio.fixture(scope="session")
def filename():
    return "Shoe (6).jpg"


@pytest_asyncio.fixture(scope="session")
def filepath(filename):
    return f"Shoe/{filename}"


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
            app=test_app, base_url="http://test"
    ) as test_client:
        yield test_client
