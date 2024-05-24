from flask import Flask, render_template, request, redirect, url_for 
import pymongo

app = Flask(__name__)

app.secret_key = "asdfghjkhgfd3456789087654w12e34"

connection = pymongo.MongoClient("mongodb://localhost:27017/")

databasename = connection["ResturantDB"]

contactCollection = databasename["Contact"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():

    if request.method == "POST":
        fullname = request.form['fullname']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        contactDetails = {"Fullname": fullname, "Email":email, "Subject":subject, "Message":message}
        contactCollection.insert_one(contactDetails)
        return redirect(url_for('home'))
    return render_template("contact.html")

@app.route("/contactlist")
def contactlist():
    contact_list = contactCollection.find()
    return render_template("contactlist.html", allList = contact_list)


if __name__ == "__main__":
    app.run(debug=True, port=7000)