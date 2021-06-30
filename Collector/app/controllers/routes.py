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
    file = 'focos_terrama2q_' + ano_inicial + '' + mes_inicial + '' + dia_inicial + '_'
    full_file = []

    for d in range(0, 60, 10):
        if d < 10:
            full_file.append(file + "000" + str(d) + '.csv')
        elif 10 <= d <= 90:
            full_file.append(file + "00" + str(d) + '.csv')
    for d in range(100, 160, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(200, 260, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(300, 360, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(400, 460, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(500, 560, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(600, 660, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(700, 760, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(800, 860, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(900, 960, 10):
        full_file.append(file + "0" + str(d) + '.csv')
    for d in range(1000, 1060, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1100, 1160, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1200, 1260, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1300, 1360, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1400, 1460, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1500, 1560, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1600, 1660, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1700, 1760, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1800, 1860, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(1900, 1960, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(2000, 2060, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(2100, 2160, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(2200, 2260, 10):
        full_file.append(file + str(d) + '.csv')
    for d in range(2300, 2360, 10):
        full_file.append(file + str(d) + '.csv')
    return "<h1>Lista de Arquivos do dia: " +dia_inicial + "/" + mes_inicial + "/" + ano_inicial + "</h1>" + str(full_file)