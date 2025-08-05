

from turtle import *
import random
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
#defining the function to draw the shape based on the number given by the user
def move_turtle(sides,answer): #this line explains what two variables are needed for the function "move_turtle"
  angle = (180*sides-360)/sides #calculates the amount of angles compared to the amount of question or sides. i.e, 5 questions means 5 side, means 
  for i in range(answer):
    forward(60) #this and the next line draws the sides in turtle
    right(180-angle)

 
sides = int(input("question", "How many questions do you want to answer, (1-10):"))
#this centers turtle starting position 
penup()
right(90)
forward(50)
pendown()
#code adjusts for difficulty, giving two extra lines to start if level one or one extra line for level two
levels = int(input("question", "Difficulty level, (3 is the easiest, 1 the hardest):"))
initialmove = levels-1
move_turtle(sides,initialmove)

  
for i in range(sides-initialmove):
  #choice is a function that randomly chooses from a list
  q = random.choice(quiz_data)
  #if q.get, which is the answer, when lowercase is equal to the input the player gives, it is correct
  if q.get("answer").lower() == input("question", q.get("question")).lower():
    print("Correct! congradulations!")
    move_turtle(sides,1)
  else:
    print("Incorrect... Try again with the next question.")
  quiz_data.remove(q)
  
  
write("Congradulations!! You completed the game, play again?")
mainloop()