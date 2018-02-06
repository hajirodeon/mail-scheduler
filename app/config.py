import os


class Config(object):
    """Default configuration options."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    BCRYPT_LOG_ROUNDS = 15
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'add-your-random-key-here'

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_USER = os.environ.get('DB_ENV_USER', 'postgres')
    POSTGRES_PASS = os.environ.get('DB_ENV_PASS', 'postgres')
    POSTGRES_DB = 'postgres'

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    ) or 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'your-mandrill-username'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'your mandrill-password'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'your@default-mail.com'

    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    RQ_REDIS_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    RQ_ASYNC = True
    RQ_SCHEDULER_INTERVAL = 10


class ProductionConfig(Config):
    """Production configuration options."""

    DEBUG = False


class StagingConfig(Config):
    """Staging configuration options."""

    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Development configuration options."""

    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    RQ_SCHEDULER_INTERVAL = 1


class TestingConfig(Config):
    """TESTING configuration options."""

    TESTING = True
    WTF_CSRF_ENABLED = False
