from flask import Flask,render_template, url_for, request, flash
from flask_bootstrap import Bootstrap5
from datetime import date
import smtplib
import os

EMAIL=os.environ.get("EMAIL_ADD")
APP_PASSWORD=os.environ.get("EMAIL_PASSWORD")

app=Flask("__name__")
app.config["SECRET_KEY"]=os.environ.get("SECRET_KEY")
bootstrap=Bootstrap5(app)

@app.route('/')
def home():
    current_year=date.today().year
    return render_template("index.html", year=current_year)

@app.route("/contact",methods=["GET","POST"])
def contact():
    current_year = date.today().year
    if request.method=="POST":
        data=request.form
        send_email(data["name"],data["email"],data["message"])
        flash("Your message has been sent.")

    return render_template("index.html", is_sent=True, year=current_year)

def send_email(name,email,message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        email_msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
        connection.starttls()
        connection.login(EMAIL,APP_PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=email_msg)


if __name__=="__main__":
    app.run(debug=False)