from database.DB_connect import DBConnect
from model.country import Country
from model.contiguity import Contiguity

class DAO:
    @staticmethod
    def getAllNodes(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT co.CCode, co.StateAbb, co.StateNme 
                   FROM country co, contiguity c 
                   WHERE c.year <= %s AND c.conttype = 1 
                   AND (c.state1no = co.CCode OR c.state2no = co.CCode)"""
        cursor.execute(query, (anno,))
        res = [Country(row["CCode"], row["StateAbb"], row["StateNme"]) for row in cursor]
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllEdges(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT state1no, state2no, year, dyad 
                   FROM contiguity 
                   WHERE year <= %s AND conttype = 1 AND state1no < state2no"""
        cursor.execute(query, (anno,))
        res = [Contiguity(row["state1no"], row["state2no"], row["year"], row["dyad"]) for row in cursor]
        cursor.close()
        cnx.close()
        return res