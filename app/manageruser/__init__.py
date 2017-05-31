from flask import Blueprint

manageruser = Blueprint('manageruser',__name__)

from . import views
