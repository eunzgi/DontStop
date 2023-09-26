from pybo import QuestionForm
from flask import Blueprint, render_template, url_for

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template('question/question_form.html', form=form)
