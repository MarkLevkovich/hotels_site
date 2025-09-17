from email.message import EmailMessage
from pydantic import EmailStr
from app.config import settings


def create_booking_confirmation(booking: dict, email_to: EmailStr):
    email = EmailMessage()

    email['Subject'] = '✅ Ваше бронирование подтверждено — Belarus Hotels'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    # Супер-качественное фото luxury отеля
    hotel_image_url = "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=1200&auto=format&fit=crop&q=80"

    email.set_content(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                    background-color: #f5f5f7;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                }}
                .email-container {{
                    max-width: 600px;
                    width: 100%;
                    background: #ffffff;
                    border-radius: 24px;
                    overflow: hidden;
                    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.08);
                    margin: 40px 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #000000 0%, #2c3e50 100%);
                    padding: 48px 40px;
                    text-align: center;
                    color: #ffffff;
                    position: relative;
                }}
                .header h1 {{
                    font-size: 32px;
                    font-weight: 600;
                    letter-spacing: -0.5px;
                    margin: 0 0 12px 0;
                }}
                .header p {{
                    font-size: 18px;
                    opacity: 0.9;
                    margin: 0;
                    font-weight: 300;
                }}
                .content {{
                    padding: 48px 40px;
                    text-align: center;
                }}
                .hotel-image {{
                    width: 100%;
                    height: 320px;
                    object-fit: cover;
                    border-radius: 20px;
                    margin: 0 0 36px 0;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }}
                .booking-dates {{
                    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
                    padding: 32px;
                    border-radius: 20px;
                    border: 1px solid rgba(0, 0, 0, 0.05);
                    margin: 0 0 36px 0;
                }}
                .dates-text {{
                    font-size: 24px;
                    font-weight: 500;
                    color: #1d1d1f;
                    margin: 0 0 16px 0;
                    letter-spacing: -0.3px;
                }}
                .date-range {{
                    font-size: 20px;
                    color: #6e6e73;
                    font-weight: 400;
                }}
                .confirmation-badge {{
                    display: inline-block;
                    background: linear-gradient(135deg, #007aff 0%, #0051a8 100%);
                    color: #ffffff;
                    padding: 20px 48px;
                    border-radius: 50px;
                    font-size: 20px;
                    font-weight: 600;
                    letter-spacing: 0.5px;
                    box-shadow: 0 8px 24px rgba(0, 122, 255, 0.3);
                    margin: 24px 0;
                }}
                .footer {{
                    background: #f5f5f7;
                    padding: 40px;
                    text-align: center;
                    border-top: 1px solid rgba(0, 0, 0, 0.05);
                }}
                .footer-text {{
                    font-size: 16px;
                    color: #86868b;
                    line-height: 1.6;
                    margin: 0;
                }}
                .apple-like-divider {{
                    height: 1px;
                    background: linear-gradient(90deg, transparent 0%, rgba(0, 0, 0, 0.1) 50%, transparent 100%);
                    margin: 36px 0;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <h1>Бронирование подтверждено</h1>
                    <p>Belarus Hotels • Премиум гостеприимство</p>
                </div>

                <div class="content">
                    <img src="{hotel_image_url}" alt="Luxury Hotel" class="hotel-image">

                    <div class="booking-dates">
                        <div class="dates-text">Даты вашего проживания</div>
                        <div class="date-range">📅 {booking["date_from"]} — {booking["date_to"]}</div>
                    </div>



                    <div class="apple-like-divider"></div>

                    <p style="color: #6e6e73; font-size: 18px; line-height: 1.6; margin: 0;">
                        Сохраните это письмо для предъявления при заселении.<br>
                        Мы с нетерпением ждём вашего приезда!
                    </p>
                </div>

                <div class="footer">
                    <p class="footer-text">
                        С уважением, команда Belarus Hotels<br>
                    </p>
                </div>
            </div>
        </body>
        </html>
        """,
        subtype="html"
    )
    return email