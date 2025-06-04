import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, APIRequestContext

# Async fixture for creating request context
@pytest_asyncio.fixture(scope="session")
async def request_context() -> APIRequestContext:
    async with async_playwright() as p:
        request_context = await p.request.new_context(base_url="https://jsonplaceholder.typicode.com")
        yield request_context
        await request_context.dispose()

@pytest.mark.asyncio
async def test_get_post(request_context: APIRequestContext):
    response = await request_context.get("/posts/1")
    assert response.ok
    json_data = await response.json()
    assert json_data["id"] == 1
    print(json_data)

@pytest.mark.asyncio
async def test_create_post(request_context: APIRequestContext):
    payload = {
        "title": "Playwright Async",
        "body": "Testing POST method",
        "userId": 101
    }
    response = await request_context.post("/posts", data=payload)
    assert response.status == 201
    json_data = await response.json()
    assert json_data["title"] == "Playwright Async"
    print(json_data)

@pytest.mark.asyncio
async def test_update_post(request_context: APIRequestContext):
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Content",
        "userId": 1
    }
    response = await request_context.put("/posts/1", data=payload)
    assert response.status == 200
    json_data = await response.json()
    assert json_data["title"] == "Updated Title"
    print(json_data)

@pytest.mark.asyncio
async def test_delete_post(request_context: APIRequestContext):
    response = await request_context.delete("/posts/1")
    assert response.status == 200
    print("Deleted successfully.")
