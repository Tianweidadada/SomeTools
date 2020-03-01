# -*- coding:utf-8 -*-
# @Time : 2019/12/29 11:17
# @Author : TianWei
# @File : config.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(db_info):
	engine = db_info.get("ENGINE") or "sqlite"
	driver = db_info.get("DRIVER") or "sqlite"
	username = db_info.get("USERNAME") or ""
	password = db_info.get("PASSWORD") or ""
	host = db_info.get("HOST") or ""
	port = db_info.get("PORT") or ""
	database = db_info.get("DATABASE") or ""
	return "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(engine,driver,username,password,host,port,database)

class Config:
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境
class DevelopConfig(Config):
	DEBUG = True
	db_info = {
		"ENGINE":"mysql",
		"DRIVER":"pymysql",
		"HOST":"127.0.0.1",
		"PORT":"3306",
		"DATABASE":"english",
		"USERNAME":"root",
		"PASSWORD":"12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 测试环境
class TestConfig(Config):
	TESTING = True
	db_info = {
		"ENGINE": "mysql",
		"DRIVER": "pymysql",
		"HOST": "127.0.0.1",
		"PORT": "3306",
		"DATABASE": "english",
		"USERNAME": "root",
		"PASSWORD": "12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 演示环境
class StagingConfig(Config):
	db_info = {
		"ENGINE": "mysql",
		"DRIVER": "pymysql",
		"HOST": "127.0.0.1",
		"PORT": "3306",
		"DATABASE": "english",
		"USERNAME": "root",
		"PASSWORD": "12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 生产环境
class ProductConfig(Config):
	db_info = {
		"ENGINE": "mysql",
		"DRIVER": "pymysql",
		"HOST": "127.0.0.1",
		"PORT": "3306",
		"DATABASE": "english",
		"USERNAME": "root",
		"PASSWORD": "12345"
	}

	SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)



# 传入 app
envs = {
	"develop":DevelopConfig,
	"testing":TestConfig,
	"staging":StagingConfig,
	"product":ProductConfig,
	"default":DevelopConfig
}