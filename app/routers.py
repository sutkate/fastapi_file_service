from fastapi import APIRouter, UploadFile, HTTPException, Query
import os
from pathlib import Path

router = APIRouter()

base_dir = Path("uploaded_files")
base_dir.mkdir(exist_ok=True)

@router.post("/file-manager")
async def upload_file(service_name: str = Query(...),file: UploadFile = None):
    try:
        #создание директории если не существует
        service_dir = base_dir / service_name
        service_dir.mkdir(parents=True, exist_ok=True)

        #сохранение файла в директории
        file_path = service_dir / file.filename
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        return {"status": 201, "file_path": str(file_path)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка загрузки: {str(e)}")

@router.delete("/file-manager")
async def delete_file(service_name: str = Query(...)):
    try:
        file_path = base_dir / service_name
        if not file_path.exists():
            raise HTTPException(status_code=400, detail="Файл не найден") #если файл не найден

        os.remove(file_path)
        return {"status": 201, "message": "Файл удален"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка удаления файла: {str(e)}")
