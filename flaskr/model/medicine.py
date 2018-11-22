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
    
            if firstname is not None:
                query += f'Name = "{name}" , '

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
	        Name,Quantity,Exp_date\
            ) VALUES (\
	        '{name}',\
            '{quantity}' , \
            '{exp_date}' , \
            );"
            cursor.execute(query1)
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result

def refillMedicine(medicine_id, pharmacist_id,quantity,date):
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
            '{date}', \
            );"
            cursor.execute(query1)
            #Todo : update in medecine table
            # Date my get from system date time
            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result


def perscribeMedicine(doctor_id, patient_id,medicine_id, quantity ,date):
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
            '{date}', \
            '{quantity}', \
            );"
            cursor.execute(query1)
            #Todo : update in medecine table ???

            mysql.commit()
    except Exception as e:
        print (e)
    finally:
        mysql.close()
    return result



