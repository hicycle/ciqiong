import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Flask Config """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hehe cai bu dao'
    SQLAICHEMY_COMMIT_ON_TEARDOWN = True
    CIQIONG_MAIL_SUBJECT_PREFIX = '[词穷]'
    CIQIONG_MAIL_SENDER = '小词 <admin@ciqiong.com>'
    CIQIONG_ADMIN = os.environ.get('CIQIONG_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 578
    MAIL_USE_TLS = True
    MAIL_USER = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLAICHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI') or 'mysql://root:root@localhost/ciqiongDev'


class TestConfig(Config):
    TESTING = True
    SQLAICHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI') or 'mysql://root:root@localhost/ciqiongTest'


class ProductionConfig(Config):
    SQLAICHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI') or 'mysql://root:root@localhost/ciqiong'


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig}
