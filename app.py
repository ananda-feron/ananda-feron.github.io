from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        send_email(name, email, message)  # Call the function to send email
        
        return "Your message has been sent!"  # redirect to another page or show a success message
    
    return render_template("index.html")  # Render the form (replace 'index.html' with your template)

def send_email(name, email, message):
    sender_email = "your-email@gmail.com"  # input email (this will be used to send emails)
    sender_password = "your-email-password"  # App password or email password
    
    recipient_email = "anandaferon1@outlook.com"  # my email where messages are sent
    
    # Setting up the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "New Contact Form Message"

    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    # Setting up the server (use Gmail SMTP server, or another one)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
  
