from sqlalchemy import create_engine


config = {
    'HOST': '',
    'USERNAME': '',
    'PASSWORD': '',
    'PORT': '',
    'DATABASE': '',
    'PARAMS': ''
}


DB_URL = 'mysql+pymysql://{用户名}:{密码}@{主机}:{端口号}/{数据库}?{参数}'

engine = create_engine(DB_URL.format(**config))



if __name__ == '__main__':
    conc = engine.connect()
    result = conc.execute('select 1')
    print(result.fetchone())