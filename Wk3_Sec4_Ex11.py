# Create an empty list of ProMatch teams.
# Use append to add each team to the list.

name="Paul"
skill_1="Leadership"
skill_2=("Lightboard guru")
skills=[skill_1, skill_2]
print("My name is " + name + " and I am learning Python.")
print("I am skilled at " +skills[0] + " & " + skills[1])
skills.append("Python")
print("I just took David's fantistic programming workshop.")
print("Now I am skilled at: " + skills[0] + ", " + skills[1] + " & " + skills[2])