from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        # wttr.in — бесплатный API без ключа
        url = f"https://wttr.in/{city}?format=j1"
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            current = data['current_condition'][0]
            temperature = current['temp_C']
            description = current['weatherDesc'][0]['value']
            return render_template('result.html', city=city, temperature=temperature, description=description)
        except Exception as e:
            return render_template('result.html', city=city, temperature="N/A", description=f"Ошибка: {e}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
