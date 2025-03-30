import pandas as pd
def createDataframe(student_data) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=["student_id","age"])