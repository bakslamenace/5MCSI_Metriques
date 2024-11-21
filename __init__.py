from flask import Flask, render_template, jsonify
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("forms.html")

@app.route('/tawarano/')
def meteo():
    try:
        response = urlopen('https://api.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')  # Remplacez 'xxx' par votre clé API
        raw_content = response.read()
        json_content = json.loads(raw_content.decode('utf-8'))
        results = []
        for list_element in json_content.get('list', []):
            dt_value = list_element.get('dt')
            temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Conversion de Kelvin en °C
            results.append({'Jour': dt_value, 'temp': temp_day_value})
        return jsonify(results=results)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

if __name__ == "__main__":
    app.run(debug=True)
