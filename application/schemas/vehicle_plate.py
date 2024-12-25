import re

from pydantic import BaseModel, Field, field_validator

GERMAN_PLATE_REGEX = r"^[A-Za-z]{1,3}-[A-Za-z]{1,2}[1-9]{1}[0-9]{0,3}$"


class GetVehiclePlateRequestModel(BaseModel):
    search_key: str = Field("", description="Search key for plate number")
    levenshtein: float = Field(
        default=1, ge=0, le=1, description="Levenshtein distance"
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
    timestamp: str


class GetVehiclePlateResponseModel(BaseModel):
    data: list[VehiclePlateDataModel]
    pagination: PagniationModel


class PostVehiclePlateRequestModel(BaseModel):
    plate: str = Field(..., description="Vehicle plate number")

    @field_validator("plate")
    @classmethod
    def validate_plate(cls, plate):
        if not re.fullmatch(GERMAN_PLATE_REGEX, plate):
            raise ValueError("Not a valid German vehicle plate number")
        return plate
