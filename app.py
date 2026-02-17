#Criar ambiente virtual no Python: python -m venv venv
#Ativar ambiente virtual:           .\venv\Scripts\activate
#Instalar o Flask:                  pip install Flask
#Instalar variaveis de ambiente     pip install python-dotenv
#Criar arquivo oculto .gitignore    https://www.toptal.com/developers/gitignore
#Criar arquivo oculto .env          arquivo com variáveis de ambiente
#Criar pasta templates
    # - Arquivo index.html



# importando a classe Flask do framework flask
from flask import Flask

# importando load_dotenv (permite importar as variáveis de ambiente)
from dotenv import load_dotenv

# importanto o OS (permite pegar o valor da variável de ambiente)
import os

# importando render_template do framework flask
from flask import render_template



#carregando as variáveis de ambiente
load_dotenv()


# criando a aplicação
app = Flask(__name__)

# criando a rota usando decorator (URL)
@app.route('/')         #http://127.0.0.1:5001/

# criando o recurso
def home():
    return render_template('index.html')


# criando outra rota usando decorator (URL)
@app.route('/nome')     #http://127.0.0.1:5001/nome

# criando o recurso 
def exibir_nome():
    return "Jorge Dantas"




# ponto de entrada (entry point)
if __name__ =='__main__':
    app.run(port=os.getenv("FLASK_PORT"),       # Definindo a porta que quero usar na comunicação              
            debug = os.getenv("FLASK_DEBUG"),   # Habilitar o Debug: serve para a conexão reiniciar automaticamente o servidor 
            host = os.getenv("FLASK_HOST"))     # Permite que a aplicação se torne acessível na rede. Permite conexões externas
                                     
