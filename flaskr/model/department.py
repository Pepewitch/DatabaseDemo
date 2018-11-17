import pymysql
from . import getConnection

def insertDepartment(name , location , manager=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            # Read a single record
            query = ''
            if manager:
                query = f'insert into Department (\
                Department.DepartmentName , \
                Department.Location , \
                Department.Manager\
                ) values (\
                {name} , \
                {location} , \
                {manager}\
                );'
            else:
                query = f'insert into Department (\
                Department.DepartmentName , \
                Department.Location\
                ) values (\
                "{name}" , \
                "{location}"\
                );'
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def getDepartment():
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = 'select * from Department'
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result
