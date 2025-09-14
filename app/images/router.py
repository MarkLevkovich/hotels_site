import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_img

router = APIRouter(prefix='/images', tags=['Upload IMG'])

@router.post('/hotels')
async def add_hotel_image(name: int, file: UploadFile):
    img_path = f'app/static/images/{name}.webp'
    with open(img_path, 'wb+') as file_obj:
        shutil.copyfileobj(file.file, file_obj)

    process_img.delay(img_path)
