from app.tasks.celery import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_img(
        path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_200_100 = im.resize((200, 100))
    im_resized_200_100.save(f'app/static/images/resized_200_100{im_path.name}')