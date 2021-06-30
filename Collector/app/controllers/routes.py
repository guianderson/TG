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

@app.route("/data/<dt_inicial>")
def data(dt_inicial):
    dia_inicial = dt_inicial[:2]
    mes_inicial = dt_inicial[2:4]
    ano_inicial = dt_inicial[4:]
    hora = []
    file = 'focos_terrama2q_'+ano_inicial+''+mes_inicial+''+dia_inicial+'_'
    for d in range(0000, 2360, 10):
        if d < 10:
            hora.append(file + "000" + str(d) + '.csv')
        elif 10 <= d <= 90:
            hora.append(file + "00" + str(d) + '.csv')
        elif 100 <= d <= 999:
            hora.append(file + "0" + str(d) + '.csv')
        else:
            hora.append(file + str(d) + '.csv')
    return str(hora)


