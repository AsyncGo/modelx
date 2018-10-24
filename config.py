import os


class Config(object):
	"""基础配置类"""
	pass


class DevConfig(Config):
	"""开发配置类"""
	DEBUG = True
	# MySQL connection
	DB_URI = {
		'feature' : 'mysql+pymysql://root:root@127.0.0.1:3306/feature?charset=utf8',
		'strategy': 'mysql+pymysql://root:root@127.0.0.1:3306/strategy??charset=utf8'
	}
	pass


class TestConfig(Config):
	"""测试配置类"""
	pass


class ProdConfig(Config):
	"""生产配置类"""
	pass


config = {
	'dev'     : DevConfig,
	'test'    : TestConfig,
	'prod'    : ProdConfig,
	'default' : DevConfig
}