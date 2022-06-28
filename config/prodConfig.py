from datetime import timedelta


class BasicConfig(object):
    # 在过期时间内关闭浏览器session仍然存在.
    SESSION_PERMANENT = True
    # 设置session过期时间为两小时.
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    SECRET_KEY = "123"


class DevelopConfig(BasicConfig):
    # 可设置本地环境变量, 也可以直接指定.
    DEBUG = True


class ProductionConfig(BasicConfig):
    DEBUG = True