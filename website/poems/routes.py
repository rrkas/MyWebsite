from flask import *
from website.static_details import *

poem_bp = Blueprint("poem_bp", __name__)


@poem_bp.route("/poems")
def poems():
    poems_obj = PoemData()
    return render_template("poems.html", title="Poems", poems=poems_obj)


@poem_bp.route("/poem/<string:p_id>")
def poem(p_id):
    poem_obj = PoemData()
    if not poem_obj.get_poem_by_id(p_id):
        abort(404)
    return render_template(
        "certificate_poem.html",
        title="Poem",
        cert=poem_obj.get_poem_by_id(p_id),
        poem=True,
    )
