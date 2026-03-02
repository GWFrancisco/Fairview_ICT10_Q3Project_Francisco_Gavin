from pyscript import display
from js import document

# countdown for character requirements 
def checkUsername():
    username = document.getElementById("username").value
    countdown_div = document.getElementById("countdown-username")
    remaining = 5 - len(username)
    if remaining > 0:
        countdown_div.textContent = f"{remaining} more characters needed"
    else:
        countdown_div.textContent = "requirement met"

# creation and validation
def create_account(event):
    # gets username and password inputs 
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    # Gets output 
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
    
    # validate password length
    pass_length = len(password)
    if pass_length < 10:
        passremain = 10 - pass_length
        output.innerHTML = f'Password requires {passremain} more characters'
        return
    
    # checks password if it contains both letters and numbers
    letter = any(c.isalpha() for c in password)
    number = any(c.isdigit() for c in password) 
    if not letter or not number:
        output.innerHTML = 'Password must contain at least one letter and one number'
        return  
    output.innerHTML = 'Account created'




from pyscript import display
from js import document

# intrams teams assigned to each section
intramsteams = {
    "emerald": "RED BULLDOGS",
    "sapphire": "BLUE BEARS",
    "topaz": "YELLOW TIGERS",
    "ruby": "GREEN HORNETS",
    "jade": "YELLOW HORNETS",
}

# conditioning, without this wont it work, if data input by user matches, it will result in the result below
def check(e=None):
    reg_yes = document.getElementById("REGSITERAPPROVED").checked
    reg_no = document.getElementById("REIGSTERNAH").checked
    registration = "yes" if reg_yes else "no" if reg_no else ""


    med_yes = document.getElementById("medicalyes").checked
    med_no = document.getElementById("medicalno").checked
    medical = "yes" if med_yes else "no" if med_no else ""

 
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value.lower()


    document.getElementById("output").innerHTML = ""

    # if nothing is inputted, it will say please complete all fields
    if registration == "" or medical == "" or grade == "" or section == "":
        display("Please complete all fields first!", target="output")
        return
 
    # situational, either yes or no on two selections, it will result with either must register or must be cleared
    if registration != "yes": 
        display("You must register first to be eligible for a team", target="output")
        return
    if medical != "yes":
        display("You must get cleared first to be eligible for a team", target="output")
        return

    # the result, if successfully eligible it will present your intrams team, if not, it will show error and prompts to try again
    team = intramsteams.get(section, None)

    #part of the team if eligible and corrct inputs
    if team:
        display(f"Congratulations! You are part of the {team}, hooray!", target="output") 
    else:
        display("Error! try again!", target="output")


# Players list display
all_players = [
    "Jairo Agudo",
    "Naser Al Hazmi", 
    "Mikko Alaiza",
    "Matthew Banaag",
    "Emille Barcelona",
    "Cyrene Brion",
    "Miguel Buo",
    "Lian Castro",
    "Shia Cruz",
    "KC Del Prado",
    "Gianna Entrada",
    "Gavin Francisco",
    "Adrian Gavina",
    "Xylee Goyenechea",
    "Sofia Guevarra",
    "Alexander Janayan",
    "Jabez Libutan",
    "Arabella Lubo",
    "Luisa Manuel",
    "Janine Mariposque",
    "Rycob Pagtalunan",
    "Lucas Reyes",
    "Fateh Singh",
    "Tyronne Subaan",
    "Audrey Tan",
    "Alexandra Vargas",
    "James Zaldivar"
]

def show_players(e):
    # Get the container where the player list will be displayed
    container = document.getElementById("players-grid")
    
    # Create HTML for the player list
    html = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px;">'
    # Loop through each name in the player list
    for name in all_players:
        # For each player, create a card div with their name inside
        html += f'<div class="player-card"><p>{name}</p></div>'
    html += '</div>'
    
    # Insert the generated HTML into the page
    container.innerHTML = html 
