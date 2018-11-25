# TODO: Add method to manage treatment table
import pymysql
from . import getConnection


def insertTreatment(doctor_id , patient_id , cost, symptom):
    mysql = getConnection()
    try:
        with mysql.cursor() as cursor:
            query = f'insert into Treatment (\
            Doctor_ID , Patient_ID , Treatment_cost, Symptom\
            ) values (\
            "{doctor_id}" , "{patient_id}" , "{cost}", "{symptom}"\
            )'
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
        return False
    finally:
        mysql.close()
    
    return True

def getTreatment(patient_id, doctor_id = None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = 'select \
            Treatment.Treatment_ID\
            Treatment.Doctor_ID \
            Treatment.Patient_ID \
            Treatment.Symptom \
            Treatment.Treatment_cost \
            Medical_staff.First_name as Doctor_first_name ,\
            Medical_staff.Last_name as Doctor_last_name ,\
            Medical_staff.Sex as Doctor_sex ,\
            Medical_staff.Email as Doctor_email ,\
            Patient_first_name,\
            Patient_last_name,\
            Patient.Sex as Patient_sex \
            from Treatment \
            join Medical_staff on Treatment.Doctor_ID = Medical_staff.Staff_ID \
            join Patient on Treatment.Patient_ID = Patient.Patient_ID'
            condition = []
            condition.append(f' Treatment.Patient_ID={patient_id}')
            if doctor_id is not None:
                condition.append(f' Treatment.Doctor_ID={doctor_id}')

            if len(condition) > 0:
                query += ' WHERE ' + ' AND '.join(condition)
            cursor.execute(query)
            result = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def updateTreatment(treatment_id, patient_id = None, doctor_id = None, cost = None, symptom = None):
    mysql = getConnection()
    try:
        with mysql.cursor() as cursor:
            condition = ''
            condition += f'Patient_ID={patient_id} ,'
            condition += f'Doctor_ID={doctor_id} ,'
            if cost is not None:
                condition += f'Treatment_cost={cost} ,'
			if symptom is not None:
                condition += f'Symptom={symptom} ,'
            if len(condition) > 0:
                query = f'update Treatment set {condition[:-1]} where Treatment_ID = {treatment_id};'
                cursor.execute(query)
                mysql.commit()
    except Exception as e:
        print (e)
        return False
    finally:
        mysql.close()

    return True

def deleteTreatment(treatment_id):
	mysql = getConnection()
	try:
		with mysql.cursor() as cursor:
			query = f'delete from Treatment where Treatment_ID="{treatment_id}"'
            cursor.execute(query)
            mysql.commit()
	except Exception as e:
        print (e)
        return False
    finally:
        mysql.close()

    return True