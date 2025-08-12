from turtle import *
import random #imports the built-in "random library"



quiz_data = [#quiz data is a list of dictionaries
  { #each dictionary defines a "question" and an "answer"
    "question": "5x10x5= ",
    "answer": "250"
  },
  {
    "question": "5+9+3+5= ",
    "answer": "22"
  },
    {
    "question": "If I have 3 friends and 12 apples, how many apples do each of them get? ",
    "answer": "4"
  },
    {
    "question": "I have 12 chocolates and my friend has 2. If we divide them equally between eachother, how many do we each get? ",
    "answer": "7"
  },
    {
    "question": "I want to buy a pickle for $18 but I only have $13. How much more money do I need? ",
    "answer": "$5"
  },
    {
    "question": "There are 4 blue birds, 2 orange birds and 5 yellow birds, how many birds are there in total? ",
    "answer": "11"
  },
    {
    "question": "There are 38 people in a room. If a table holds 3 people, what is the least amount of tables do we need for all of them? ",
    "answer": "13"
  },
    {
    "question": " I have twelve oranges and 3 apples, but my friend has 14 apples and 2 oranges. In total, do we have more oranges or apples? ",
    "answer": "apples"
  },
    {
    "question": "Jamie is 12 years old and Carl is 7 years younger, how old is Carl? ",
    "answer": "5"
  },
    {
    "question": "100+50+40+50 = ",
    "answer": "240"
  },
]

correct = 0

#defining the function to draw the shape based on the number given by the user
def move_turtle(sides,answer): #this line explains what two variables are needed for the function "move_turtle"
  angle = (180*sides-360)/sides #calculates the amount of angles compared to the amount of question or sides. i.e, 5 questions means 5 side, means 
  for i in range(answer):
    forward(60) #this and the next line draws the sides in turtle and turns the turtle the predeterminded angle
    right(180-angle)

#asks user for the color used at the end of the game

while True:
  shapecol = input("What is your favourite colour?(red, orange, yellow, green, blue, purple or pink) ").strip()
  
  if shapecol.lower() in ["red", "blue", "orange", "green", "yellow", "purple", "pink"] :
    print("Aw cool!! Thats my favourite colour too!")
    break
  else:
    print("Ooh, I don't know that color? Can you enter one of the ones I have listed?")
    
    
  


sides = int(input("How many questions do you want to answer, (1-10):"))
#this centers turtle starting position 
penup()
right(90)
forward(50)
pendown()
fillcolor(shapecol)
begin_fill()
#code adjusts for difficulty, giving two extra lines to start for level one or one extra line for level two
levels = int(input("Difficulty level, (3 is the easiest, 1 the hardest):"))
initialmove = levels-1
#this calls the function, telling the turtle to draw the intialmove amount of sides
move_turtle(sides,initialmove)

  
for i in range(sides):
  #choice is a function that randomly chooses from a list
  q = random.choice(quiz_data)
  #if q.get, which is the answer, when lowercase is equal to the input the player gives, it is correct
  if q.get("answer").lower() == input(q.get("question")).lower():
    (print("Correct! congradulations!"))
    move_turtle(sides,1) #this calls the function, drawing 1 side
    correct += 1
  else:
    print("Incorrect... Try again with the next question.")
  quiz_data.remove(q) #this removes the question from the list ensuring it doesn't give the same question


if correct + initialmove >= sides:
  print("Congratulations!! You completed the game, play again?")
  end_fill()
else:
  print("Oh no, the shape is incompete! Thats ok, try again?")
mainloop()