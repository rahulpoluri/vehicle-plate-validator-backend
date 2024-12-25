from fastapi.testclient import TestClient

from application.main import app

client = TestClient(app)
