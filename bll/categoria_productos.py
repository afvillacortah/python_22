from dal.db import Db
def listar():
    sql = 'SELECT "codigo" , "categoria" FROM "Categorias_productos" ORDER BY "codigo";'
    result = Db.consulta_db(sql)
    return result