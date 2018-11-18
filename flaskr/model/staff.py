import pymysql
from . import getConnection


def getMedicalStaff(staff_id=None , medical_type=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = "SELECT * FROM Medical_staff"
            condition = []
            if medical_type is not None:
                condition.append(f'Medical_type = "{medical_type}"')
            if staff_id is not None:
                condition.append(f'Staff_ID = {staff_id}')
            if len(condition) > 0:
                query += ' WHERE ' + ' AND '.join(condition)
            cursor.execute(query)
            if staff_id:
                result = cursor.fetchone()
            else:
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
            if sex is not None:
                query += f'Sex = "{sex}" , '
            if salary is not None:
                query += f'Salary = {salary} , '
            if mobile_tel is not None:
                query += f'Mobile_tel = "{mobile_tel}" , '
            if home_tel is not None:
                query += f'Home_tel = "{home_tel}" , '
            if firstname is not None:
                query += f'First_name = "{firstname}" , '
            if lastname is not None:
                query += f'Last_name = "{lastname}" , '
            if address is not None:
                query += f'Address = "{address}" , '
            if email is not None:
                query += f'Email = "{email}" , '
            if query == temp:
                raise ValueError('Args are invalid!')
            else:
                query = query[:-2]
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

def delete(staff_id):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = f"DELETE FROM Medical_staff WHERE Staff_ID = {staff_id}"
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def insertNurse(sex,salary,mobile_tel,firstname,lastname,home_tel,email,address,birthdate,nurse_type):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query1 = f"INSERT INTO Medical_staff (\
	        First_name,Last_name,Birthdate,Sex,Salary,Address,Medical_type,Email,Home_tel,Mobile_tel\
            ) VALUES (\
	        '{firstname}',\
            '{lastname}' , \
            '{birthdate}' , \
            '{sex}' , \
            {salary} , \
            '{address}' , \
            'Nurse' , \
            '{email}' , \
            '{home_tel}' , \
            '{mobile_tel}'\
            );"
            query2 = f" \
            insert into Nurse (\
            Nurse_ID , \
            Nurse_type\
            ) values ( \
            last_insert_id() , \
            '{nurse_type}' \
            );"
            cursor.execute(query1)
            cursor.execute(query2)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def insertDoctor(sex,salary,mobile_tel,firstname,lastname,home_tel,email,address,birthdate,doctor_type):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query1 = f"INSERT INTO Medical_staff (\
	        First_name,Last_name,Birthdate,Sex,Salary,Address,Medical_type,Email,Home_tel,Mobile_tel\
            ) VALUES (\
	        '{firstname}',\
            '{lastname}' , \
            '{birthdate}' , \
            '{sex}' , \
            {salary} , \
            '{address}' , \
            'Doctor' , \
            '{email}' , \
            '{home_tel}' , \
            '{mobile_tel}'\
            );"
            query2 = f" \
            insert into Doctor (\
            Doctor_ID , \
            Doctor_type\
            ) values ( \
            last_insert_id() , \
            '{doctor_type}' \
            );"
            cursor.execute(query1)
            cursor.execute(query2)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def insertPharmacist(sex,salary,mobile_tel,firstname,lastname,home_tel,email,address,birthdate,pharmacist_type):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query1 = f"INSERT INTO Medical_staff (\
	        First_name,Last_name,Birthdate,Sex,Salary,Address,Medical_type,Email,Home_tel,Mobile_tel\
            ) VALUES (\
	        '{firstname}',\
            '{lastname}' , \
            '{birthdate}' , \
            '{sex}' , \
            {salary} , \
            '{address}' , \
            'Pharmacist' , \
            '{email}' , \
            '{home_tel}' , \
            '{mobile_tel}'\
            );"
            query2 = f" \
            insert into Pharmacist (\
            Pharmacist_ID , \
            Pharmacist_type\
            ) values ( \
            last_insert_id() , \
            '{pharmacist_type}' \
            );"
            cursor.execute(query1)
            cursor.execute(query2)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result