from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from application.auth import generate_token, verify_username_and_password
from application.db.models import Users
from application.schemas.users import UserPasswordChangeRequestModel

router = APIRouter(
    prefix="",
    tags=["Users"],
    # dependencies=[Depends(generate_token)],
)


@router.post(
    "/token",
    responses={404: {"description": "Not found"}},
    # response_model=GetVehiclePlateResponseModel,
)
async def login_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = Users.get_one_or_404(username=form_data.username)
    access_token = generate_token(user.username, user.password, user.role)
    user.token = access_token
    user.save()
    return {"access_token": access_token, "token_type": "bearer"}


@router.patch(
    "/password",
    responses={
        404: {"description": "Not found"},
        401: {"description": "Not Authenticated"},
    },
    dependencies=[Depends(verify_username_and_password)],
)
async def change_password(data: UserPasswordChangeRequestModel):
    return Response(status_code=200)


# @router.post(
#     "",
#     responses={404: {"description": "Not found"}},
#     # response_model=GetVehiclePlateResponseModel,
# )
# async def create_user():
#     return

# @router.delete(
#     "",
#     responses={404: {"description": "Not found"}},
#     # response_model=GetVehiclePlateResponseModel,
# )
# async def delete_user():
#     return
