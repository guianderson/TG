import os
from flask import render_template
from app import app
from ftplib import FTP
from datetime import date, timedelta

# TODO: Criar arquivo para armazenas as variaveis de ambiente
dir_name = '/terrama2q/TerraMA2Q_408'
ftp_adress = 'ftp.dgi.inpe.br'
user_info = ('queimadas', 'inpe_2012')

conn = FTP(ftp_adress)
conn.login(*user_info)
conn.cwd(dir_name)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


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


@app.route("/data/<dt_inicial>")
def data(dt_inicial):
    dia_inicial = dt_inicial[:2]
    mes_inicial = dt_inicial[2:4]
    ano_inicial = dt_inicial[4:]
    file = 'focos_terrama2q_' + ano_inicial + '' + mes_inicial + '' + dia_inicial + '_'
    full_file = []

    nonpassive = False
    if nonpassive:
        conn.set_pasv(False)

    if str(mes_inicial) == str('02') and str(dia_inicial) > str(28):
        return "<h1>Data invalida</h1>"
    else:
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

        for f in full_file:
            conn.retrbinary("RETR " + f, open(f, "wb").write)

        return "<h1>Lista de Arquivos do dia: " + dia_inicial + "/" + mes_inicial + "/" + ano_inicial + "</h1>" + str(full_file)


@app.route("/data/<dt_inicial>/<dt_final>")
def downbetwendate(dt_inicial, dt_final):
    days = []
    file_name = 'focos_terrama2q_'
    full_file_name = []

    dia_inicial = dt_inicial[:2]
    mes_inicial = dt_inicial[2:4]
    ano_inicial = dt_inicial[4:]

    dia_final = dt_final[:2]
    mes_final = dt_final[2:4]
    ano_final = dt_final[4:]

    sdate = date(int(ano_inicial), int(mes_inicial), int(dia_inicial))
    edate = date(int(ano_final), int(mes_final), int(dia_final))
    delta = edate - sdate

    for i in range(delta.days + 1):
        days.append(sdate + timedelta(days=i))

    for day in days:
        if day.month < 10 and day.day < 10:
            for d in range(0, 60, 10):
                if d < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_000"
                                          + str(d) + '.csv')
                elif 10 <= d <= 90:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_00"
                                          + str(d) + '.csv')
        for d in range(100, 160, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" +
                                  str(d) + '.csv')
        for d in range(200, 260, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" +
                                  str(d) + '.csv')
        for d in range(300, 360, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(400, 460, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(500, 560, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(600, 660, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(700, 760, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(800, 860, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(900, 960, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_0" + str(d)
                                  + '.csv')
        for d in range(1000, 1060, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1100, 1160, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1200, 1260, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1300, 1360, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1400, 1460, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1500, 1560, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1600, 1660, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1700, 1760, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1800, 1860, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(1900, 1960, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(2000, 2060, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(2100, 2160, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(2200, 2260, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')
        for d in range(2300, 2360, 10):
            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + "_" + str(d)
                                  + '.csv')

    return str(full_file_name)
