import pandas as pd
data = {
    'Name' : ['Amina', 'Brian', 'Doracs', 'Kevin'],
    'Marks' : [78, 45, 89, 55]

}
df = pd.DataFrame(data)
df.to_csv('student.csv', index=False)

print(df)
#adding csv files using pd.read_csv file reads data from from a csv file
student = pd.read_csv('student.csv')
print(student)
print(student.head(2))
print(student.tail(2))
#dataset information
print(student.info())
#stastical summary
print(student.describe())
#numbers of rows and coloumns
print(student.shape)
print(student.shape)
print(student[['Name','Marks']])
#filtering data
print(student[student['Marks'] > 50])
student['Result'] =student['Marks'].apply(
    lambda x: 'pass' if x >= 60 else 'Fail'
)
print(student)
#counting categories with value column
print(student['Result'].value_counts())
student['Marks'].apply(
    lambda x: 'pass' if x >=60 else 'Fail'
    )
print(student['Result'].value_counts())
pass_count = (student['Result'] == 'pass').sum()
total_student = len (student)
pass_rate = (pass_count / total_student) * 100
print("pass rate:", pass_rate, "%")
#sorting data
print(student.sort_values(by='Marks', ascending=False))
print(student.sort_values(by='Marks', ascending=True))
#saving a clean dataset
student.to_csv('final_student_results.csv', index=False)
print("CSV file saved succefully!")
#handling missing data
import pandas as pd
data = {
    'Name': ['Amina', 'Brian', 'Dorcas', 'Kevin'],
    'Marks': [78, None, 89, 55]
}
student = pd.DataFrame(data)
print(student)
print("checking missing values:")
print(student.isnull())
print("counting missing values:")
print(student.isnull().sum())
print("original data:")
print(df)
print("\nMissing values:")
print(df.isnull().sum())
average = df['Marks'].mean()
print(average)
df['Marks'] = df['Marks'].fillna(average)
print("\nUpdate data")
print(df)
#duplicates
import pandas as pd
data = {
    "Name": ["Amina", "Dorcas", "Brian", "Amina", "Kevin"],
    "Marks": [87, 67, 78, 87, 70],
}
df = pd.DataFrame(data)

print("Original dataset:")
print(df)

print("\nChecking duplicates:")
print(df.drop_duplicates())

print("\nNumber of duplicates:")
print(df.duplicated().sum())


print("\nRemoving duplicates:")
df = df.drop_duplicates()

print("\nClean dataset:")
print(df)

print("\nDuplicates remaining:")
print(df.duplicated().sum())
#creating a data set
import pandas as pd
data ={
    "Student_Name": ["Dori", "Chari", "Brian",],
    "Student_Marks": [78, 89, 85],
    "Studen_Age": [20, 13, 17],

}
df =pd. DataFrame(data)

print(df)

print("Original dataset:")
print(df)

df = df.rename(columns={
    "Student_Name": "Name",
    "Stusent_Marks": "Marks",
    "Student_Age": "Age"
})

print("\nRenamed dataset:")
print(df)
print("\nAverage marks per student:")

# GROUPING STUDENTS BY AGE GROUP

# Create an age group column
df["Age_Group"] = df["Studen_Age"].apply(
    lambda age: "18 and above" if age >= 18 else "Below 18"
)

print("\nDataset with Age Groups:")
print(df)

# Group data by age group and calculate average marks
age_average = df.groupby("Age_Group")["Student_Marks"].mean()

print("\nAverage Marks per Age Group:")
print(age_average)
# GROUPBY WITH MULTIPLE STATISTICS

age_summary = df.groupby('Age_Group')['Student_Marks'].agg(
    ['count', 'mean', 'max', 'min']
)

print("\nAge Group Summary:")
print(age_summary)

print("TESTING FILTERING")

print(age_summary)

high_performance = age_summary[age_summary['mean'] > 75]

print("FILTERING COMPLETED")

print(high_performance)
print(age_summary)
print(age_summary.columns)

import pandas as pd

data = {
    'Name': ['Amina', 'Brian', 'Kevin', 'Dorcas', 'Mary', 'John'],
    'Age': [20, 21, 20, 22, 21, 20],
    'Marks': [78, 90, 88, 65, 95, 82]
}

df = pd.DataFrame(data)

# Group by age and calculate multiple statistics
summary = df.groupby('Age')['Marks'].agg(
    ['count', 'mean', 'max', 'min']
)

print("GROUP SUMMARY")
print(summary)

# Filter using multiple conditions
result = summary[
    (summary['mean'] > 80) &
    (summary['max'] > 90)
]

print("\nFILTERED RESULTS")
print(result)

import pandas as pd

data = {
    'Name': ['Amina', 'Brian', 'Kevin', 'Dorcas', 'Mary'],
    'Age': [20, 21, 20, 22, 21],
    'Marks': [78, 90, 88, 65, 95],
    'Fees': [15000, 18000, 15000, 12000, 18000]
}

df = pd.DataFrame(data)

# Group by age and calculate different statistics
result = df.groupby('Age').agg({
    'Marks': ['mean', 'max'],
    'Fees': ['sum', 'mean']
})

print(result)

import pandas as pd

print("========== PANDAS FINAL PROJECT ==========")

# ==========================================
# 1. CREATE STUDENT DATASETS
# ==========================================

students = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Amina', 'Brian', 'Kevin', 'Dorcas', 'Mary'],
    'Age': [20, 21, 22, 20, 23],
    'Course': ['Statistics', 'Data Science', 'Statistics',
               'Data Science', 'Statistics']
}

df_students = pd.DataFrame(students)

marks = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Maths': [78, 85, 90, 65, 88],
    'Python': [82, 90, 85, 70, 92],
    'Excel': [75, 88, 80, 60, 85]
}

df_marks = pd.DataFrame(marks)

print("\n1. STUDENT DATA")
print(df_students)

# ==========================================
# 2. MERGING DATASETS
# ==========================================

merged = pd.merge(
    df_students,
    df_marks,
    on='Student_ID',
    how='inner'
)

print("\n2. MERGED DATA")
print(merged)

# ==========================================
# 3. JOINING DATASETS
# ==========================================

attendance = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104, 105],
    'Attendance': [90, 85, 95, 70, 88]
})

student_join = df_students.set_index('Student_ID')
attendance_join = attendance.set_index('Student_ID')

joined = student_join.join(attendance_join)

print("\n3. JOINED DATA")
print(joined)

# ==========================================
# 4. CONCATENATING DATASETS
# ==========================================

semester_one = pd.DataFrame({
    'Name': ['Amina', 'Brian', 'Kevin'],
    'Marks': [78, 85, 90]
})

semester_two = pd.DataFrame({
    'Name': ['Dorcas', 'Mary'],
    'Marks': [70, 92]
})

combined = pd.concat(
    [semester_one, semester_two],
    ignore_index=True
)

print("\n4. CONCATENATED DATA")
print(combined)

# ==========================================
# 5. PIVOT TABLE
# ==========================================

pivot = pd.pivot_table(
    merged,
    values=['Maths', 'Python', 'Excel'],
    index='Course',
    aggfunc='mean'
)

print("\n5. PIVOT TABLE")
print(pivot)

# ==========================================
# 6. CROSS TABULATION
# ==========================================

cross_tab = pd.crosstab(
    df_students['Course'],
    df_students['Age']
)

print("\n6. CROSS TABULATION")
print(cross_tab)

# ==========================================
# 7. DATE AND TIME ANALYSIS
# ==========================================

dates = pd.DataFrame({
    'Name': ['Amina', 'Brian', 'Kevin', 'Dorcas', 'Mary'],
    'Registration_Date': [
        '2026-01-10',
        '2026-02-15',
        '2026-03-20',
        '2026-04-05',
        '2026-05-12'
    ]
})

dates['Registration_Date'] = pd.to_datetime(
    dates['Registration_Date']
)

dates['Year'] = dates['Registration_Date'].dt.year
dates['Month'] = dates['Registration_Date'].dt.month
dates['Day'] = dates['Registration_Date'].dt.day

print("\n7. DATE ANALYSIS")
print(dates)

# ==========================================
# 8. ADVANCED DATA CLEANING
# ==========================================

raw_data = {
    'Name': ['Amina', 'Brian', 'Kevin', 'Dorcas', 'Amina'],
    'Marks': [78, 85, None, 70, 78],
    'Age': [20, 21, 22, 20, 20]
}

dirty_df = pd.DataFrame(raw_data)

print("\n8. ORIGINAL DATA WITH ERRORS")
print(dirty_df)

# Remove extra spaces
dirty_df['Name'] = dirty_df['Name'].str.strip()

# Fill missing marks with the average
dirty_df['Marks'] = dirty_df['Marks'].fillna(
    dirty_df['Marks'].mean()
)

# Remove duplicate records
dirty_df = dirty_df.drop_duplicates()

print("\nCLEANED DATA")
print(dirty_df)

# ==========================================
# 9. CALCULATE STUDENT AVERAGES
# ==========================================

merged['Average'] = merged[
    ['Maths', 'Python', 'Excel']
].mean(axis=1)

print("\n9. STUDENT AVERAGES")
print(merged[['Name', 'Average']])

# ==========================================
# 10. RANK STUDENTS
# ==========================================

merged['Rank'] = merged['Average'].rank(
    ascending=False,
    method='min'
)

print("\n10. STUDENT RANKING")
print(
    merged[['Name', 'Average', 'Rank']]
    .sort_values('Rank')
)

# ==========================================
# 11. FILTER TOP PERFORMERS
# ==========================================

top_students = merged[
    merged['Average'] >= 80
]

print("\n11. STUDENTS WITH AVERAGE OF 80 OR ABOVE")
print(top_students[['Name', 'Average']])

# ==========================================
# 12. SAVE FINAL DATASET TO CSV
# ========================================

# Organise final student dataset

final_df = merged[
    [
        'Student_ID',
        'Name',
        'Age',
        'Course',
        'Maths',
        'Python',
        'Excel',
        'Average',
        'Rank'
    ]
].copy()

# Sort students by rank
final_df = final_df.sort_values(
    by='Rank',
    ascending=True
)

# Round average to 2 decimal places
final_df['Average'] = final_df['Average'].round(2)

# Reset row numbering
final_df = final_df.reset_index(drop=True)

# Save organised dataset
final_df.to_csv(
    'pandas_final_student_analysis.csv',
    index=False
)

print("\nFINAL ORGANIZED STUDENT DATA")
print(final_df.to_string(index=False))

print("\nOrganized CSV saved successfully!")
import pandas as pd

df = pd.read_csv('pandas_final_student_analysis.csv')

print(df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nStudent ranking:")
print(df[['Name', 'Average', 'Rank']])




    







