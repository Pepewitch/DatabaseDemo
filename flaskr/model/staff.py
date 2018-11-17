import pymysql
from . import getConnection


def getMedicalStaff(medical_type=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = "SELECT * FROM Medical_staff"
            if medical_type != None:
                query += f' WHERE Medical_type = "{medical_type}"'
            cursor.execute(query)
            result = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def test():
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Medical_staff` where `Email` = %s"
            cursor.execute(sql, ('aqover@hotmail.com',))
            result = cursor.fetchone()
            print(result)
    except Exception as e:
        print (e)
    finally:
        mysql.close()
        return result