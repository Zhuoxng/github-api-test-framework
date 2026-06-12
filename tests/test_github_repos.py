import pytest

class TestGitHubRepos:

    def test_get_user_repos_returns_list(self, github_session):
        url = "https://api.github.com/user/repos"
        response = github_session.get(url)
    
        assert response.status_code == 200
        assert isinstance(response.json(), list) 


    @pytest.mark.parametrize("repo_name", [
        "pytest-dev/pytest",
        "microsoft/vscode",
        "torvalds/linux"
    ])
    def test_public_repos_are_accessible(self, github_session, repo_name):
        url = f"https://api.github.com/repos/{repo_name}"
        response = github_session.get(url)
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify the data matches what we asked for
        assert data["full_name"] == repo_name
        assert "description" in data

    def test_non_existent_repo_returns_404(self, github_session):
        url = "https://api.github.com/repos/fake-user-999/fake-repo-999"
        response = github_session.get(url)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Not Found"