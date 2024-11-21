from flask import Flask, render_template, jsonify
from urllib.request import urlopen
import json
from datetime import datetime
from collections import Counter
import requests

app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("forms.html")

@app.route('/')
def hello_world():
    return render_template('hello.html')  # comm2

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Conversion de Kelvin en °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def mongraphique2():
    return render_template("graphique2.html")

# Route pour fournir les données des commits
@app.route('/commits-data/')
def commits_data():
    try:
        # URL de l'API GitHub pour récupérer les commits
        url = 'https://github.com/mamacito93/5MCSI_Metriques/commits'
        response = requests.get(url)
        response.raise_for_status()  # Vérification des erreurs HTTP
        
        commits = response.json()
        
        # Extraire les minutes des dates de commits
        minutes_list = [
            datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ').minute
            for commit in commits
        ]
        
        # Compter le nombre de commits par minute
        minutes_count = Counter(minutes_list)
        
        # Transformer en format JSON pour le graphique
        data = [{'minute': minute, 'count': count} for minute, count in sorted(minutes_count.items())]
        return jsonify(data=data)
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Route pour afficher le graphique des commits
@app.route("/commits/")
def commits():
    return render_template("commits.html")

if __name__ == "__main__":
    app.run(debug=True)
