import pymysql
from . import getConnection

def insertAppoint(doctor_id , patient_id , appoint_date):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = f'insert into Appoint (\
            Doctor_ID , Patient_ID , Appointment_date\
            ) values (\
            {doctor_id} , {patient_id} , {appoint_date}\
            )'
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def getAppoint(start=None , stop=None , id=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = 'select * from Appoint'
            # TODO: add query by id
            if start and stop:
                query += f' where Appointment_date >= "{start}" and Appointment_date <= "{stop}"'
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result
