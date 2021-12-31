from flask import *
from website.details import *

technical_project = Blueprint("technical_project", __name__)


@technical_project.route("/technical")
def technical():
    technical_obj = Technical()
    return render_template("technical.html", title="Technical", technical=technical_obj)


@technical_project.route("/certificate/<int:c_id>")
def certificate(c_id: int):
    technical_obj = Technical()
    if not c_id or c_id > len(technical_obj.certificates):
        abort(404)
    cert = technical_obj.certificates[c_id - 1]
    return render_template(
        "certificate_poem.html", title="Certificate", cert=cert, poem=False
    )


@technical_project.route("/projects")
def projects():
    projects_obj = Projects()
    return render_template(
        "projects.html", title="Projects", projects=projects_obj.projects
    )
