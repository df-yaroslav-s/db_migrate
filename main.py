import cx_Oracle
import pymysql.cursors
import pandas as pd
from sqlalchemy import create_engine

class db_migrate:

    def __init__(self, db_from_user, db_from_password, db_from_host, db_from_port, db_from_service_name, \
                 db_to_user, db_to_password, db_to_host, db_to_dbname, script):
        self.db_from_user = db_from_user
        self.db_from_password = db_from_password
        self.db_from_host = db_from_host
        self.db_from_port = db_from_port
        self.db_from_service_name = db_from_service_name

        self.db_to_user = db_to_user
        self.db_to_password = db_to_password
        self.db_to_host = db_to_host
        self.db_to_dbname = db_to_dbname
        # self.db_to_port = db_to_port
        # self.db_to_service_name = db_to_service_name

        self.script = script

    def migrate(self):
        conn_from = cx_Oracle.connect(user=self.db_from_user,
                                      password=self.db_from_password,
                                      dsn=cx_Oracle.makedsn(self.db_from_host, self.db_from_port,
                                      service_name=self.db_from_service_name))

        conn_to = pymysql.connect(host='localhost',
                        user=self.db_to_user,
                        password=self.db_to_password,
                        db=self.db_to_dbname,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)


        query = conn_from.cursor().execute(self.script)

        df_table = pd.read_sql(self.script, con=conn_from)

        sqlEngine = create_engine('mysql+pymysql://'+self.db_to_user+':'+self.db_to_password+'@'+self.db_to_host+'/'+self.db_to_dbname)
        dbConnection = sqlEngine.connect()

        frame = df_table.to_sql('tbl3', dbConnection, if_exists='fail')

'''
        with conn_to.cursor() as cursor:
            sql = "CREATE TABLE tb2 %s"
            cursor.execute(sql, (query))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        conn_to.commit()
'''


scrpt = "select rmp.id_mp from alex.r_rest_mp@alex rmp where ROWNUM <= 2"
test_object = db_migrate('df_reader', 'd3760aecfa', '91.194.17.66', '13622', 'vitaprod', 'usr', '12345678', '127.0.0.1', 'testdb', scrpt)
test_object.migrate()

