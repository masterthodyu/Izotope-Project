#Anthony Hoang & Quinn Roberts
#MINI PROJECT w/ BONUS
#12/2/2018
#Python 3.6.7

#Import library
import math
import time
import matplotlib.pyplot as plt

#Main System
def main():
    try:#Try to trap errors
        #Variables
        Isotope = '' 
        a = 0 #Counter for while loop
        A0 = 0.0 # initial activity
        mass = 0.0
        percent = 0.0
        life = 0.0 #half life
        constant = 0.693 # constant decay
        disposal = 37.00 # disposal constant
        final = 0.0 #final activity level
        days = 0.0 # Final day
        safe = 0.0 # Safe activity level
        counter = 1 # day counter
        time_in_seconds = 0.0 #BONUS
        DAY_LIST = [] 
        VALUE_LIST = []
        DAYCOUNTER = 0

        #Choose Isotope
        while a != 1:
            Isotope = (input("What isotope do you want to use? "+"\nYour options are Chronium(Cr) and Phosphorus(Ph)"+"\nPlease type your answer as one of the options in ()"))
            Isotope = Isotope.lower()
            if Isotope == 'cr':
                life = 27.7
                a = 1
                Isotope = 'Chronium'
            elif Isotope == 'ph':
                life = 14.3
                a = 1
                Isotope = 'Phosphorus'
            else:
                print("You spelled it wrong, try again")#Prevents program from crashing due to wrong input

        #Get inputs
        A0 = float(input("What is the initial activity or A0 in kBq? "))
        mass = float(input("What is the mass in Kg? "))
        percent = float(input("What is the percent of radioactive isotope present? "))
        time_in_seconds = float(input("What's the rate you'd like the data to be displayed?"))#BONUS

        #Process
        days = days_to_safe_decay_level(disposal,constant,mass,A0,life,percent)
        safe = Safe_Activity_Level(A0,life,constant,days)
        wait_function(time_in_seconds)#BONUS

        #State final day and level
        print("\nIt'll take",format(days, '0.2f'),"days to reach a safe activity level of",format(safe, '0.2f'))

        #Display new activity
        wait_function(time_in_seconds)#BONUS
        final = new_isotope_activity(constant, life, A0)
        print("Day ", counter, " ", format(final, '0.2f'))
        A0 = final
        
        #Display from day 1 to day
        while (counter < days and final > safe):
            wait_function(time_in_seconds)#BONUS
            final = new_isotope_activity(constant,life,A0)
            DAYCOUNTER = counter
            counter += 1
            DATA = A0
            A0 = final
            print("Day ",counter," ",format(final,'0.2f'))
            VALUE_LIST.append(DATA)#data value list
            DAY_LIST.append(DAYCOUNTER)#Day value list

        #Graph
        plt.xlabel('Days')
        plt.ylabel('Radioactive level(Bq)')
        plt.title('Radioactive Isotope Decay')
        plt.plot(DAY_LIST,VALUE_LIST,marker = '*',color='red',label = 'Radioactive level each day')
        plt.legend(loc='upper right')
        plt.show()

    #Exceptions
    except IndexError:#Trap list errors
        print("Something is wrong with the list.\nStopping program.")
    except ValueError:#Traps non-numbnerical errors
        print("Non-numerical value was detected.\nStopping program.")
    except:#Any errors I don't catch
        print("Looks like you gotta check your code again.\nStopping program.")

#Calculate the safe day
def days_to_safe_decay_level(disposal,constant,mass,A0,life,percent):
    percent /= 100
    mass *= percent
    days = (-1.0 * (life/constant)) * (math.log(disposal / (A0/mass)))
    return days

#Calculate the safe level
def Safe_Activity_Level(A0,life,constant,days):
    safe = A0 * math.exp(-1.0 * (constant * days / life))
    return safe

#Calculate the new isotope level
def new_isotope_activity(constant,life,A0):
    final = A0 * math.exp(-1.0 * (constant/life))
    return final

#BONUS time freezer
def wait_function(time_in_seconds):
    time.sleep(time_in_seconds)

main()#Close main
