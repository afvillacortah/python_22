from dal.db import Db

def listar():
    sql = 'SELECT "id" , "tipo" FROM "Roles" ORDER BY "id";'
    result = Db.consulta_db(sql)
    return result