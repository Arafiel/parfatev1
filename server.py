from flask import Flask, render_template, request, redirect, send_from_directory
import csv
app = Flask(__name__)


def write_to_csv(data):
    with open('database.csv', newline='',  mode='a') as db2:
        email = data['email']
        csv_writer = csv.writer(
            db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data['email'])
        if data['email'] == '':
            return render_template('index.html', text="Please enter a valid email address.")
        else:
            try:
                write_to_csv(data)
                return render_template('index.html', text="Thanks!  Stay stuned for updates.")
            except:
                return render_template('index.html', text="Something went wrong, please try again.")
    else:
        return render_template('index.html', text="Something went wrong, please try again.")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
