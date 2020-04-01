from functools import wraps

from flask.views import View
from flask_api import status
from flask import jsonify, request
from werkzeug.security import generate_password_hash
from .model import Users
import uuid, datetime, jwt


def token_required(f):

    @wraps(f)
    def decorator(*args, **kwargs):

        token = request.get_json()['token'] # for postman
        # token = request.args.get('token') # for browser
        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            from setting.app import app
            # Checking whether the token matches our app secret key or not.
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)

    return decorator


class Login(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        try:
            data = request.get_json()
            # hashed_password = generate_password_hash(data['password'], method='sha256')
            # user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False).save()

            from setting.app import app
            # You can also add the time validity.
            token = jwt.encode({'data': data}, app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({
                'status': status.HTTP_200_OK,
                # 'id': str(user.id),
                'token': token.decode('UTF-8')
            })

        except Exception as e:
            return jsonify({
                'message': str(e),
            })


class ValidateJWT(View):

    @token_required
    def dispatch_request(self):
        return jsonify({'message': 'Validated'})
