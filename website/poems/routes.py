from flask import *
from website.static_details import *
from website.models import *

poem_bp = Blueprint('poem_bp', __name__)


@poem_bp.route('/poems')
def poems():
    return render_template('poems.html', title='Poems', poems=PoemData)


@poem_bp.route('/poem/<int:p_id>')
def poem(p_id: int):
    if not p_id or p_id > Poem.count:
        abort(404)
    p = PoemData.get_poem_by_id(p_id)
    return render_template('certificate_poem.html', title='Poem', cert=p, poem=True)
