import pytest
from playwright.async_api import async_playwright, APIRequestContext

@pytest.fixture(scope="session")
async def request_context() -> APIRequestContext:
    async with async_playwright() as p:
        context = await p.request.new_context(base_url="https://jsonplaceholder.typicode.com")

        yield context

        await context.dispose()
