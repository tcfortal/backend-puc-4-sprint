from flask_cors import CORS
from flask import Flask, request
import pickle
from bd import Idiomas

def importa_modelo():
    modelo = pickle.load(open('./trained_pipeline.sav', 'rb'))
    return modelo

app = Flask(__name__)
modelo = importa_modelo()



@app.route('/idiomas', methods=['GET'])
def get_idiomas():
    return Idiomas




@app.route('/idiomas', methods=['POST'])
def home():
    dados_post = request.get_json()
    dados = [dados_post[i] for i in ['frase']]
    resultado = modelo.predict(dados)[0]
    Idiomas.append({'idioma': resultado})
    
    return resultado









CORS(app)



app.run(
    debug=True,
    port='5001'
)