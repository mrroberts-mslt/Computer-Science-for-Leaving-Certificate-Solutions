'''iteration is when we instruct a computer to repeat a section of code
over and over again. This is known as a loop'''

#while loops
#very similar toan if statement...a condition must be met
counter = 0
while counter < 7:
    print (counter)
    counter += 1
print("I'm glad that loop is finished!")

#experiment with the above code, change the parameters etc.
''' a while loop must consist of
A counter = loop control variable
The word "while"
A boolean expression to state the condition
A colon
indented block of code on the line after the colon....(while clause)
Another branch of a loop otherwise you may have an infinite loop'''

#be careful that your counter is not OBOE off by one error....what does this mean??

while True:
    print ("Lets just print this forever!")
