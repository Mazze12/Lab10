from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query="""   select c.CCode, c.StateAbb, c.StateNme
                    from country c
        """
        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(annoMax):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct CCode, StateAbb, StateNme
                    from(	select co.CCode , co.StateAbb , co.StateNme  
		                    from contiguity c
		                    join country co on c.state1no =co.CCode 
		                    where c.`year` <= %s
		                    and c.conttype =1
		                    UNION
		                    select co.CCode , co.StateAbb , co.StateNme 
		                    from contiguity c
		                    join country co on c.state2no =co.CCode
		                    where c.`year` <= %s
		                    and c.conttype =1) t1
            """
        cursor.execute(query, (annoMax,annoMax,))

        for row in cursor:
            result.append(Country(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(annoMax, idMap):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select c.state1no as CC1, c.state2no as CC2,  c.`year` as year, c.dyad
                    from contiguity c
                    where c.`year` <=%s
                    and c.conttype =1
                """
        cursor.execute(query, (annoMax,))

        for row in cursor:
            result.append(Contiguity(idMap[row["CC1"]], idMap[row["CC2"]], row["year"], row["dyad"]))
        cursor.close()
        conn.close()
        return result








