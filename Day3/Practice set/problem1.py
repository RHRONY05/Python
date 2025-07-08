# Import date time module to get the current time
import datetime

# Take user name and tell good evening to the user

def greetings(name):
   print(f"Good evening {name}")

def letter(name):
   print(f"""
      Dear {name},
         
      You are selected!

      Date :- {datetime.date.today()}
   """)


name = input("Enter your name: ")
greetings(name)
letter(name)

# Write a letter to that user