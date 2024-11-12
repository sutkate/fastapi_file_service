from fastapi import APIRouter, Query, UploadFile
from services import save_file, delete_file
router = APIRouter()

@router.post("/file-manager")
async def upload_file(service_name: str = Query(...),file: UploadFile = None):
    return await save_file(service_name, file)

@router.delete("/file-manager")
async def delete_file(service_name: str = Query(...)):
    return await delete_file(service_name)
