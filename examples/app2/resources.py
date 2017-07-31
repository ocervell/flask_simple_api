from flask_flash.core import CRUD
from models import *

class User(CRUD):
    model = UserModel
    schema = UserSchema

class Permission(CRUD):
    model = PermissionModel
    schema = PermissionSchema
