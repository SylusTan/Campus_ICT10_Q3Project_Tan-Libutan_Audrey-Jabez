# main2.py
from pyscript import document   # type: ignore 
# gives you access to the DOM
                               

players = [
    "Jairo Agudo", "Naser Al Hazmi", "Mikko Alaiza",
    "Matthew Banaag", "Emille Barcelona", "Cyrene Brion",
    "Miguel Buo", "Lian Castro", "Shia Cruz",
    "Karla Del Prado", "Gianna Entrada", "Gavin Francisco",
    "Adrian Gavina", "Xylee Goyenechea", "Sofia Guevarra",
    "Ioana Haberia", "Alexander Janayan", "Jabez Libutan",
    "Arabella Lubo", "Luisa Manuel", "Janine Mariposque",
    "Rycob Pagtalunan", "Lucas Reyes", "Fateh Singh",
    "Tyronne Subaan", "Audrey Tam", "Alexandra Vargas",
    "James Zaldivar"
]

def render_players():
    # grab the specific list container by id so we don't accidentally target another <ul>
    ul = document.querySelector("#players-list")
    # clear any existing children (useful if you re‑render later)
    while ul.firstChild:
        ul.removeChild(ul.firstChild)

    for i, name in enumerate(players, start=1):
        li = document.createElement("li")
        li.innerText = f"{i}. {name}"
        ul.appendChild(li)

# run on load
render_players()
