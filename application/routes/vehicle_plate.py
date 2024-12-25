from fastapi import APIRouter, Depends, Response

from application.schemas.vehicle_plate import (GetVehiclePlateRequestModel,
                                               GetVehiclePlateResponseModel,
                                               PostVehiclePlateRequestModel)

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
    return {
        "data": [
            {"plate": "M-PP123", "timestamp": "2020-09-18T13:21:21Z"},
            {"plate": "K-A123", "timestamp": "2020-09-18T14:21:21Z"},
        ],
        "pagination": {
            "page_number": 1,
            "page_size": 10,
            "total_pages": 5,
            "total_items": 50,
        },
    }


@router.post("", responses={201: {"description": "Created"}})
async def post_plate(data: PostVehiclePlateRequestModel):
    return Response(status_code=201)
