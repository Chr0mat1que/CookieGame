scenes = []
def add_scene(tag, description, a, a_next, b, b_next, c, c_next):
    scene_info = {
        "tag": tag, # This tag is derrived from the choices required to get there, e.g. "0aba" for "A -> B -> A"
        "description": description, # This is the text providing the information relevant to the questions
        "a": a, # The first question or answer
        "a_next": a_next, # The tag linked to ^
        "b": b, # The second question or answer
        "b_next": b_next, # The tag linked to ^
        "c": c, # The third question or answer
        "c_next": c_next, # The tag linked to ^
    }
    scenes.append(scene_info)

def init_scenes(): # Add each possible scene here, one by one. Yes this sucks. No i can't think of a better way.
    add_scene("0",
              "You walk into the house,you have been hired to find our who broke into the family house,to the second you walk in you notice all everyone screaming at each other, you don't like getting involed.You ask where the owners of the house are, they ignore you. Then the littlest one (couldn't be above 12) comes up to you and says 'are you blind? they obviously aren't here.' You get angry but dont show it, your their private detective after all, what do you say next?",
              "Do you know where they went?",
              "0a",
              "How old are you kid?",
              "0b",
              "Then can YOU take me to the crime scene.",
              "0c")

init_scenes()
