from flask import Flask, render_template
from flask import request
from flask import session
from flask import url_for
import pymysql

# import config as config

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# db = pymysql.connect(host='localhost', port=11245, user='RentalStart', passwd='vip0818!', db='RentalStart', charset='utf8')

# def page_not_found(e):
#     return render_template('404.html'), 404


# 애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)

    # app.run(host='0.0.0.0', port=8888, debug=True)

    # ORM
    # db.init_app(app)
    # migrate.init_app(app, db)

    # 블루프린트
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    
    return app
