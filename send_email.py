import smtplib
import ssl


def send_email(message, user_email):
    host = "smtp.gmail.com"
    port = 465
    username = "simoaboulfath52@gmail.com"
    password = ""
    receiver = "simoaboulfath52@gmail.com"
    context = ssl.create_default_context()
    email_message = f"Subject: New Contact Message\n\n{message}\n\nFrom: {user_email}"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message)

