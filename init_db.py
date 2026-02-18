#Arquivo de configurações para gerenciar o banco de dados

#Importar a biblioteca sqlite3
import sqlite3

#Criar uma conexão
conn =sqlite3.connect("banco.db")

#Excrever a tabela do esquema.sql dentro do banco.db
with open("esquema.sql","r",encoding="utf-8") as f:
    conn.executescript(f.read())

    # Confirmar a criacação
    conn.commit()
    
    # Fechar a conexão
    conn.close()

    print("Banco de Dados criado com sucesso")