import pymysql
from . import getConnection

def insertPatient(
    firstname ,
    lastname , 
    sex , 
    birthdate , 
    address , 
    phone , 
    parent_phone , 
    parent_firstname , 
    parent_lastname
):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = f'insert into Patient (\
            Patient_first_name,\
            Patient_last_name, \
            Sex, \
            Birthdate, \
            Address, \
            Phone_number, \
            Parent_phone_number, \
            Parent_first_name, \
            Parent_last_name\
            ) values (\
            "{firstname}" ,\
            "{lastname}" ,\
            "{sex}" ,\
            "{birthdate}" ,\
            "{address}" ,\
            "{phone}" ,\
            "{parent_phone}" ,\
            "{parent_firstname}" ,\
            "{parent_lastname}"\
            )'
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def getPatient(patient_id=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = 'select * from Patient'
            if patient_id is not None:
                query += f' where Patient_ID = {patient_id}'
                cursor.execute(query)
                result = cursor.fetchone()
            else:
                cursor.execute(query)
                result = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result
