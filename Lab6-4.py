"""
Create a Python file named lab_6-4

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a list of 3 subjects that you have studied at Prep and store it as a variable.
Use a method to add a fourth subject you have studied to the end of the list.
Use a method to return the index of one of the subjects in your list.
Order the subjects alphabetically using a method.
Use a method to make a copy of this list and store it in a different variable.
Use a method to order this second list in reverse alphabetical order.
"""
#Alsir Elsheikh 11/8/2023

# My list is math, science, and history
my_subjects = ["Math", "Science", "History"]
my_subjects.append("English")
subject_index = my_subjects.index("Science")
my_subjects.sort()
copied_subjects = my_subjects.copy()
#This will make them print reverse
copied_subjects.sort(reverse=True)
print("Original List of Subjects:", my_subjects)
print("Index of 'Science' in the list:", subject_index)
print("Alphabetically Ordered List:", my_subjects)
print("Reversed Alphabetical Order List:", copied_subjects)

