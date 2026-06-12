import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def github_session():
    token = os.getenv("GITHUB_TOKEN")
    
    if not token:
        pytest.fail("GITHUB_TOKEN is missing from the .env file!")

    session = requests.Session()
    
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    })
    
    yield session