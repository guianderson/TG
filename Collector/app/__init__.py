from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Este import fica em baixo, diferente da estrutura padrão, pois,
# precisa do módulo app instanciado
from app.controllers import routes


