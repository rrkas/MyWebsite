import secrets


class Config:
    SECRET_KEY = secrets.token_hex(8)
    UPLOAD_FOLDER = 'static/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
