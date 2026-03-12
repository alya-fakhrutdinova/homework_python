import uuid
import pytest
from dotenv import load_dotenv
from yougile_api import YougileAPI

load_dotenv()



@pytest.fixture()
def api() -> YougileAPI:
    return YougileAPI()



@pytest.fixture()
def created_project(api: YougileAPI) -> str:
    title = f"test_project_{uuid.uuid4()}"
    r = api.create_project(title)
    assert r.status_code == 201, r.text

    project_id = r.json().get("id")
    assert project_id

    yield project_id

    api.delete_project(project_id)
