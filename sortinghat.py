gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print ("The Sorting Hat Quiz")

print ("Q1. Do you like 1. Dawn or 2. Dusk?")
answer = int(input("Enter 1 or 2  "))

if answer == 1:
  gryffindor =+ 1 
  ravenclaw =+ 1
elif answer == 2:
  slytherin =+ 1
  hufflepuff =+ 1
else:
  print ("Wrong input")

print ("Q2. When I'm dead, I want people to remember me as:")
print ("1. The Good")
print ("2. The Great")
print ("3. The Wise")
print ("4.The Bold")

answer2 = int(input("Enter 1-4  "))

if answer2 == 1:
  hufflepuff =+ 2
elif answer == 2: 
  slytherin =+ 2
elif answer == 3:  
  ravenclaw =+ 2
elif answer == 4:
  gryffindor =+ 2
else:
  print ("wrong input")

print ("Q3 What kind of instrument most pleases your ear?")
print ("1. The Violin")
print ("2. The Trumpet")
print ("3. The piano")
print ("4. The drum")

answer3 = int(input("Enter 1-4 "))

if answer3 == 1:
  slytherin =+ 4
elif answer3 == 2:
  hufflepuff =+ 4
elif answer3 == 3:
  ravenclaw =+ 4
elif answer3 == 4:
  gryffindor =+ 4
else:
  print ("wrong input")  

print ("Gryffindor: " , gryffindor)
print ("Slytherin: " , slytherin)
print ("Hufflepuff: " , hufflepuff)
print ("Ravenclaw: " , ravenclaw)

total_points = max(gryffindor, slytherin, hufflepuff, ravenclaw)

if gryffindor == total_points:
  print ("You are a Gryffindor!")
elif slytherin == total_points:
  print ("You are a Slytherin!")
elif hufflepuff == total_points:    
  print ("You are a Hufflepuff!")
elif ravenclaw == total_points:
  print ("You are a Ravenclaw!")  