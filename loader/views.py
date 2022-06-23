from flask import Blueprint, render_template

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/upload')
def load_page():
    return render_template('post_form.html')

