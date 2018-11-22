### API for medicine

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
    "Name": string,
    "Quantity": number,
    "Exp_date":  datetime string eg. "Fri, 26 Apr 1991 00:00:00 GMT"
}
```
### GET /api/medicine/<medicine_id>
    Get a medicine that match medicine_id  


### POST /api/medicine/
    Add a new medicine
| Body | Type | Value |
|:---:|:---:|:---:|
| name | string | medicine name |
| quantity | number | quantity of medicines |
| exp_date | datetime string | expiration date of medicine |


### PATCH /api/medicine/<medicine_id> # note : Shall we allow to edit medicine??
    Edit a medicine that match medicine_id, optional key can be used together.
| Body | Type | Value |
|:---:|:---:|:---:|
| name | string (Optional) | Medicine name |
| quantity | number(Optional) | Medicine quantity |
| exp_date | string (Optional) | Staff sex | yangmaised!!


### DELETE /api/medicine/<medicine_id>
    Delete a medicine that match medicine_id

### Refill Medicine  /api/medicine/refill/
    Refill a medicine
| Body | Type | Value |
|:---:|:---:|:---:|
| medicine_name | string | Medicine name |
| quantity | number | Quantity of medicine |


### Perscibe Medicine /api/medicine/perscribe/
    Perscribe a medicine to patient
| Body | Type | Value |
|:---:|:---:|:---:|
| medicine_name | string | Medicine name |
| quantity | number | Medicine quantity |
| doctor_name | string | Doctor name | 
| patient_name | string | Patient name | 