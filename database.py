from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import json

# config_file = r'C:\projects\myapi\config.json'  # Raw 문자열로 표시
# config = json.loads(open(config_file).read())
# DB = config["DB"]
# DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

DB_URL = 'mysql+pymysql://admin:adversarial23@database-1.ctgb77tye88l.ap-northeast-2.rds.amazonaws.com:3306/mydb'


ENGINE = create_engine(
    DB_URL
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
