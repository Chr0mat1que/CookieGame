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
        "You walk into the house,you have been hired to find our who broke into the family house,to the second you walk in you notice all everyone screaming at each other, you don't like getting involed.You ask where the owners of the house are, thye ignore you. Then the littlest one (couldnt be above 12) comes up to you and says 'are you blind? they obviously aren't here.' You get angry but dont show it, your their private detective afterall, what do you say next?", 
        "Do you know where they went?", 
        "0a", 
        "How old are you kid?", 
        "0b", 
        "Then can YOU take me to the crime scene?", 
        "0c")

    add_scene("0a",
        "'Who knows with those two, you were supposed to be here 1 hour ago, we can't wait forever' he says. You weren't late though, you are never late. \n You appologize anyways, no point in arguing with a 12 year old. Where are your siblings? you ask nicely, wanting to start the job as soon as poosible. \n Reluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy, 'Ethan, why are you with that man and who is he?' 'Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Amy, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "TODO",
        "0ac")

init_scenes()
