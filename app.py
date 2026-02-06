#Criar ambiente virtual no Python: python -m venv venv
#Ativar ambiente virtual:           .\venv\Scripts\activate
#Instalar o Flask:                    pip install Flask

# importando a classe Flask do framework flask
from flask import Flask

# criando a aplicação
app = Flask(__name__)

# criando a rota(URL)
@app.route('/')

# criando o recurso
def home():
    return "Hello, world!"