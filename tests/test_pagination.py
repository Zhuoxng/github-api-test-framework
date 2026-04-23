import pytest
import asyncio
import httpx
import os

@pytest.mark.asyncio
async def test_async_pagination():
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    base_url = "https://api.github.com/users/microsoft/repos"

    async def fetch_page(client, page_number):
        response = await client.get(f"{base_url}?page={page_number}&per_page=30")
        assert response.status_code == 200
        return response.json()
    
    async with httpx.AsyncClient(headers=headers) as client:
        tasks = [fetch_page(client, page) for page in range(1,6)]
        pages = await asyncio.gather(*tasks)
    
    assert len(pages) == 5
    assert len(pages[0]) == 30
    assert pages[0][0]["id"] != pages[1][0]["id"], "Error: duplicate pages"

    