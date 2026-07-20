import pandas as pd
df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv")
print(f"Original DataSheet:\n{df}\n")

while True:
    print("*******************************************************MENU**********************************************************")
    print("Press 1 for Data Cleaning")
    print("Press 2 for Data Processing")
    print("Press 3 to Exit")

    choice = input("Enter your choice: ")

    if choice == "3":
        print("Exiting the program.")
        break

    if choice == "1":
        print("****************************************************Data Cleaning***************************************************")
        print("Press 1 for removing duplicate rows")
        print("Press 2 for removing rows with missing Name or CGPA")
        print("Press 3 for changing data types of columns")
        print("Press 4 for renaming columns")
        print("Press 5 for removing rows with invalid CGPA or Age values")

        process_choice = input("Enter your choice: ")

        if process_choice == "1":
            Row_removed = df[df.duplicated()]
            if Row_removed.empty:
                print("No duplicate rows found.")
            else:
                print("The following duplicate rows are removed:")
                print(Row_removed)
            df = df.drop_duplicates()
            print(f"\nDataSheet after removing duplicate rows:\n{df}\n")
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "2":
            Rows_to_remove = df[df["Name"].isna() | df["CGPA"].isna()]
            if Rows_to_remove.empty:
                print("No rows with missing Name or CGPA found.")
            else:
                for index in Rows_to_remove.index:
                    print(f"Row {index + 1} is removed because Name or CGPA is missing.")
            df = df.drop(Rows_to_remove.index)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "3":
            print("Changing data types of columns:")
            print("Before:")
            print(df.dtypes)
            df["Age"] = df["Age"].astype(int)
            df["CGPA"] = df["CGPA"].astype(float)
            df["Attendance"] = df["Attendance"].astype(int)
            print("\nAfter:")
            print(df.dtypes)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)  

        elif process_choice == "4":
            print("Renaming columns:")
            print("Before:")
            print(df.columns)
            input_name=input("Enter the new name for the 'Name' column: ")
            df = df.rename(columns={"Name": input_name})
            print("\nAfter:")
            print(df.columns)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "5":
            print("Removing rows with invalid CGPA or Age values:")
            print("Before:")
            print(df)

            invalid_cgpa = df[(df["CGPA"] < 0) | (df["CGPA"] > 4.0)]
            if invalid_cgpa.empty:
                print("No invalid CGPA values found.")
            else:
                print("The following rows have invalid CGPA and is removed:")
                print(invalid_cgpa)
                df = df.drop(invalid_cgpa.index)

            invalid_age = df[(df["Age"] < 16) | (df["Age"] > 30)]
            if invalid_age.empty:
                print("No invalid Age values found.")
            else:
                print("The following rows have invalid Age and is removed:")
                print(invalid_age)
                df = df.drop(invalid_age.index)

            print(f"\nDataSheet after removing invalid CGPA and Age values:\n{df}\n")
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        else:
            print("Invalid choice. Please select a valid option.")



    if choice == "2":
        print("*******************************************************DATA PROCESSING***********************************************************")
        print("Press 1 for Top 5 Students based on CGPA")
        print("Press 2 for Sorting DataSheet by CGPA in descending order")
        print("Press 3 for Filtering Students with Attendance >= 75%")
        print("Press 4 for Displaying Students after department")
        print("Press 5 for Displaying Students with highest and lowest attendance")
        print("Press 6 for adding a new column for Grade based on CGPA")

        process_choice = input("Enter your choice: ")

        if process_choice == "1":
            Top_5_students = df.nlargest(5, "CGPA")
            print("Top 5 Students based on CGPA:")
            print(Top_5_students)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "2":
            Sorting_by_CGPA = df.sort_values(by="CGPA", ascending=False)
            print("\nDataSheet sorted by CGPA in descending order:")
            print(Sorting_by_CGPA)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)
        

        elif process_choice == "3":
            Filter_by_Attendance = df[df["Attendance"] <= 75]
            print("\nStudents with low Attendance are: ")
            print(Filter_by_Attendance)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "4":
            print("\nDisplaying Students after department:")
            Departments = df["Department"].unique()
            for dept in Departments:
                print(f"\nDepartment: {dept}")
                print(df[df["Department"] == dept])
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "5":
            Highest_Attendance = df[df["Attendance"] == df["Attendance"].max()]
            Lowest_Attendance = df[df["Attendance"] == df["Attendance"].min()]
            print("\nStudents with Highest Attendance:")
            print(Highest_Attendance)
            print("\nStudents with Lowest Attendance:")
            print(Lowest_Attendance)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)

        elif process_choice == "6":
            def assign_grade(cgpa):
                if cgpa >= 3.5:
                    return "A+"
                elif cgpa >= 3.0:
                    return "A"
                elif cgpa >= 2.5:
                    return "B"
                elif cgpa >= 2.0:
                    return "C"
                elif cgpa >= 1.0:
                    return "D"
                else:
                    return "F"

            df["Grade"] = df["CGPA"].apply(assign_grade)
            print("\nDataSheet with Grade column added:")
            print(df)
            df.to_csv(r"C:\Users\Hp\OneDrive\Desktop\Python codes\Data2.csv", index=False)  

        else:
            print("Invalid choice. Please select a valid option.")

