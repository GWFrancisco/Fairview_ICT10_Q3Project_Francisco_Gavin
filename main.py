from pyscript import display
from js import document

# countdown for thecharacter requirement 
def checkUsername():
   
    username = document.getElementById("username").value
    countdown_div = document.getElementById("countdown-username")
    # this to calculate remoaining characters neededd
    remaining = 5 - len(username)
    
    if remaining > 0:
        countdown_div.textContent = f"{remaining} more characters needed"
    else:
        countdown_div.textContent = "requirement met"

#  creation and validation
def create_account(event):
    # get username and password inputs 
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    # Get the output 
    output = document.getElementById("output1")
    
    output.innerHTML = ""

    # checks if username or password is empty
    if username == "" or password == "":
        display("make sure all fields aren't empty", target="output1")
        return

    # validate username length
    user_length = len(username)
    if user_length < 7:
        userremain = 7 - user_length
        output.innerHTML = f'Username requires {userremain} more characters'
        return

    # Validate password length 
    pass_length = len(password)
    if pass_length < 10:
        passremain = 10 - pass_length
        output.innerHTML = f'Password requires {passremain} more characters'
        return
    
    # Check that password contains both letters and numbers
    letter = any(c.isalpha() for c in password)
    number = any(c.isdigit() for c in password) 
    if not letter or not number:
        output.innerHTML = 'Password must contain at least one letter and one number'
        return  
    
    output.innerHTML = 'Account created'




from pyscript import display
from js import document

intramsteams = { #intrams teams assigned to each section
    "emerald": "RED BULLDOGS",
    "sapphire": "BLUE BEARS",
    "topaz": "YELLOW TIGERS",
    "ruby": "GREEN HORNETS",
    "jade": "YELLOW HORNETS",
}


def check(e=None): #conditioning, without this wont work at all, if data inputted by user matches whatever below, it will result in the result below
    reg_yes = document.getElementById("REGSITERAPPROVED").checked
    reg_no = document.getElementById("REIGSTERNAH").checked
    registration = "yes" if reg_yes else "no" if reg_no else ""


    med_yes = document.getElementById("medicalyes").checked
    med_no = document.getElementById("medicalno").checked
    medical = "yes" if med_yes else "no" if med_no else ""

 
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value.lower()


    document.getElementById("output").innerHTML = ""

    if registration == "" or medical == "" or grade == "" or section == "": #if nothing inputted, it will say please complete all fields
        display("Please complete all fields first!", target="output")
        return
 
    if registration != "yes": #situational still, either which yes or no on the two selections, it will result with either must register or must be cleared
        display("You must register first to be eligible for a team", target="output")
        return
    if medical != "yes":#situational still, either which yes or no on the two selections, it will result with either must register or must be cleared
        display("You must get cleared first to be eligible for a team", target="output")
        return


    team = intramsteams.get(section, None) #the result, if successfully eligible it will present your intrams team, if not, it will show error and prompts user to try again
    if team:
        display(f"Congratulations! You are part of the {team}, hooray!", target="output") #part of the team if eligible and corrct inputs
    else:
        display("Error! try again!", target="output") 
