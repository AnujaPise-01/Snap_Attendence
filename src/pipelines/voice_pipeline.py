#  Create a dictionary where:Q5
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
# depending on the operation they want to perform on the dictionary:
# 1. - Add a studentA
# 2. - Update marksB
# 3. - Search for a studentC
# 4. - Display all students and marks

# def student_management_system():
#     # Initialize an empty dictionary for student records
#     students_marks = {}

#     while True:
#         print("\n--- Student Marks Management System ---")
#         print("A. Add a student")
#         print("B. Update marks")
#         print("C. Search for a student")
#         print("D. Display all students and marks")
#         print("E. Exit")

#         # Get user choice and convert to uppercase for uniformity
#         choice = input("Choose an option (A/B/C/D/E): ").strip().upper()

#         if choice == 'A':
#             name = input("Enter student name to add: ").strip()
#             if name in students_marks:
#                 print(f"Student '{name}' already exists. Use option B to update marks.")
#             else:
#                 try:
#                     marks = int(input(f"Enter marks for {name}: "))
#                     students_marks[name] = marks
#                     print(f"Student '{name}' added successfully with {marks} marks.")
#                 except ValueError:
#                     print("Invalid input! Marks must be an integer.")

#         elif choice == 'B':
#             name = input("Enter student name to update marks: ").strip()
#             if name in students_marks:
#                 try:
#                     marks = int(input(f"Enter new marks for {name}: "))
#                     students_marks[name] = marks
#                     print(f"Marks for '{name}' updated successfully to {marks}.")
#                 except ValueError:
#                     print("Invalid input! Marks must be an integer.")
#             else:
#                 print(f"Student '{name}' not found in the records.")

#         elif choice == 'C':
#             name = input("Enter student name to search: ").strip()
#             if name in students_marks:
#                 print(f"Found! {name} scored: {students_marks[name]} marks.")
#             else:
#                 print(f"Student '{name}' not found.")

#         elif choice == 'D':
#             if not students_marks:
#                 print("No student records available.")
#             else:
#                 print("\n--- All Students and Marks ---")
#                 for name, marks in students_marks.items():
#                     print(f"Name: {name} | Marks: {marks}")
#                 print("-" * 30)

#         elif choice == 'E':
#             print("Exiting program. Goodbye!")
#             break

#         else:
#             print("Invalid choice! Please select a valid option from A, B, C, D, or E.")

# # Run the program
# if __name__ == "__main__":
#     student_management_system()
# Given a tuple of integers create
#  A tuple of all even numbers
#  A tuple of all odd numbers
class Solution:
    def createTuple(self,tup1: tuple[int]) -> tuple[int]:
        even_tup = ()
        odd_tup = ()
        for i in tup1:
            
            if i % 2 == 0:
                i = str(i)
                even_tup.__add__(i)
                return even_tup
            else:
                i = str(i)
                odd_tup.__add__(i)
                return odd_tup
s1 = Solution()
result = s1.createTuple((1,2,2,3,4,5,6,7,6,8,7,9,8,0))
print(result)
            




            










