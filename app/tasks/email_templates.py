from email.message import EmailMessage
from pydantic import EmailStr
from app.config import settings


def create_booking_confirmation(
        booking: dict,
        email_to: EmailStr,
):
    email = EmailMessage()

    email['Subject'] = 'Подтверждение брони в Belarus BNB'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>Подтвердите бронь:</h1>
            <h3>Отель с {booking["date_from"]} до {booking["date_to"]}</h3>
        """,
        subtype="html"
    )
    return email