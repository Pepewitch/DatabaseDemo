import { Sex } from '../enum/Sex';
import { Medical_type } from '../enum/Medical_type';

export default interface MedicalStaff {
  Staff_ID: number;
  First_name: string;
  Last_name: string;
  Birthdate: Date;
  Sex: Sex;
  Salary: number;
  Address: string;
  Medical_type: Medical_type;
  Email: string;
  Home_tel: string;
  Mobile_tel: string;
  Start_hiring_date: Date;
  Stop_hiring_date: Date;
}
