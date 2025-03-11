from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Route for the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Save to CSV
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email])

        return redirect('/')

    return '''
    <h2>Enter your details:</h2>
    <form method="post">
        Name: <input type="text" name="name" required><br>
        Email: <input type="email" name="email" required><br>
        <button type="submit">Submit</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
