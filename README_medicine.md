# API for medicine

### GET /api/medicine
    Get medicine from database with / without condition  
| Query | Type | Output |
|:---:|:---:|:---:|
| None | None |Get all medicine , return an array of object |
| id | number |Get a medicine which match `id` , return a single object |

#### Object description
```
{
    "Medicine_ID" : number, 
    "Medicnie_name": string,
    "Quantity": number,
    "Exp_date":  datetime string eg. "Fri, 26 Apr 1991 00:00:00 GMT"
}
```

### POST /api/medicine/
    Add a new medicine
| Body | Type | Value |
|:---:|:---:|:---:|
| name | string | medicine name |
| quantity | number | quantity of medicines |
| exp_date | datetime string | expiration date of medicine |

### GET /api/medicine/<medicine_id>
    Get a medicine that match medicine_id  

### DELETE /api/medicine/<medicine_id>
    Delete a medicine that match medicine_id

### Refill Medicine  /api/medicine/refill
    Refill a medicine
| Body | Type | Value |
|:---:|:---:|:---:|
| medicine_id | number | id of medicine |
| pharmacist_id | number | is of pharmacist |
| quantity | number | Quantity of medicine |


### POST /api/medicine/perscribe
    Perscribe a medicine to patient
| Body | Type | Value |
|:---:|:---:|:---:|
| medicine_id | number | Medicine ID |
| quantity | number | Medicine's quantity |
| doctor_id | number | Doctor ID | 
| patient_id | number | Patient ID | 
### GET /api/medicine/perscibe
    Get a persription info. (query can combine together)
| Query | Type | Output |
|:---:|:---:|:---:|
| medicine_id | number | Get all Perscription match to medicine_id, Return array of object |
| doctor_id | number | Get all Perscription match to doctor_id, Return array of object | 
| patient_id | number | Get all Perscription match to patient_id, Return array of object |

### Object Description
```
{
    'Medicine_ID': number ,
    'Patient_ID': number, 
    'Doctor_ID': number, 
    'Quantity' : number, 
    'Perscribe_date : datetime string eg. "Fri, 26 Apr 1991 00:00:00 GMT"'
}
```
