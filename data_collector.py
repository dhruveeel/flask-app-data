from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# Set your JSONBin API key (replace 'YOUR_API_KEY' with your actual key)
JSONBIN_API_KEY = "$2a$10$0w8uk//5hlkgzaZ8zsWxPORuyBe3SlpcsuxtwglCZ9kyUEyZMbTuS"
BIN_ID = "67d0ce128561e97a50ea3883"

# Headers for JSONBin requests
HEADERS = {
    'Content-Type': 'application/json',
    'X-Master-Key': JSONBIN_API_KEY
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Fetch current data from JSONBin
        response = requests.get(f'https://api.jsonbin.io/v3/b/{BIN_ID}', headers=HEADERS)
        data = response.json().get('record', [])

        # Add new user
        data.append({'name': name, 'email': email})

        # Update JSONBin with new data
        update_response = requests.put(f'https://api.jsonbin.io/v3/b/{BIN_ID}', json=data, headers=HEADERS)

        if update_response.status_code == 200:
            return redirect('/')
        else:
            return f"Error saving data: {update_response.text}"

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
