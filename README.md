# Database demo

This repository is a demo for database subject , Chulalongkorn University

## Requirement
* Python3.6
* MySQL

## Quick start
* run `pip3 install -r requirements.txt` to install module
* run `python3 flaskr/main.py` to run the application in PORT 8080
* **Optional** run `nodemon flaskr/main.py` instread of python3 to watch files

## API
### GET /api/medical_staff
    Get medical staff from database with / without condition  
| Query | Type | Output |
|:---:|:---:|:---:|
| None | None |Get all staffs , return an array of object |
| id | number |Get a staff which match `id` , return a single object |
| type | string |Get staffs which medical_type match `type` , return an array of object |
#### Object description
```
{
    "Address": string,
    "Birthdate": datetime string eg. "Fri, 26 Apr 1991 00:00:00 GMT",
    "Email": string,
    "First_name": string,
    "Home_tel": string,
    "Last_name": string,
    "Medical_type": 'Doctor' | 'Pharmacist' | 'Nurse',
    "Mobile_tel": string,
    "Salary": number,
    "Sex": 'Male' | 'Female',
    "Staff_ID": number
}
```
### GET /api/medical_staff/<staff_id>
    Get a medical staff that match staff_id  

### PATCH /api/medical_staff/<staff_id>
    Edit a medical staff that match staff_id  
| Body | Type | Value |
|:---:|:---:|:---:|
| sex | string | Staff sex |
| salary | number | Staff salary |
| mobile_tel | string | Staff mobile_tel |
| home_tel | string | Staff home_tel |
| address | string | Staff address |

### DELETE /api/medical_staff/<staff_id>
    Delete a medical staff that match staff_id
    **** Cannot delete because of reference from Doctor , Nurse and Pharmacist table , wait for fix **** 

### GET /api/department
    Get department from database  
| Query | Type |Output |
|:---:|:---:|:---:|
| None | None | Get all departments , return an array of object |
#### Object description
```
{
    "DepartmentName": string,
    "Location": string,
    "Manager_ID": number,
    "Manager_first_name": string,
    "Manager_last_name": string,
    "Manager_sex": 'Male' | 'Female',
    "Manager_tel": string
}
```

### POST /api/department
    Add department to database  
| Body | Type | Value |
|:---:|:---:|:---:|
| name | string | Department name |
| location | string | Department location |
| manager | number | staff_id of the manager |

### GET /api/patient
    Get patient from database with / without condition  
| Query | Type |Output |
|:---:|:---:|:---:|
| None | None | Get all patients , return an array of object |
| id | number | Get a patient which match `id` , return a single object |
#### Object description
```
{
    "Address": string,
    "Birthdate": datetime string eg. "Sun, 19 May 1985 00:00:00 GMT",
    "Parent_first_name": string,
    "Parent_last_name": string,
    "Parent_phone_number": string,
    "Patient_ID": number,
    "Patient_first_name": string,
    "Patient_last_name": string,
    "Phone_number": string,
    "Sex": 'Male' | 'Female'
}
```

### POST /api/patient

    Add a patient to the database   

| Body | Type | Value |
|:---:|:---:|:---:|
| firstname | string | Patient firstname |
| lastname | string | Patient lastname |
| sex | string | 'Male' or 'Female' |
| birthdate | string | datestring in ISO format from Date.toISOString() |
| address | string | Patient address |
| phone | string | Patient phone number |
| parent_firstname | string | Patient's parent firstname |
| parent_lastname | string | Patient's parent lastname |
| parent_phone | string | Patient's parent phone |

### GET /api/appoint
    Get appointments from database, many optional queries can be used together.
| Query | Type |Output |
|:---:|:---:|:---:|
| None | None | Get all appointments , return an array of object |
| patient_id | number(Optional) | Get appointments which match patient_id , return an array of object |
| doctor_id | number(Optional) | Get appointments which match doctor_id , return an array of object |
#### Object description
```
{
    "Appointment_date": datetime string eg. "Mon, 23 Jul 2018 13:00:00 GMT",
    "Doctor_ID": number,
    "Doctor_email": string,
    "Doctor_first_name": string,
    "Doctor_last_name": string,
    "Doctor_sex": 'Male' | 'Female',
    "Patient_ID": number,
    "Patient_first_name": string,
    "Patient_last_name": string,
    "Patient_sex": 'Male' | 'Female'
}
```
### POST /api/appoint
    Add an appointment
| Body | Type | Value |
|:---:|:---:|:---:|
| doctor_id | number | Staff_ID of the doctor |
| patient_id | number | Patient_ID |
| appoint_date | string | datetimestring in ISO format from Date.toISOString() |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
