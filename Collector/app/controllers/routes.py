import os
from flask import render_template
from app import app
from ftplib import FTP

# TODO: Criar arquivo para armazenas as variaveis de ambiente
dir_name = '/terrama2q/TerraMA2Q_408'
ftp_adress = 'ftp.dgi.inpe.br'
user_info = ('queimadas', 'inpe_2012')

conn = FTP(ftp_adress)
conn.login(*user_info)
conn.cwd(dir_name)


@app.route("/collector")
def collector():

    log = []
    files_list = []
    nonpassive = False

    conn.retrlines('LIST', callback=log.append)
    dirs = (line.rsplit(None, 1)[1] for line in log)

    if nonpassive:
        conn.set_pasv(False)

    for d in dirs:
        files_list.append(d)
    del (files_list[0:2])

    return str(files_list)


@app.route("/collector/download/<nome_arquivo>")
def download_by_name(nome_arquivo):
    nonpassive = False

    print(conn.retrlines('LIST'))

    if nonpassive:
        conn.set_pasv(False)

    return conn.retrbinary("RETR " + nome_arquivo, open(nome_arquivo, "wb").write)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')