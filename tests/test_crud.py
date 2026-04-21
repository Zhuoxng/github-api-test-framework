import pytest
import uuid

class TestGitHubCRUD:

    @pytest.fixture
    def repo_lifecycle(self, github_session):
        unique_id = uuid.uuid4().hex[:8]
        repo_name = f"test-{unique_id}"
        user_data = github_session.get("https://api.github.com/user").json()
        username = user_data["login"]
        yield repo_name, username
        delete_url = f"https://api.github.com/repos/{username}/{repo_name}"
        github_session.delete(delete_url)

    def test_repo_crud_lifecycle(self, github_session, repo_lifecycle):
        repo_name, username = repo_lifecycle
        repo_url = f"https://api.github.com/repos/{username}/{repo_name}"

        # Create repo
        create_url = "https://api.github.com/user/repos"
        payload = {
            "name": repo_name,
            "description": "Created by auto QA test",
            "private": True
        }
        create_response = github_session.post(create_url, json=payload)
        assert create_response.status_code == 201

        # Read repo
        read_response = github_session.get(repo_url)
        assert read_response.status_code == 200
        assert read_response.json()["description"] == "Created by auto QA test"

        # Update repo
        update_payload = {"description": "Updated by QA Auto v2"}
        update_response = github_session.patch(repo_url, json=update_payload)

        assert update_response.status_code == 200
        assert update_response.json()["description"] == "Updated by QA Auto v2"

        # Delete repo
        #guardrail 
        if repo_name.startswith("test-"):
         delete_response = github_session.delete(repo_url)
         assert delete_response.status_code == 204

        # Check if deleted
        verify_res = github_session.get(repo_url)
        assert verify_res.status_code == 404

