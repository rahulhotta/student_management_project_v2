import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.utility.email_utility import SENDER_EMAIL, SENDER_PASSWORD
from scripts.constants.app_constants import Email
from scripts.logging.log_config import getLogger

logger = getLogger()
class Email_handler:
    def send_email(self,body, Email: Email):
        # Set up the email details
        sender_email = SENDER_EMAIL
        sender_password = SENDER_PASSWORD
        receiver_email = Email.rec_email

        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = Email.subject
        
    # Add the body to the email
        message.attach(MIMEText(body, "html"))

        try:
            # Create a secure connection to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login to the sender's email account
            server.login(sender_email, sender_password)
            
            # Send the email
            server.send_message(message)

            # Close the connection
            server.quit()

            return {"message": "Email sent successfully"}
        
        except Exception as e:
            # logger.info({"status": "failed","error":str(e.args)})
            logger.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
email_object = Email_handler()