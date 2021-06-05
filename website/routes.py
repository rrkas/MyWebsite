import os
from datetime import datetime
from flask import *
from website.static_details import *
from website.models import *

main = Blueprint('main', __name__)


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html', title='About', details=PersonalDetails)


@main.route('/technical')
def technical():
    return render_template('technical.html', title='Technical', technical=Technical)


@main.route('/certificate/<int:c_id>')
def certificate(c_id: int):
    if not c_id or c_id > len(Technical.certificates):
        abort(404)
    cert = Technical.get_certificates()[c_id - 1]
    return render_template('certificate_poem.html', title='Certificate', cert=cert, poem=False)


@main.route('/projects')
def projects():
    p = Projects.get_projects()
    return render_template('projects.html', title='Projects', projects=p)


@main.route('/poems')
def poems():
    return render_template('poems.html', title='Poems', poems=PoemData)


@main.route('/poem/<int:p_id>')
def poem(p_id: int):
    if not p_id or p_id > Poem.count:
        abort(404)
    p = PoemData.get_poem_by_id(p_id)
    return render_template('certificate_poem.html', title='Poem', cert=p, poem=True)


@main.route('/cv')
def cv():
    return render_template('cv.html', title='CV', url=PersonalDetails.cv_url)

# ======================== error handlers ===========================

@main.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html')


@main.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html')
