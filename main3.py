from pyscript import document #type: ignore
import random

def check(event):
    # Get values from the DOM
    registered = document.getElementById('registered-yes').checked
    medical = document.getElementById('medical-yes').checked
    grade_val = document.getElementById('grade').value
    section = document.getElementById('section').value
    
    # Simple validation for the dropdowns
    if not grade_val or not section:
        document.getElementById('result').innerHTML = '<div class="alert alert-warning">Please select both Grade and Section.</div>'
        return

    grade = int(grade_val)
    
    # Process eligibility
    result_div = document.getElementById('result')
    result_div.innerHTML = check_eligibility(registered, medical, grade, section)

#This part of the code is to process your team if you are eligible.
#Each intramural team has its own image and its own section assigned to it as well.
def check_eligibility(registered, medical, grade, section):
    # remove team_images dictionary since we no longer show images
    if registered and medical and 7 <= grade <= 10:
        team_dict = {
            # updated assignments per user request
            "Emerald": "Red Bulldogs",
            "Ruby": "Green Hornets",
            "Sapphire": "Yellow Tigers",
            "Topaz": "Blue Bears",
            "Jade": "Blue Bears"  # still defaults to Blue Bears
        }
        
        # Get team or pick a random one if not in list
        team = team_dict.get(section, random.choice(list(team_dict.values())))

       #This part of the code is to check if you are eligible. 
        return f"""
        <div class="alert alert-success">
            <strong>Success!</strong> You are eligible. <br>
            Your assigned team is: <strong>{team}</strong>
        </div>
        """
    #This part of the code is to check if you are not eligible.
    else:
        errors = []
        if not registered: errors.append("You must register online.")
        if not medical: errors.append("You need medical clearance.")
        if not (7 <= grade <= 10): errors.append("Only Grades 7-10 are eligible.")

    #It also includes the error messages if you are not eligible.        
        error_items = "".join([f"<li>{err}</li>" for err in errors])
        return f"""
        <div class="alert alert-danger">
            <strong>Not Eligible:</strong>
            <ul class="mb-0">{error_items}</ul>
        </div>
        """