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

def edit(
    staff_id , 
    sex=None , 
    salary=None , 
    mobile_tel=None , 
    firstname=None , 
    lastname=None , 
    home_tel=None , 
    email=None , 
    address=None
):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            temp = 'UPDATE Medical_staff SET '
            query = temp
            if sex:
                query += f'Sex = {sex} , '
            if salary:
                query += f'Salary = {salary} , '
            if mobile_tel:
                query += f'Mobile_tel = {mobile_tel} , '
            if home_tel:
                query += f'Home_tel = {home_tel} , '
            if firstname:
                query += f'First_name = {firstname} , '
            if lastname:
                query += f'Last_name = {lastname} , '
            if address:
                query += f'Address = {address} , '
            if email:
                query += f'Email = {email} , '
            if query == temp:
                raise ValueError('Args are invalid!')
            else:
                query += f' WHERE Staff_ID = {staff_id}'
            cursor.execute(query)
            mysql.commit()
    except ValueError as e:
        result = e
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def delete(id):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = "DELETE FROM Medical_staff WHERE Staff_ID = {id}"
            cursor.execute(query)
            mysql.commit()
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