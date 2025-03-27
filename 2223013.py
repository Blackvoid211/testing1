import pandas as pd

data={
    'student_id':[101,101,101,101,101,102,102,102,102,103,103,103,103,103,104,104,104,104,104],
    'attendance_date':['2024-03-01','2024-03-02','2024-03-03','2024-03-04','2024-03-05','2024-03-02','2024-03-03',
                       '2024-03-04','2024-03-05','2024-03-05','2024-03-06','2024-03-07','2024-03-08','2024-03-09',
                       '2024-03-01','2024-03-02','2024-03-03','2024-03-04','2024-03-05'],
    'status':['Absent','Absent','Absent','Absent','Present','Absent','Absent','Absent','Absent','Absent','Absent',
              'Absent','Absent','Absent','Present','Present','Absent','Present','Present']

}
df= pd.DataFrame(data)
df['attendance_date']=pd.to_datetime(df['attendance_date'])
df=df.sort_values(by=['student_id','attendance_date','status'])

total_absent_days=[]

for student_id, group in df.groupby('student_id'):
    group= group.reset_index(drop=True)
    absence_start_date=None
    absence_end_date=None

for i in range(1,len(group)):
    if(group['attendance_date'].iloc[i] - group['attendance_date'].iloc[i-1]).days==1:
        if absence_start_date is None:
            absence_start_date=i-1
            absence_end_date=group['attendance_date'].iloc[i-1]
    else:
        if absence_start_date is not None and i - absence_start_date>3:
            total_absent_days.append({
            'student_id':student_id,
            'absence_start_date':group['attendance_date'].iloc[absence_start_date],
            'absence_end_date':group['attendance_date'].iloc[i-1],
            'total_absent_days':i-absence_start_date
})
    if absence_start_date is not None and (len(group)- absence_start_date)>3:
        total_absent_days.append({
            'student_id': student_id,
            'absence_start_date': group['attendance_date'].iloc[absence_start_date],
            'absence_end_date': group['attendance_date'].iloc[i - 1],
            'total_absent_days': len(group) - absence_start_date})

total_df=pd.DataFrame(total_absent_days)
print(total_df)