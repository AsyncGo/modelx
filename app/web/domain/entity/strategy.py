# coding: utf-8
from sqlalchemy import Column, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class RiskExecuteLog(Base):
    __tablename__ = 'risk_execute_log'

    id = Column(INTEGER(10), primary_key=True)
    create_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    apply_no = Column(INTEGER(10), nullable=False, index=True)
    risk_analysis_id = Column(String(128), nullable=False, index=True, server_default=text("''"))
    input = Column(Text)
    rules = Column(Text)
    params = Column(Text)
