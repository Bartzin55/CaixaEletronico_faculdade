import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'contas.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'Contas'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#CRIA TABELA
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'Nome TEXT NOT NULL,'
    'Senha TEXT NOT NULL,'
    'Saldo REAL DEFAULT 0,'
    'Numero_cartao TEXT,'
    'Data_validade_cartao DATE,'
    'CVV TEXT,'
    'Senha_cartao TEXT'
    ')'
)
connection.commit()

def fechar_conexão(): #fecha conexao com banco de dados, usado ao desligar o caixa eletronico
    cursor.close()
    connection.close()

#Função que adiciona uma conta que não existe
def adicionarconta(nome, senha):
    cursor.execute(
        f'INSERT INTO {TABLE_NAME} (Nome, Senha) VALUES (?,?)',
        (nome, senha)
    )
    connection.commit()

def verificalogin(idusuario, senha):
    cursor.execute(f'SELECT Senha FROM {TABLE_NAME} WHERE id = ?', (idusuario,)) #procura na database 
    resultado = cursor.fetchone() #coleta a linha de resultado da consulta

    if resultado:
        senha_salva = resultado[0]
        if senha == senha_salva:
            return True
        else:
            return False
    else:
        return False

#função que coleta o nome do usuário logado relacionado ao nome, para mostrá-lo no sistema
def coletarnome(idusuario):
    cursor.execute(
        f'SELECT Nome FROM {TABLE_NAME} WHERE id = ?',
        (idusuario,)
    )
    nomeusuario = cursor.fetchone()
    return nomeusuario[0]

#na criação de um cartão, essa função coletará os dados do cartao e salvará no banco de dados
def inserircartao(numerocartao, validade, cvv, senha, idusuario):
    cursor.execute(
        f'UPDATE {TABLE_NAME} SET Numero_cartao = ?, Data_validade_cartao = ?, CVV = ?, Senha_cartao = ? WHERE id = ?',
        (numerocartao, validade, cvv, senha, idusuario)
    )
    connection.commit()

def coletarid(nomeusuario): #coletar nome do usuário relacionado ao ID
    cursor.execute(
        f'SELECT id FROM {TABLE_NAME} WHERE Nome = ?',
        (nomeusuario,)
    )
    idusuario = cursor.fetchone()
    return idusuario[0]

def coletarsaldo(idusuario):
    cursor.execute(
        f'SELECT Saldo FROM {TABLE_NAME} WHERE id = ?',
        (idusuario,)
    )
    saldo = cursor.fetchone()
    return saldo[0]

def depositarvalor(iduser, valor): #adiciona valor à conta do usuário
    cursor.execute(
        f'UPDATE {TABLE_NAME} SET Saldo = Saldo + ? WHERE id = ?',
        (valor, iduser)
    )
    connection.commit()

def sacarvalor(iduser, valor):
    cursor.execute(
        f'UPDATE {TABLE_NAME} SET Saldo = Saldo - ? WHERE id = ?',
        (valor, iduser)
    )
    connection.commit()

def verifica_id_existe(id_usuario): #em operações de transferência, é necessário verificar se a conta de desitno existe, essa função faz isso pelo ID
    cursor.execute(
        f'SELECT 1 FROM {TABLE_NAME} WHERE id = ?',
        (id_usuario,)
    )
    resultado = cursor.fetchone()
    if resultado:
        return True
    else:
        return False

def coletardadoscartao(id_usuario): #busca dados do cartão
    cursor.execute(f'SELECT Numero_cartao, Data_validade_cartao, CVV FROM {TABLE_NAME} WHERE id = ?', (id_usuario,))
    resultado = cursor.fetchone()
    if resultado:
        numerocartao_pego, data_pega, cvv_pego = resultado
        return numerocartao_pego, data_pega, cvv_pego
    else:
        return None, None, None

def deletar_usuario(id_usuario): #deleta a conta do usuario
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} WHERE id = ?',
        (id_usuario,)
    )
    connection.commit()