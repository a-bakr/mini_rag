from fastapi import APIRouter, Depends, UploadFile, status
from controllers import DataController, ProjectController
from helpers.config import get_settings, Settings
from fastapi.responses import JSONResponse
from models import ResponseSignal
import logging
import aiofiles

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, 
                      app_settings: Settings = Depends(get_settings)):

    # validate the file properties
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
    
    file_path, file_id = data_controller.generate_unique_filename(file.filename, project_id)

    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as ex:
        logging.error(f"Error while uploading file: {ex}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED
            }
        )

    return JSONResponse(
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id": file_id
        }
    )
    