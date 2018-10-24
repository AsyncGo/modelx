# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Float, Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMTEXT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class RuleZmxyFea(Base):
    __tablename__ = 'rule_zmxy_fea'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    serial_id = Column(INTEGER(11), nullable=False, unique=True, server_default=text("'0'"))
    zm_score = Column(INTEGER(11), nullable=False, server_default=text("'-9999999'"))
    feature_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

