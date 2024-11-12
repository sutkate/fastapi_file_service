import aiofiles
from config import base_dir
from fastapi import UploadFile, HTTPException, Query
import os


async def save_file(service_name: str = Query(...), file: UploadFile = None):
    try:
        service_dir = base_dir / service_name
        service_dir.mkdir(parents=True, exist_ok=True)

        file_path = service_dir / file.filename
        async with aiofiles.open(file_path, "wb") as f:
            content = await file.read()
            await f.write(content)

        return {"status": 201, "file_path": str(file_path)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ошибка: {str(e)}")

async def delete_file(service_name: str = Query(...)):
    try:
        file_path = base_dir / service_name
        if not file_path.exists():
            raise HTTPException(status_code=400, detail="Файл не найден") #если файл не найден

        os.remove(file_path)
        return {"status": 201, "message": "Файл удален"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка удаления файла: {str(e)}")