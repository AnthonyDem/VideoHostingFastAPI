import os

from fastapi_users.authentication import JWTStrategy

auth_backends = []

SECRET = os.environ.get("SECRET_KEY")

jwt_authentication = JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)