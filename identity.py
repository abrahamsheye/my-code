students_names = input("Identify yourself: ").title()
names = ["Nathan", "Lydia", "Glory", "Abraham"]
if students_names not in names:
 print("Sorry, " + students_names + " you're not an exam enrolled student ") 
 quit()




def main():
    
    
    students_grades = int(input(" Enter your grade:"))
    if students_grades >= 90:
     print("Congratulations! You got an A1 " + students_names)
    elif students_grades >= 80:
     print("Congratulations! You got B2 " + students_names)
    elif students_grades >=70:
     print("Congralations! You got C3 " + students_names) 
    else: 
     print("oh, " + students_names + " fair result put more effort!")

             
main()        
