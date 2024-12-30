import re
from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from application.examples import (
    PLATE_GET_RESPONSE_SCHEMA_EXAMPLE,
    PLATE_POST_REQUEST_SCHEMA_EXAMPLE,
)

GERMAN_PLATE_REGEX = r"^[A-Za-z]{1,3}-[A-Za-z]{1,2}[1-9]{1}[0-9]{0,3}$"


class GetVehiclePlateRequestModel(BaseModel):
    search_key: str = Field(..., description="Search key for plate number")
    levenshtein: int = Field(
        default=0,
        ge=0,
        le=10,
        description="Levenshtein distance, With maximum value of 2",
    )
    page_number: int = Field(default=1, ge=1, description="Page number")
    page_size: int = Field(default=10, ge=1, description="Page size")


class PagniationModel(BaseModel):
    page_number: int
    page_size: int
    total_pages: int
    total_items: int


class VehiclePlateDataModel(BaseModel):
    plate: str
    timestamp: datetime


class GetVehiclePlateResponseModel(BaseModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                PLATE_GET_RESPONSE_SCHEMA_EXAMPLE  # type: ignore[list-item]
            ]
        }
    }
    data: list[VehiclePlateDataModel]
    pagination: PagniationModel


class PostVehiclePlateRequestModel(BaseModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                PLATE_POST_REQUEST_SCHEMA_EXAMPLE  # type: ignore[list-item]
            ]
        }
    }

    plate: str = Field(..., description="Valid German plate number")

    @field_validator("plate")
    @classmethod
    def validate_plate(cls, plate):
        if not re.fullmatch(GERMAN_PLATE_REGEX, plate):
            raise ValueError("Not a valid German vehicle plate number")
        return plate
