import cx_Oracle

class db_migrate:

    def __init__(self, connection_string_from, connection_string_to, script):
        self.connection_string_from = connection_string_from
        self.connection_string_to = connection_string_to
        self.script = script


    def migrate (self):


