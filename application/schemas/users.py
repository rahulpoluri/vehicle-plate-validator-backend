from pydantic import BaseModel, Field

from application.examples import USERS_PATCH_REQUEST_SCHEMA_EXAMPLE


class UserPasswordChangeRequestModel(BaseModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                USERS_PATCH_REQUEST_SCHEMA_EXAMPLE  # type: ignore[list-item]
            ]
        }
    }

    password: str = Field(..., description="New Password to be set")
