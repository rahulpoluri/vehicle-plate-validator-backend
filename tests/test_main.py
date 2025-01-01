from dotenv import load_dotenv
from fastapi.testclient import TestClient

load_dotenv()

from application.main import app  # noqa

client = TestClient(app)
