from unittest.mock import patch
from src.github_client import get_repo_count

class TestGitHubClientMocked:

    @patch("src.github_client.requests.get")
    def test_get_repo_count_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"public_repos": 42}

        result = get_repo_count("randomuser")

        assert result == 42
        mock_get.assert_called_once_with("https://api.github.com/users/randomuser")

    @patch("src.github_client.requests.get")
    def test_get_repo_count_handles_api_crash(self, mock_get):
        mock_get.return_value.status_code = 500
        
        result = get_repo_count("randomuser")
        assert result == -1
