from flask import Blueprint

mhosts = Blueprint('mhosts',__name__)

from . import views
