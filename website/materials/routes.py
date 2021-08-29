from flask import *
from website.static_details import *

materials_bp = Blueprint("materials_bp", __name__)


@materials_bp.route("/materials")
def materials():
    return render_template(
        "study_material_list.html", summary=StudyMaterials.get_summary()
    )


@materials_bp.route("/materials/<std>")
def materials_std(std):
    data = StudyMaterials.get_std_data(std)
    return render_template("study_material_class.html", data=data)
