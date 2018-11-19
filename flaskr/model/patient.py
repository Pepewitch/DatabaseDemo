import pymysql
from . import getConnection
from functools import reduce

def reduceAllergy(prev , curr):
    if isinstance(prev['Allergy_name'],str):
        prev['Allergy_name'] = [prev['Allergy_name']]
    prev['Allergy_name'].append(curr['Allergy_name'])
    return prev

def insertPatient(
    firstname ,
    lastname , 
    sex , 
    birthdate , 
    address , 
    phone , 
    parent_phone , 
    parent_firstname , 
    parent_lastname ,
    allergy = None
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
            if allergy is not None:
                query = 'insert into Allergy (Allergy_name , Patient_ID) values '
                query += ' , '.join(
                    map(lambda x: f'("{x}",last_insert_id())' , allergy)
                )
                cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def getPatient(patient_id=None):
    result = None
    if patient_id is not None:
        mysql = getConnection()
        try:
            with mysql.cursor() as cursor:
                query = f'select * from Patient left join Allergy \
                on Patient.Patient_ID = Allergy.Patient_ID \
                where Patient_ID = {patient_id}'
                cursor.execute(query)
                res = cursor.fetchall()
                if len(res) > 0:
                    result = reduce(reduceAllergy , res)
        except Exception as e:
            print (e)
        finally:
            mysql.close()
    else:
        mysql = getConnection()
        patients = None
        allergies = None
        try:
            with mysql.cursor() as cursor:
                query = f'select * from Patient'
                cursor.execute(query)
                patients = cursor.fetchall()
                for i in patients:
                    i['Allergy_name'] = []
                query = f'select * from Allergy'
                cursor.execute(query)
                allergies = cursor.fetchall()
                for i in allergies:
                    for j in patients:
                        if j['Patient_ID'] == i['Patient_ID']:
                            j['Allergy_name'].append(i['Allergy_name'])
                result = patients
        except Exception as e:
            print (e)
        finally:
            mysql.close()
    return result