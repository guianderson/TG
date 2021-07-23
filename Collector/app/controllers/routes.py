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
    global files_list
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

@app.route("/collector/teste/<ini>/<dia_fim>")
def download_teste(ini, dia_fim):
    new_file_list = []

    dia_ini = ini[:2]
    mes_ini = ini[2:4]
    ano_ini = ini[4:]
    full_dia = 'focos_terrama2q_' + ano_ini + mes_ini + dia_ini + '_0000.csv'
    for f in files_list:
        new_file_list.append(f)
    return full_dia


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

    del_itens = [
        'focos_terrama2q_20210308_1550.csv', 'focos_terrama2q_20210308_1600.csv',
        'focos_terrama2q_20210308_1610.csv', 'focos_terrama2q_20210308_1630.csv',
        'focos_terrama2q_20210308_1640.csv', 'focos_terrama2q_20210308_1710.csv',
        'focos_terrama2q_20210308_1730.csv', 'focos_terrama2q_20210308_1740.csv',
        'focos_terrama2q_20210308_1820.csv', 'focos_terrama2q_20210308_1830.csv',
        'focos_terrama2q_20210301_1650.csv', 'focos_terrama2q_20210301_1720.csv',
        'focos_terrama2q_20210301_1730.csv', 'focos_terrama2q_20210301_1740.csv',
        'focos_terrama2q_20210301_1750.csv', 'focos_terrama2q_20210301_1810.csv',
        'focos_terrama2q_20210301_1820.csv', 'focos_terrama2q_20210301_1830.csv',
        'focos_terrama2q_20210301_1900.csv', 'focos_terrama2q_20210301_1910.csv',
        'focos_terrama2q_20210301_1920.csv', 'focos_terrama2q_20210301_1930.csv',
        'focos_terrama2q_20210301_2030.csv', 'focos_terrama2q_20210301_2040.csv',
        'focos_terrama2q_20210301_2050.csv', 'focos_terrama2q_20210301_2120.csv',
        'focos_terrama2q_20210301_2130.csv', 'focos_terrama2q_20210301_2140.csv',
        'focos_terrama2q_20210308_1750.csv', 'focos_terrama2q_20210308_1840.csv',
        'focos_terrama2q_20210308_1850.csv', 'focos_terrama2q_20210420_1640.csv',
        'focos_terrama2q_20210420_1650.csv', 'focos_terrama2q_20210420_1830.csv',
        'focos_terrama2q_20210420_1850.csv', 'focos_terrama2q_20210420_1920.csv',
        'focos_terrama2q_20210420_1930.csv', 'focos_terrama2q_20210420_1940.csv',
        'focos_terrama2q_20210420_1950.csv', 'focos_terrama2q_20210420_2040.csv',
        'focos_terrama2q_20210420_2050.csv', 'focos_terrama2q_20210420_2330.csv',
        'focos_terrama2q_20210421_0020.csv', 'focos_terrama2q_20210421_0040.csv',
        'focos_terrama2q_20210421_0050.csv', 'focos_terrama2q_20210421_0110.csv',
        'focos_terrama2q_20210421_0130.csv', 'focos_terrama2q_20210421_0140.csv',
        'focos_terrama2q_20210421_0150.csv', 'focos_terrama2q_20210421_0210.csv',
        'focos_terrama2q_20210421_0220.csv', 'focos_terrama2q_20210421_0230.csv',
        'focos_terrama2q_20210421_0240.csv', 'focos_terrama2q_20210421_0250.csv',
        'focos_terrama2q_20210421_0300.csv', 'focos_terrama2q_20210421_0310.csv',
        'focos_terrama2q_20210421_0320.csv', 'focos_terrama2q_20210421_0330.csv',
        'focos_terrama2q_20210421_0350.csv', 'focos_terrama2q_20210421_0400.csv',
        'focos_terrama2q_20210421_0410.csv', 'focos_terrama2q_20210421_0420.csv',
        'focos_terrama2q_20210421_0440.csv', 'focos_terrama2q_20210421_0450.csv',
        'focos_terrama2q_20210421_0520.csv', 'focos_terrama2q_20210421_0530.csv',
        'focos_terrama2q_20210421_0540.csv', 'focos_terrama2q_20210421_0550.csv',
        'focos_terrama2q_20210421_0610.csv', 'focos_terrama2q_20210421_0620.csv',
        'focos_terrama2q_20210421_1040.csv', 'focos_terrama2q_20210421_1050.csv',
        'focos_terrama2q_20210421_1110.csv', 'focos_terrama2q_20210421_1120.csv',
        'focos_terrama2q_20210421_1130.csv', 'focos_terrama2q_20210421_1140.csv',
        'focos_terrama2q_20210421_1150.csv', 'focos_terrama2q_20210421_1210.csv',
        'focos_terrama2q_20210421_1220.csv', 'focos_terrama2q_20210421_1230.csv',
        'focos_terrama2q_20210421_1240.csv', 'focos_terrama2q_20210421_1250.csv',
        'focos_terrama2q_20210421_1310.csv', 'focos_terrama2q_20210421_1320.csv',
        'focos_terrama2q_20210421_1330.csv', 'focos_terrama2q_20210421_1340.csv',
        'focos_terrama2q_20210421_1350.csv', 'focos_terrama2q_20210421_1410.csv',
        'focos_terrama2q_20210421_1420.csv', 'focos_terrama2q_20210421_1430.csv',
        'focos_terrama2q_20210421_1440.csv', 'focos_terrama2q_20210421_1450.csv',
        'focos_terrama2q_20210421_1500.csv', 'focos_terrama2q_20210421_1510.csv',
        'focos_terrama2q_20210421_1520.csv', 'focos_terrama2q_20210421_1530.csv',
        'focos_terrama2q_20210421_1540.csv', 'focos_terrama2q_20210421_1550.csv',
        'focos_terrama2q_20210421_1610.csv', 'focos_terrama2q_20210421_1620.csv',
        'focos_terrama2q_20210421_1630.csv', 'focos_terrama2q_20210421_1640.csv',
        'focos_terrama2q_20210421_1650.csv', 'focos_terrama2q_20210421_1700.csv',
        'focos_terrama2q_20210421_1710.csv', 'focos_terrama2q_20210421_1720.csv',
        'focos_terrama2q_20210421_1730.csv', 'focos_terrama2q_20210421_1740.csv',
        'focos_terrama2q_20210421_1750.csv', 'focos_terrama2q_20210421_1810.csv',
        'focos_terrama2q_20210421_1820.csv', 'focos_terrama2q_20210421_1930.csv',
        'focos_terrama2q_20210421_1940.csv', 'focos_terrama2q_20210421_1950.csv',
        'focos_terrama2q_20210421_2030.csv', 'focos_terrama2q_20210421_2040.csv',
        'focos_terrama2q_20210421_2050.csv', 'focos_terrama2q_20210421_2020.csv',
        'focos_terrama2q_20210421_2120.csv', 'focos_terrama2q_20210421_2130.csv',
        'focos_terrama2q_20210421_2140.csv', 'focos_terrama2q_20210421_2150.csv',
        'focos_terrama2q_20210421_2220.csv', 'focos_terrama2q_20210421_2230.csv',
        'focos_terrama2q_20210421_2250.csv', 'focos_terrama2q_20210421_2300.csv',
        'focos_terrama2q_20210421_2310.csv', 'focos_terrama2q_20210421_2320.csv',
        'focos_terrama2q_20210421_2330.csv', 'focos_terrama2q_20210421_2340.csv',
        'focos_terrama2q_20210421_2350.csv', 'focos_terrama2q_20210422_0020.csv',
        'focos_terrama2q_20210422_0030.csv', 'focos_terrama2q_20210422_0040.csv',
        'focos_terrama2q_20210422_0050.csv', 'focos_terrama2q_20210422_0110.csv',
        'focos_terrama2q_20210422_0120.csv', 'focos_terrama2q_20210422_0130.csv',
        'focos_terrama2q_20210422_0140.csv', 'focos_terrama2q_20210422_0150.csv',
        'focos_terrama2q_20210422_0210.csv', 'focos_terrama2q_20210422_0220.csv',
        'focos_terrama2q_20210422_0230.csv', 'focos_terrama2q_20210422_0240.csv',
        'focos_terrama2q_20210422_0250.csv', 'focos_terrama2q_20210422_0300.csv',
        'focos_terrama2q_20210422_0310.csv', 'focos_terrama2q_20210422_0320.csv',
        'focos_terrama2q_20210422_0330.csv', 'focos_terrama2q_20210422_0340.csv',
        'focos_terrama2q_20210422_0350.csv', 'focos_terrama2q_20210422_0400.csv',
        'focos_terrama2q_20210422_0410.csv', 'focos_terrama2q_20210422_0420.csv',
        'focos_terrama2q_20210422_0430.csv', 'focos_terrama2q_20210422_0440.csv',
        'focos_terrama2q_20210422_0450.csv', 'focos_terrama2q_20210422_0500.csv',
        'focos_terrama2q_20210422_0510.csv', 'focos_terrama2q_20210422_0520.csv',
        'focos_terrama2q_20210422_0530.csv', 'focos_terrama2q_20210422_0540.csv',
        'focos_terrama2q_20210422_0550.csv', 'focos_terrama2q_20210422_0600.csv',
        'focos_terrama2q_20210422_0610.csv', 'focos_terrama2q_20210422_0620.csv',
        'focos_terrama2q_20210422_1040.csv', 'focos_terrama2q_20210422_1050.csv',
        'focos_terrama2q_20210422_1110.csv', 'focos_terrama2q_20210422_1120.csv',
        'focos_terrama2q_20210422_1130.csv', 'focos_terrama2q_20210422_1140.csv',
        'focos_terrama2q_20210422_1150.csv', 'focos_terrama2q_20210422_1200.csv',
        'focos_terrama2q_20210422_1220.csv', 'focos_terrama2q_20210422_1230.csv',
        'focos_terrama2q_20210422_1240.csv', 'focos_terrama2q_20210422_1250.csv',
        'focos_terrama2q_20210422_1300.csv', 'focos_terrama2q_20210422_1310.csv',
        'focos_terrama2q_20210422_1320.csv', 'focos_terrama2q_20210422_1330.csv',
        'focos_terrama2q_20210422_1340.csv'
    ]

    for i in range(delta.days + 1):
        days.append(sdate + timedelta(days=i))

    for day in days:
            if day.day < 10 and day.month < 10:
                for d in range(0, 60, 10):
                    if d < 10:
                        full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) +
                                              "_000" + str(d) + '.csv')
                    elif 10 <= d <= 90:
                        full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) +
                                              "_00" + str(d) + '.csv')
            if day.day < 10 and day.month >= 10:
                    for d in range(0, 60, 10):
                        if d < 10:
                            full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + "_000"
                                                  + str(d) + '.csv')
                        elif 10 <= d <= 90:
                            full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + "_00" +
                                                  str(d) + '.csv')
            if day.day > 9 and day.month < 10:
                    for d in range(0, 60, 10):
                        if d < 10:
                            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + "_000"
                                                  + str(d) + '.csv')
                        elif 10 <= d <= 90:
                            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + "_00" +
                                                  str(d) + '.csv')
            if day.day > 9 and day.month > 9:
                    for d in range(0, 60, 10):
                        if d < 10:
                            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + "_000"
                                                  + str(d) + '.csv')
                        elif 10 <= d <= 90:
                            full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + "_00" +
                                                  str(d) + '.csv')

            for d in range(100, 160, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d)
                                          + '.csv')
            for d in range(200, 260, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d) +
                                          '.csv')
            for d in range(300, 360, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d) +
                                          '.csv')
            for d in range(400, 460, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d)
                                          + '.csv')
            for d in range(500, 560, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d)
                                          + '.csv')
            for d in range(600, 660, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d) +
                                          '.csv')
            for d in range(700, 760, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d) +
                                          '.csv')
            for d in range(800, 860, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d)
                                          + '.csv')
            for d in range(900, 960, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_0'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_0' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_0' + str(d) +
                                          '.csv')
            for d in range(1000, 1060, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1100, 1160, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1200, 1260, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1300, 1360, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1400, 1460, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1500, 1560, 10):
                if day.day == 8 and day.month == 3 and d == 1550:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1600, 1660, 10):
                if (day.day == 1 and day.month == 3 and d == 1650) or (day.day == 8 and day.month == 3 and d == 1600)\
                        or (day.day == 8 and day.month == 3 and d == 1610) \
                        or (day.day == 8 and day.month == 3 and d == 1630) \
                        or (day.day == 8 and day.month == 3 and d == 1640):
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1700, 1760, 10):
                if (day.day == 1 and day.month == 3 and d == 1720) or (day.day == 1 and day.month == 3 and d == 1730)\
                        or (day.day == 1 and day.month == 3 and d == 1750) \
                        or (day.day == 8 and day.month == 3 and d == 1710)\
                        or (day.day == 8 and day.month == 3 and d == 1730)\
                        or (day.day == 8 and day.month == 3 and d == 1740):
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day == 1 and day.month == 3 and d == 1740:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 3) + '.csv')
                if day.day == 8 and day.month == 3 and d == 1750:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 2) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1800, 1860, 10):
                if (day.day == 1 and day.month == 3 and d == 1810) or (day.day == 1 and day.month == 3 and d == 1820)\
                        or (day.day == 1 and day.month == 3 and d == 1830)\
                        or (day.day == 8 and day.month == 3 and d == 1820)\
                        or (day.day == 8 and day.month == 3 and d == 1830):
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day == 8 and day.month == 3 and d == 1840:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 2) + '.csv')
                if day.day == 8 and day.month == 3 and d == 1850:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 3) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(1900, 1960, 10):
                if (day.day == 1 and day.month == 3 and d == 1900) or (day.day == 1 and day.month == 3 and d == 1910) \
                        or (day.day == 1 and day.month == 3 and d == 1920) or (day.day == 1 and day.month == 3 and
                                                                               d == 1930):
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_'
                                          + str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(2000, 2060, 10):
                if (day.day == 1 and day.month == 3 and d == 2030) or (day.day == 1 and day.month == 3 and d == 2050):
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day == 1 and day.month == 3 and d == 2040:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 2) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(2100, 2160, 10):
                if (day.day == 1 and day.month == 3 and d == 2120) or (day.day == 1 and day.month == 3 and d == 2130)\
                        or (day.day == 1 and day.month == 3 and d == 2140):
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d + 1) + '.csv')
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(2200, 2260, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')
            for d in range(2300, 2360, 10):
                if day.day < 10 and day.month < 10:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + '0' + str(day.day) + '_' +
                                          str(d) + '.csv')
                elif day.day >= 10 > day.month:
                    full_file_name.append(file_name + str(day.year) + '0' + str(day.month) + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day < 10 <= day.month:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + '0' + str(day.day) + '_' + str(d)
                                          + '.csv')
                elif day.day >= 10 and day.month >= 10:
                    full_file_name.append(file_name + str(day.year) + str(day.month) + str(day.day) + '_' + str(d) +
                                          '.csv')

                for i in full_file_name:
                    for j in del_itens:
                        if i == j:
                            full_file_name.remove(i)

    return str(full_file_name)
