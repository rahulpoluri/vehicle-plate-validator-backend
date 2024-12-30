import math
from datetime import datetime

from fastapi import APIRouter, Depends, Response

from application.db.models import Plates
from application.schemas.vehicle_plate import (
    GetVehiclePlateRequestModel,
    GetVehiclePlateResponseModel,
    PostVehiclePlateRequestModel,
)

router = APIRouter(
    prefix="/plate",
    tags=["vehicle_plates"],
    # dependencies=[Depends(get_token_header)]},
)


@router.get(
    "",
    responses={404: {"description": "Not found"}},
    response_model=GetVehiclePlateResponseModel,
)
async def get_plate(params: GetVehiclePlateRequestModel = Depends()):
    data, total = Plates.get_with_fuzzy_search(
        params.search_key.upper(),
        params.levenshtein,
        params.page_size,
        params.page_number,
    )
    pagination = {
        "page_number": params.page_number,
        "page_size": params.page_size,
        "total_pages": math.ceil(total / params.page_size),
        "total_items": total,
    }
    return {"data": data, "pagination": pagination}


@router.post("", responses={201: {"description": "Created"}})
async def post_plate(data: PostVehiclePlateRequestModel):
    Plates.put(Plates(plate=data.plate, timestamp=datetime.now()))
    return Response(status_code=201)
