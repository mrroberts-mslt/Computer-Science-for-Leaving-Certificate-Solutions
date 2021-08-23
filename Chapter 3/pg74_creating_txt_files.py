file = open("myFirstTextFile.txt" , "w")
#file is a variable name. Two arguments are passed into the function
#first one is the name of the file and is a .txt extension
#second one "w" refers to write to this file
#other options are "a" for append and "r" for read

file.write("Test text")
#This line writes the string "Test text" to the file
#We could include a variable here if we wanted to

file.close()
#This line closes the file. This is good practice.