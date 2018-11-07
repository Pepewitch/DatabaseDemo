import MedicalStaff from 'MedicalStaff';

export interface Doctor extends Partial<MedicalStaff> {
  Doctor_ID: number;
  Doctor_type: string;
}
