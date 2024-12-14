from fastapi import APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@base_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings = Depends(get_settings)):

    # validate teh file properties
    pass