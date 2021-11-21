import os

from flask import Flask, render_template, request
from werkzeug.utils import redirect
from flask_basicauth import BasicAuth

application = Flask(__name__)
basic_auth = BasicAuth(application)

application.config['BASIC_AUTH_USERNAME'] = os.environ.get("BASIC_AUTH_USERNAME")
application.config['BASIC_AUTH_PASSWORD'] = os.environ.get("BASIC_AUTH_PASSWORD")


def get_url():
    app_root = os.path.dirname(os.path.abspath(__file__))
    url_text_path = os.path.join(app_root, 'url.txt')
    url_file = open(url_text_path, "r")
    url = url_file.readline()
    url_file.close()
    return url


@application.route("/")
def main():
    return redirect(get_url())


@application.route("/admin")
@basic_auth.required
def admin():
    return render_template('admin.html', url=get_url())


@application.route('/admin', methods=['POST'])
@basic_auth.required
def set_url():
    app_root = os.path.dirname(os.path.abspath(__file__))
    url_text_path = os.path.join(app_root, 'url.txt')
    url_file = open(url_text_path, "w")
    data = request.form
    url_file.write(data['tikkie'])
    url_file.close()
    return render_template('admin.html', url=get_url())
