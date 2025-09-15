from app.config import settings
from app.tasks.celery import celery
from PIL import Image
from pathlib import Path
from pydantic import EmailStr
import smtplib
from app.tasks.email_templates import create_booking_confirmation


@celery.task
def process_img(
        path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_200_100 = im.resize((200, 100))
    im_resized_200_100.save(f'app/static/images/resized_200_100{im_path.name}')



@celery.task
def send_booking_confirmation(
        booking: dict,
        email_to: EmailStr,
):
    test_my_mail = settings.SMTP_USER
    msg_content = create_booking_confirmation(booking, test_my_mail)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)