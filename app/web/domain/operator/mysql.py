#coding=utf-8
import os
import sys
sys.path.append("../")
sys.path.append("../../../../")
from config import config
from entity import feature, strategy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

class MysqlOperator:
    engines = {}

    def __init__(self):
        pass

    @staticmethod
    def initPool(env = 'dev'):
        if MysqlOperator.engines.__len__() > 0 :
            return
        uris = config[env].DB_URI;
        if uris.__len__() <= 0:
            return

        for keyn in uris.keys():
            # print(uris[keyn])
            MysqlOperator.engines[keyn] = create_engine(uris[keyn], echo=True)
        #print(MysqlOperator.engines)

    @staticmethod
    def getSession(type = 'feature'):
        if MysqlOperator.engines.__len__() <= 0:
            MysqlOperator.initPool(os.getenv('FLASK_CONFIG') or 'default')
        # todo,增加存在判断
        engine = MysqlOperator.engines[type]
        print(engine)
        Session = sessionmaker(bind=engine)
        return Session()

    @staticmethod
    def execute(sql):
        pass

    @staticmethod
    def insert():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

if __name__ == '__main__':
    MysqlOperator.initPool('dev')
    session = MysqlOperator.getSession('feature')
    #print(session)
    print(feature.RuleZmxyFea)
    #zmxys = session.query(feature.RuleZmxyFea).from_statement(text("SELECT * FROM rule_zmxy_fea where id=:id")).params(id=1).all()
    zmxys = session.execute("SELECT * FROM rule_zmxy_fea where id=1").first()
    print(zmxys)



