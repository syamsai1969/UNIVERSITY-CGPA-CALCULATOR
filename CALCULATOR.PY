import os


def display_title_bar():
    os.system('clear')

    terminal_width = os.get_terminal_size().columns
    message = "UNIVERSITY CGPA CALCULATOR"
    print( ((6+len(message))*"-").center(terminal_width))
    print(message.center(terminal_width))
    print( ((6+len(message))*"-").center(terminal_width))
   


def quick_cgpa():
    os.system('clear')
    
    print("""Enter the SGPAs for each semester separated by spaces and hit Enter.


              
    
           """)
    
    sgpas = [float(x) for x in input().split()]
             
    total_no_of_semesters = len(sgpas)


    
    sum = 0.0
    for i in range(len(sgpas)):
        sum = sum + sgpas[i]

    print(sum)
    cgpa = sum/total_no_of_semesters
    print("You entered {} SGPAs. They were:" .format(total_no_of_semesters))
    for i in sgpas:
        print(i)
    
    print("\n\nThe final CGPA is {}".format(cgpa))


def quick_sgpa():
    os.system('clear')
    print("""For each subject of the semester:
    Enter the subject name, credits, the gradepoint secured by the student in one line separated by commas and hit enter:
    For example, if the subject name is 'Business Commmunication' and the credits of the subject is 3 credits and the gradepoint secured by the student is 9, then enter:

    Business Communication,3,9
    
    
    """)
    user_input = ''
    subjects = []
    credits = []
    scores = []
    print("\n\nEnter the subject name, credits of that subject, and the gradepoint secured by the student, separated by commas. To quit, press q and hit Enter:")
    while user_input not in ['q', 'none']: 
        user_input = input()
        
        if user_input not in ['q', 'none']:
            input_list = user_input.split(',')
            """
            print(input_list)
            """
           
            subjects.append(input_list[0])
            
            credits.append( int( input_list[1].strip() ) )
            scores.append( int( input_list[2].strip() ) )
           
            """ 
            print("Subjects -> ", end="")
            print(subjects)
            print("Credits -> ", end="")
            print(credits)
            print("Scores -> ", end="")
            print(scores)
            """
        elif user_input == 'none':
            break
        elif user_input == 'q':
            return
     
    len_subjects = len(subjects)
    len_credits = len(credits)
    len_scores = len(scores)

    sum = 0 
    credit_sum = 0
    for x in range(len_credits):
        sum = sum + (credits[x]*scores[x])
    
    for x in range(len_credits):
        credit_sum = credit_sum + credits[x]
    
    sgpaa = sum / credit_sum  
   
    big_padding = len(max(subjects, key=len)) 
    if big_padding <= len("SUBJECT NAME"): 
        big_padding = len("SUBJECT NAME") + 8
    other_padding = 15 + len("Total Credits -") 

   
    print("\n\n\n")
    print("Complete SGPA calculation")
    print("SUBJECT NAME".center(big_padding, " ") + "|" + "CREDITS".center(other_padding, " ") + "|" + "GRADE".center(other_padding, " ") )
    print( ("-"*big_padding) + "+" + "-"*other_padding + "+" + "-"*other_padding )
    for i in range(len(subjects)):
        print( subjects[i].center(big_padding, " ") + "|" + str(credits[i]).center(other_padding, " ") + "|" + str(scores[i]).center(other_padding, " ") )
    print( ("-"*big_padding) + "+" + "-"*other_padding + "+" + "-"*other_padding )
    print( " ".center(big_padding, " ") + "|" + ("Total Credits -" + " " + str(credit_sum)).center(other_padding, " ") )
    


   
    print("\n\n")
    
    print("SGPA is {}" .format(sgpaa))
    
    

    



display_title_bar()
choice = ''
while choice != 'q':    

    print("""\n\n\n
               [1] QUICK CGPA Calculation. You need to enter the SGPAs for all semesters.
               [2] QUICK SGPA Calculation. You need to enter the credits and the grade secured for each subject in the semester.
               [q] Quit the program. 
            """)
    
    choice = input("\n What do you choose?\n")
    if choice == '1':
        print("You selected QUICK CGPA")
        quick_cgpa()
    elif choice == '2':
        
        print("QUICK SGPA")
        quick_sgpa()
    elif choice == 'q':
        print("Goodbye!")
    else:
        print("Sorry!. I could not understand that input")