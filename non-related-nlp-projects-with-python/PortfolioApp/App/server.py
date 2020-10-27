from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/index")
def my_home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/works")
def work():
    return render_template('works.html')


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou')
    else:
        return "bg"


def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db,delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


