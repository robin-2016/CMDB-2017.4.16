from flask import Blueprint

offhost = Blueprint('offhost',__name__)

from . import views
