import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

INITIAL_ACTIVITIES_STATE = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: restore baseline in-memory state before each test.
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES_STATE))


@pytest.fixture
def client():
    # Arrange: create a test client for API calls.
    return TestClient(app)
