from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

api_key = os.getenv('API_NINJAS_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    company_name = request.form['company']
    api_url = f'https://api.api-ninjas.com/v1/logo?name={company_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    
    if response.status_code == 200:
        data = response.json()
        if data:
            company_data = data[0]
            print("API Response:", company_data)  
            return render_template('result.html', data=company_data)
        else:
            return "No data returned from API"
    else:
        print("API Error:", response.status_code, response.text)  
        return f"Error: {response.status_code} {response.text}"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
