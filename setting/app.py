# For any query, contact maazsabahuddin@gmail.com
from flask import Flask
from User.db import initialize_db
from User.view import Login, ValidateJWT


app = Flask(__name__)
app.config['SECRET_KEY']='alHGkd_7j28ASDi2'
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Flask',
    'connect': False,
}

initialize_db(app)


app.add_url_rule("/login/", view_func=Login.as_view('login_view'))
app.add_url_rule("/validate/token/", view_func=ValidateJWT.as_view('validate_token'))

if __name__ == "__main__":
    app.run(debug=True)
