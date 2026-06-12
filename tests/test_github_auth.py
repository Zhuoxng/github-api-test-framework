def test_github_authentication_succeeds(github_session):
    url="https://api.github.com/user"
    response = github_session.get(url)
    assert response.status_code == 200

    data = response.json()
    assert "login" in data
    print(f"\nSuccess! Authenticated as GitHub user: {data['login']}")