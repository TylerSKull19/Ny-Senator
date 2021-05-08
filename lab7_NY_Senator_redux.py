'''
CSC101 Lab 7
Part 1: Senator for NY Qualifications
Tyler Smith
10/7/2020
'''

def is_eligible_for_NY_Senator(age, citizenship, residency):
   result = age >= 30 and citizenship >= 9 and residency == "New York"
   return result 

def main():

   print("Do you meet the qualifications to become US senator for New York State?")
   
   
   age = int(input("how old are you? "))
   citizenship = int(input("how long have you been a U.S. citizen? ")) 
   residency = input("In what state do you reside? ")
   
   
   if is_eligible_for_NY_Senator(age, citizenship, residency): 
      print("You meet the qualifications to be a US Senator for New York state!")
   else:
      print("Sorry, you cannot be a Senator for New York state.")
        
        
        
main()