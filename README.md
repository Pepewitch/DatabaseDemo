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
| None | get all staff , return array of object |
| id | get staff which match `id` , return single object |
| type | get staff which medical_type match `type` , return array of object |
##### Object description
```
{
    "Address": string,
    "Birthdate": date format string eg. "Fri, 26 Apr 1991 00:00:00 GMT",
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
