from DbConnector import DbConector

class MySQLdbConnector(DbConector):
    def __init__(self, ConnectionString):
        super().__init__(ConnectionString)
    def Connect(self):
        return "#Connection MySql"