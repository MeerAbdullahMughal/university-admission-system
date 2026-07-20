import pandas as pd

student_df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\studentsinfo.csv")
university_df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\universitiesinfo.csv")
admission_df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\AdmissionInfo.csv")

while True:

    print("********************* UNIVERSITY ADMISSION SYSTEM *********************")
    print("1. Display Student Information")
    print("2. Display University Information")
    print("3. Search Student by ID")
    print("4. Search University by ID")
    print("5. Student Admission")
    print("6. Show Admissions")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        print(student_df)

    elif choice == "2":
        print(university_df)

    elif choice == "3":

        student_id = input("Enter Student ID: ")

        if student_id in student_df["Student_ID"].values:

            result_student = student_df[student_df["Student_ID"] == student_id]
            print(result_student)
            print("Student Found.")

        else:

            print("Student not found.")

            add = input("Do you want to add this student? (yes/no): ")

            if add.lower() == "yes":

                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                age = input("Enter Age: ")
                gender = input("Enter Gender: ")
                program = input("Enter Program: ")
                semester = input("Enter Semester: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone Number: ")
                cgpa = input("Enter CGPA: ")

                new_student = {
                    "Student_ID": student_id,
                    "First_Name": first_name,
                    "Last_Name": last_name,
                    "Age": age,
                    "Gender": gender,
                    "Program": program,
                    "Semester": semester,
                    "Email": email,
                    "Phone": phone,
                    "CGPA": cgpa
                }

                student_df.loc[len(student_df)] = new_student

                student_df.to_csv(
                    r"C:\Users\Hp\OneDrive\Desktop\Python codes\studentsinfo.csv",
                    index=False
                )

                print("Student added successfully.")

            else:
                print("Student was not added.")

    elif choice == "4":

        university_ID = input("Enter University ID: ")

        if university_ID in university_df["University_ID"].values:

            result_university = university_df[university_df["University_ID"] == university_ID]
            print(result_university)
            print("University Found.")

        else:

            print("University not found.")

            add = input("Do you want to add this university? (yes/no): ")

            if add.lower() == "yes":

                university_name = input("Enter University Name: ")
                short_name = input("Enter Short Name: ")
                city = input("Enter City: ")
                province = input("Enter Province: ")
                type_uni = input("Enter Type (Public/Private): ")
                established = input("Enter Established Year: ")
                main_focus = input("Enter Main Focus: ")
                website = input("Enter Website: ")
                student_population = input("Enter Student Population: ")

                new_university = {
                    "University_ID": university_ID,
                    "University_Name": university_name,
                    "Short_Name": short_name,
                    "City": city,
                    "Province": province,
                    "Type": type_uni,
                    "Established": established,
                    "Main_Focus": main_focus,
                    "Website": website,
                    "Student_Population": student_population
                }                

                university_df.loc[len(university_df)] = new_university

                university_df.to_csv(
                r"C:\Users\Hp\OneDrive\Desktop\Python codes\universitiesinfo.csv",
                index=False
                )

                print("University added successfully.")

            else:
                print("University was not added.")
    elif choice == "5":

        admission_df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\AdmissionInfo.csv")

        student_id = input("Enter Student ID: ")

        while student_id not in student_df["Student_ID"].values:
            print("Invalid Student ID.")
            student_id = input("Enter Student ID: ")

        result_student = student_df[student_df["Student_ID"] == student_id]
        print(result_student)

        university_ID = input("\nEnter University ID: ")

        while university_ID not in university_df["University_ID"].values:
            print("Invalid University ID.")
            university_ID = input("Enter University ID: ")

        result_university = university_df[university_df["University_ID"] == university_ID]
        print(result_university)

        enroll = input("Do you want to enroll this student in this university? (yes/no): ")

        if enroll.lower() == "yes":

            print("******** PROGRAM MENU ********")
            print("1. BSAI")
            print("2. BSCS")
            print("3. BSSE")
            print("4. BSPSY")
            print("5. BSAF")

            program_choice = input("Enter Program Choice: ")

            if program_choice == "1":
                program = "BSAI"

            elif program_choice == "2":
                program = "BSCS"

            elif program_choice == "3":
                program = "BSSE"

            elif program_choice == "4":
                program = "BSPSY"

            elif program_choice == "5":
                program = "BSAF"

            else:
                print("Invalid Program Choice.")
                continue

            student_name = result_student.iloc[0]["First_Name"] + " " + result_student.iloc[0]["Last_Name"]
            university_name = result_university.iloc[0]["University_Name"]

            new_admission = {
                "Student_ID": student_id,
                "Student_Name": student_name,
                "University_ID": university_ID,
                "University_Name": university_name,
                "Program": program
            }

            admission_df.loc[len(admission_df)] = new_admission
            print("\nAdmission DataFrame:")
            print(admission_df)

            admission_df.to_csv(
                r"C:\Users\Hp\OneDrive\Desktop\Python codes\AdmissionInfo.csv",
                index=False
            )

            print("Admission Successful!")
            print(student_name, "has been admitted to", university_name, "in", program, "program.")

            print("**************************************************")
            print("          ADMISSION SUCCESSFUL")
            print("**************************************************")
            print("Student Name   :", student_name)
            print("University     :", university_name)
            print("Program        :", program)
            print(student_name, "has been admitted to", university_name, "in", program, "program.")
            print("Congratulations!")
            print("**************************************************")

        else:
            print("Admission Cancelled.")

    elif choice == "6":
        print("Showing Admissions...")
        print(admission_df)

    elif choice == "7":
        print("Thank you for using the Admission System.")
        break

    else:
        print("Invalid Choice. Please Try Again.")

   
