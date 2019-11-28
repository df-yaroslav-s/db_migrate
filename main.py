import cx_Oracle

class db_migrate:

    def __init__(self, db_from_user, db_from_password, db_from_host, db_from_port, db_from_service_name, \
                 db_to_user, db_to_password, db_to_host, db_to_port, db_to_service_name, script):
        self.db_from_user = db_from_user
        self.db_from_password = db_from_password
        self.db_from_host = db_from_host
        self.db_from_port = db_from_port
        self.db_from_service_name = db_from_service_name

        self.db_to_user = db_to_user
        self.db_to_password = db_to_password
        self.db_to_host = db_to_host
        self.db_to_port = db_to_port
        self.db_to_service_name = db_to_service_name




    def migrate (self):
        conn_from = cx_Oracle.connect(user=self.db_from_user, password=self.db_from_password, \
                                 dsn = cx_Oracle.makedsn(self.db_from_host, self.db_from_port, \
                                                         service_name=self.db_from_service_name))

        conn_to = cx_Oracle.connect(user=self.db_to_user, password=self.db_to_password, \
                                      dsn=cx_Oracle.makedsn(self.db_to_host, self.db_to_port, \
                                                            service_name=self.db_to_service_name))

