import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
  patients_with_condition = patients[patients['conditions'].str.contains(r'\bDIAB1')]
  result_df = patients_with_condition[['patient_id','patient_name','conditions']]
  return result_df
