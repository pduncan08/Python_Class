# Lists - Exercise 3

# Python indexing starts at 0. This will come up whenever you
# have items in a list format, so always remember to ask for
# 1 less than whatt you want!

John_Skills=["Python", "Communicateon", "Low Salary Request", 1000]
print(John_Skills)

Applicants=[["John", "Python"],["Geoff", "Doesn't Know Python"]]
print(Applicants)

# Create Lists of Lists
heights=[["Jenny",61], ["Alexus",70],["Sam",67], ["Grace",64],["vik",68]]
ages=[["Aaron",15],["Dhruti",16]]
print(heights[2][1])
print(ages[0])

# You can use zip to create a new list

names=["Jenny", "Alexus", "Samuel", "Grace"]
skills=["Python", "R", "NOTHING","Python"]
names_and_skills=zip(names, skills)
print(names_and_skills)