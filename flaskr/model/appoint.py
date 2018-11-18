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
            {doctor_id} , {patient_id} , "{appoint_date}"\
            )'
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def getAppoint(start=None , stop=None , patient_id=None , doctor_id=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = 'select \
            Appoint.Doctor_ID as Doctor_ID ,\
            Appoint.Patient_ID as Patient_ID ,\
            Appoint.Appointment_date as Appointment_date ,\
            Medical_staff.First_name as Doctor_first_name ,\
            Medical_staff.Last_name as Doctor_last_name ,\
            Medical_staff.Sex as Doctor_sex ,\
            Medical_staff.Email as Doctor_email ,\
            Patient_first_name,\
            Patient_last_name,\
            Patient.Sex as Patient_sex \
            from Appoint \
            join Medical_staff on Appoint.Doctor_ID = Medical_staff.Staff_ID \
            join Patient on Appoint.Patient_ID = Patient.Patient_ID'
            condition = []
            if patient_id != None:
                condition.append(f' Appoint.Patient_ID={patient_id}')
            if doctor_id != None:
                condition.append(f' Appoint.Doctor_ID={doctor_id}')
            if start != None:
                condition.append(f' Appoint.Appointment_date >= "{start}"')
            if stop != None:
                condition.append(f' Appoint.Appointment_date <= "{stop}"')
            if len(condition) > 0:
                query += ' WHERE ' + ' AND '.join(condition)
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result
