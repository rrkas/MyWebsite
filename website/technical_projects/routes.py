from flask import *
from website.static_details import *

technical_project = Blueprint('technical_project', __name__)


@technical_project.route('/technical')
def technical():
    return render_template('technical.html', title='Technical', technical=Technical)


@technical_project.route('/certificate/<int:c_id>')
def certificate(c_id: int):
    if not c_id or c_id > len(Technical.certificates):
        abort(404)
    cert = Technical.get_certificates()[c_id - 1]
    return render_template('certificate_poem.html', title='Certificate', cert=cert, poem=False)


@technical_project.route('/projects')
def projects():
    p = Projects.get_projects()
    return render_template('projects.html', title='Projects', projects=p)
