import numpy as np

student_ids = [
    "S001", "S002", "S003", "S004", "S005",
    "S006", "S007", "S008", "S009", "S010",
    "S011", "S012", "S013", "S014", "S015",
    "S016", "S017", "S018", "S019", "S020"
]

student_names = [
    "Mahad", "Abdullah", "Asad", "Meer", "Hasnain",
    "Fatima", "Saba", "Asad", "Hammad", "Noor",
    "Maryam", "Zain", "Heer", "Saad", "Iqra",
    "Taha", "Laiba", "Abdullah", "Arslan", "Omer"
]

subjects = [
    "Math",
    "English",
    "Physics",
    "Chemistry",
    "Computer"
]

marks = np.array([
    [97, 98, 98, 99, 99],
    [65, 70, 68, 72, 75],
    [95, 92, 90, 96, 94],
    [40, 45, 90, 50, 42],
    [78, 80, 82, 76, 79],
    [55, 60, 58, 62, 57],
    [88, 85, 91, 90, 87],
    [30, 35, 40, 45, 38],
    [72, 74, 70, 68, 75],
    [98, 96, 97, 95, 99],
    [81, 79, 83, 85, 80],
    [60, 65, 62, 58, 64],
    [89, 90, 92, 88, 91],
    [47, 50, 52, 48, 49],
    [76, 78, 80, 82, 79],
    [66, 64, 68, 70, 65],
    [93, 95, 94, 92, 96],
    [58, 55, 60, 62, 57],
    [84, 86, 88, 85, 87],
    [39, 41, 37, 40, 38]
])

for i in range(len(student_ids)):
    print(f"{student_ids[i]} - {student_names[i]}")
    for j in range(len(subjects)):
        print(f"   {subjects[j]} : {marks[i][j]}")
    print()


student_average = np.mean(marks, axis=1)
print("Average Marks Per Student")
for i in range(len(student_ids)):
    print(f"{student_ids[i]} - {student_names[i]} : {student_average[i]:.2f}")


subject_average = np.mean(marks, axis=0)
print("Average Marks Per Subject")
for i in range(len(subjects)):
    print(f"{subjects[i]} : {subject_average[i]:.2f}")


highest_marks_student=np.argmax(student_average)
print(f"Student with Highest Average: {student_ids[highest_marks_student]} - {student_names[highest_marks_student]} : {student_average[highest_marks_student]:.2f}")



lowest_marks_student=np.argmin(student_average)
print(f"Student with Lowest Average: {student_ids[lowest_marks_student]} - {student_names[lowest_marks_student]} : {student_average[lowest_marks_student]:.2f}")


failed = np.any(marks < 40, axis=1)
print("Failed Students")
for i in range(len(student_ids)):
    if failed[i]:
        print(student_ids[i], "-", student_names[i], "-", marks[i])


class_average = np.mean(student_average)
print(f"Class Average: {class_average:.2f}")





df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["CGPA"] = pd.to_numeric(df["CGPA"], errors="coerce")
df["Attendance (%)"] = pd.to_numeric(df["Attendance (%)"], errors="coerce")

df = df.rename(columns={"Name": "Names"})

df = df[(df["CGPA"] >= 0) & (df["CGPA"] <= 4.0)]

df = df[(df["Age"] >= 16) & (df["Age"] <= 30)]

df.to_excel("cleaned_students.xlsx", index=False)

print(df)