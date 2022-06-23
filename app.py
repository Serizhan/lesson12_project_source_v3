from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
from functions import search_post
from functions import load_post
from functions import is_filename_allowed
import logging

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/search')
def search_page():
    logging.basicConfig(filename="./static/basic_search.log", encoding="utf-8", level=logging.INFO)
    search = request.args['s']
    result = search_post(search)
    return render_template('post_list.html', search=search, result=result)


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_upload():
    picture = request.files.get("picture")
    filename = picture.filename
    if is_filename_allowed(filename):
        picture.save(f"./uploads/{filename}")
        content = request.form["content"]
        post = {'pic': f"./uploads/{filename}", 'content': content}
        load_post(post)
        return render_template('post_uploaded.html', filename=filename, content=content)
    else:
        extension = filename.split(".")[-1]
        logging.basicConfig(filename="./static/basic_picture.log", encoding="utf-8", level=logging.INFO)
        return f"Тип файлов {extension} не поддерживается"


@app.route("/post", methods=["POST"])
def page_post_form():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

