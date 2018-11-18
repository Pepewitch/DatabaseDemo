import pymysql
from . import getConnection

def insertDepartment(name , location , manager=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = ''
            if manager is not None:
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
            query = 'select  \
            DepartmentName ,\
            Location ,\
            Staff_ID as Manager_ID , \
            First_name as Manager_first_name ,\
            Last_name as Manager_last_name ,\
            Sex as Manager_sex ,\
            Mobile_tel as Manager_tel \
            from Department left join Medical_staff \
            on Department.Manager = Medical_staff.Staff_ID'
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

# TODO: Add method to edit department