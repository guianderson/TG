import os
from flask import render_template
from app import app
from ftplib import FTP
from datetime import date

from app.models.forms import DataForm


@app.route("/collector")
def collector():
    dir_name = '/terrama2q/TerraMA2Q_408'
    ftp_adress = 'ftp.dgi.inpe.br'
    user_info = ('queimadas', 'inpe_2012')

    conn = FTP(ftp_adress)
    conn.login(*user_info)
    conn.cwd(dir_name)

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

    return render_template('teste.html'), str(files_list)


@app.route("/")
@app.route("/index")
def download():
    return render_template('index.html')