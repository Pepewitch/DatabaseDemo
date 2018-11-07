import pymysql

def test():
    mysql = pymysql.connect(host='dgo.ojudge.in.th', user='dbsec33', password='123456', db='Hospital', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
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