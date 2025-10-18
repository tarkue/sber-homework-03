from fastapi import APIRouter

index_router = APIRouter(tags=["Root"])

@index_router.get("/")
def read_root():
    return {"message": "Это сообщение было отправлено с сервера, Капитан!"}