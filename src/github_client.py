import requests

def get_repo_count(username: str) -> int:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("public_repos", 0)
    
    # If the user doesn't exist or the API crashes, return -1
    return -1