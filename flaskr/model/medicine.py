import pymysql
from . import getConnection


def getMedicine(medicine_id=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = "SELECT * FROM Medicine"
            condition = []
            if medicine_id is not None:
                condition.append(f'Medicine_ID = {medicine_id}')
            if len(condition) > 0:
                query += ' WHERE ' + ' AND '.join(condition)
            cursor.execute(query)
            if medicine_id:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def edit(
    medicine_id , 
    name=None , 
    quantity=None , 
    exp_date=None 
):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            temp = 'UPDATE Medecine SET '
            query = temp
    
            if name is not None:
                query += f'Medicine_Name = "{name}" , '
            if quantity is not None:
                query += f'Quantity = "{quantity}" , '
            if exp_date is not None:
                query += f'Exp_date = "{exp_date}" , '
            if query == temp:
                raise ValueError('Args are invalid!')
            else:
                query = query[:-2]
                query += f' WHERE Medicine_ID = {medicine_id}'
            cursor.execute(query)
            mysql.commit()
    except ValueError as e:
        result = e
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def delete(medicine_id):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = f"DELETE FROM Medicine WHERE Medicine_ID = {medicine_id}"
            cursor.execute(query)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def insertMedicine(name,quantity,exp_date):
    mysql = getConnection()
    result = None
    
    try:
        with mysql.cursor() as cursor:
            query1 = f"INSERT INTO Medicine (\
	        Medicine_name,Quantity,Exp_date\
            ) VALUES (\
	        '{name}',\
            '{quantity}', \
            '{exp_date}'\
            );"
            print(query1)
            cursor.execute(query1)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def refillMedicine(medicine_id, pharmacist_id,quantity): #done
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query1 = f"INSERT INTO Refill (\
	        Medicine_ID,Pharmacist_ID, Quantity,Refill_date\
            ) VALUES (\
	        '{medicine_id}',\
            '{pharmacist_id}' , \
            '{quantity}' , \
            NOW() \
            );"
            query2 = f"UPDATE Medicine SET Quantity = Quantity + {quantity}\
            WHERE Medicine_ID = {medicine_id};"
            cursor.execute(query1)
            cursor.execute(query2)
            mysql.commit()
            
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result


def perscribeMedicine(medicine_id, patient_id,doctor_id, quantity):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query1 = f"INSERT INTO Perscribe (\
	        Doctor_ID,Patient_ID,Medicine_ID, Perscribe_date, Quantity\
            ) VALUES (\
	        '{doctor_id}',\
            '{patient_id}' , \
            '{medicine_id}' , \
            NOW(), \
            '{quantity}' \
            );"
            query2 = f"UPDATE Medicine SET Quantity = Quantity - {quantity}\
            WHERE Medicine_ID = {medicine_id};"
            print(query2)
            cursor.execute(query1)
            cursor.execute(query2)
            mysql.commit()
            

    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result


def getPerscribe(medicine_id=None, patient_id=None,doctor_id=None):
    mysql = getConnection()
    result = None
    try:
        with mysql.cursor() as cursor:
            query = "SELECT * FROM Perscribe"
            condition = []
            if medicine_id is not None:
                condition.append(f'Medicine_id = "{medicine_id}"')
            if doctor_id is not None:
                condition.append(f'Doctor_ID = {doctor_id}')
            if patient_id is not None:
                condition.append(f'Patient_ID = {patient_id}')
            if len(condition) > 0:
                query += ' WHERE ' + ' AND '.join(condition)
            print(query)
            cursor.execute(query)
            # print(query)
            result = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result



