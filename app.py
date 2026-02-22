#Criar ambiente virtual no Python: python -m venv venv
#Ativar ambiente virtual:           .\venv\Scripts\activate
#Instalar o Flask:                  pip install Flask
#Instalar variaveis de ambiente     pip install python-dotenv
#Criar arquivo oculto .gitignore    https://www.toptal.com/developers/gitignore
#Criar arquivo oculto .env          arquivo com variáveis de ambiente
#Criar pasta templates              para colocar os templates que o FLASK/Jinja irá buscar
    # - Arquivo index.html
    # - Arquivo user.html
#Criar a pasta static               para colocar os arquivos de modo que o jinja renderize corretamente
    # - Pasta CSS
    # - Pasta img
#Criar arquivo esquema.sql          onde tem os esquemas de criação dos bancos de dados
#Cirar aquivo init_db.py            arquivo de configurações do banco de dados


# importando a classe Flask do framework flask
from flask import Flask

# importando load_dotenv (permite importar as variáveis de ambiente)
from dotenv import load_dotenv

# importanto o OS (permite pegar o valor da variável de ambiente)
import os

# importando render_template do framework flask
from flask import render_template, g, flash, url_for, request, redirect, abort, session

# importando biblioteca sqlite3
import sqlite3

#Carregando o Banco de Dados
DATABASE="banco.db"
SECRET_KEY ="1234"


#carregando as variáveis de ambiente
load_dotenv()


# criando a aplicação
app = Flask(__name__)

# Carregando as COnfigurações para o banco de dados
app.config.from_object(__name__)

# Criando a função para conectar ao Banco de Dados
def conectar():
    return sqlite3.connect(DATABASE)

#Criando um decorator para abrir a função
@app.before_request
def before_request():
    g.db = conectar()

#Garantir o fechamento da conexão
@app.teardown_request
def teardown_request(f):
    g.db.close()  

# criando a rota usando decorator (URL)
@app.route('/')         #http://127.0.0.1:5001/

# criando o recurso
#def home():
def exibir_posts():
    sql = "SELECT titulo, texto, data_criacao from posts ORDER BY id DESC"
    resultado = g.db.execute(sql)
    posts = []

    for titulo, texto, data_criacao in resultado.fetchall():
        posts.append({
            "titulo":titulo,
            "texto":texto,
            "data_criacao":data_criacao
        })
    #return render_template('index.html')
    return render_template('exibir_posts.html', post = posts)   

@app.route("/login", methods = ["POST", "GET"])
def login():
    erro = None
    if(request.method == "POST"):
        if request.form['username'] == "Ocean" and request.form['password'] == "1234":
            session['logado'] = True
            flash("Usuário logado " + request.form['username'])
            return redirect(url_for('exibir_posts'))
        erro = "Usuário ou senha incorretos"
    return render_template("login.html", erro = erro) 

@app.route("/logout")
def logout():
    session.pop('logado', None)

    flash("Logout Efetuado")
    return redirect(url_for('exibir_posts'))

@app.route("/inserir", methods = ["POST", "GET"])
def inserir():
    if not session.get('logado'):
        abort(401)

    titulo = request.form.get('titulo') 
    texto = request.form.get('texto')

    sql = "INSERT INTO posts(titulo, texto) values (?, ?)"
    g.db.execute(sql,[titulo, texto])
    g.db.commit()
    flash("Novo post inserido")   
    return redirect(url_for('exibir_posts'))

""" Deletado na Aula04
# criando outra rota usando decorator (URL)
@app.route('/name')     #http://127.0.0.1:5001/name

# criando o recurso 
def username():
    name = "Jorge Dantas"
    return render_template("user.html", username=name) # retornará a renderização do user.html, em que username = name utilizando
                                                        # o render_template do FLASK (jinjar)
"""

""" Deletado na Aula 3 pois não estavamos usando
# criando outra rota usando decorator (URL)
@app.route('/nome')     #http://127.0.0.1:5001/nome

# criando o recurso 
def exibir_nome():
    return "Jorge Dantas"
"""


# ponto de entrada (entry point)
if __name__ =='__main__':
    app.run(port=os.getenv("FLASK_PORT"),       # Definindo a porta que quero usar na comunicação              
            debug = os.getenv("FLASK_DEBUG"),   # Habilitar o Debug: serve para a conexão reiniciar automaticamente o servidor 
            host = os.getenv("FLASK_HOST"))     # Permite que a aplicação se torne acessível na rede. Permite conexões externas
                                     
