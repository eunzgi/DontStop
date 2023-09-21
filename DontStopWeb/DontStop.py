from flask import Flask, render_template
from flask import request
from flask import session
from flask import url_for
import pymysql

# db = pymysql.connect(host='localhost', port=11245, user='RentalStart', passwd='vip0818!', db='RentalStart', charset='utf8')

# 애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8888, debug=True)

    from .DontStop import main_views
    app.register_blueprint(main_views.bp)


    
    return app


def page_not_found(e):
    return render_template('404.html'), 404
