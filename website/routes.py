from datetime import datetime
from flask import *
from website.static_details import *
from website.models import *

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/technical')
def technical():
    Technical.certificates.sort(key=lambda x: datetime.strptime(x.date, '%d-%m-%Y'), reverse=True)
    return render_template('technical.html', title='Technical', technical=Technical)


@main.route('/poems')
def poems():
    return render_template('poems.html', title='Poems', poems=PoemData)


# ======================== error handlers ===========================

@main.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html')


@main.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html')
