import pymysql
from . import getConnection


def getMedicalStaff():
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            # Read a single record
            query = "SELECT * FROM Medical_staff"
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
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