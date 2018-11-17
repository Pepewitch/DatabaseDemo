# Database demo

This repository is a demo for database subject , Chulalongkorn University

## Requirement
* Python3.6
* MySQL

## Quick start
* run `pip3 install -r requirements.txt` to install module
* run `python3 flaskr/main.py` to run the application in PORT 8080
* Optional run `nodemon flaskr/main.py` instread of python3 to watch files

## API
### GET /api/medical_staff
#### Get medical staff from database with / without condition
| Query | Output |
|:---:|:---:|
| None | Get all staffs , return an array of object |
| id | Get a staff which match `id` , return a single object |
| type | Get staffs which medical_type match `type` , return an array of object |
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

### GET /api/department
#### Get department from database
| Query | Output |
|:---:|:---:|
| None | Get all departments , return an array of object |
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
#### Add department to database
| Form | Value |
|:---:|:---:|
| name | Department name |
| location | Department location |
| manager | staff_id of the manager |

### GET /api/patient
#### Get patient from database with / without condition
| Query | Output |
|:---:|:---:|
| None | Get all patients , return an array of object |
| id | Get a patient which match `id` , return a single object |
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


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
