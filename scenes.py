scenes = []
def add_scene(tag, description, a, a_next, b, b_next, c, c_next, images=None):
    scene_info = {
        "tag": tag, # This tag is derrived from the choices required to get there, e.g. "0aba" for "A -> B -> A"
        "images": images, # This is a list of image identifiers (probably by name, like amy_happy), leave empty for none
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
        "0c",
        ["amy_happy", "amy_angry"])

    add_scene("0a",
        "'Who knows with those two, you were supposed to be here 1 hour ago, we can't wait forever' he says. You weren't late though, you are never late. \nYou appologize anyways, no point in arguing with a 12 year old. Where are your siblings? you ask nicely, wanting to start the job as soon as poosible. \n\nReluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy, 'Ethan, why are you with that man and who is he?' 'Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Amy, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "TODO",
        "0ac")

    add_scene("0b",
        "'First of all my name is not kid, its Ethan, second of all, I am not a kid i'm 13 and a half. My birthday was... last week, we went to wendys and ate... pizza!' Ok...ki- Ethan, sorry about that you say, no point in arguing with a 12 year old. Can I talk to your siblings? Best to start talking to some real adults. \n\nReluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy,'Ethan, why are you with that man and who is he?" "Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Amy, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "TODO",
        "0ac")

    add_scene("0c",
        "'Crime scene? HAHAH who do you think you are batman?' he laughed 'Its just a window' Well your dad asked me to be here and you do not hire a private investigator for a broken window, so can you lead me to an adult I can speak to? you say firmly \n\nReluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy,'Ethan, why are you with that man and who is he?" "Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Amy, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "TODO",
        "0ac")

    add_scene("0aa",
        "'What are you on about? What do you need our rooms for?' One of the older boys says hastily,too hastily, You snap your neck towards him and stare 'Bedrooms are off limits' Amy says. is she trying to hide something? Probably not, no one like snooping around though. 'Is there a reason?' you ask?, 'You know what fine. I would like to talk to talk to you all 1 by 1 please'",
        "TODO",
        "0aaa",
        "TODO",
        "0aab",
        "TODO",
        "0aac")

    add_scene("0ab",
        "'No we can not, and can't you speak to us? What do you need them for let us help you.' Amy says, you sigh and look around, is there a private room? We can stay in i would like to ask you all questions individually. You say to them. Amy says smiling, 'Sure, you can the guest ro-' 'NO! the more talkative twin, you think they are twins anyways, screams, you cant go to the guest room, it... its messy verry messy actually, sorry how about the ... bathroom? 'Ok fine the bathrooms' amy grits, you comply.",
        "TODO",
        "0aba",
        "TODO",
        "0abb",
        "TODO",
        "0abc")

    add_scene("0ac",
        "'We were talking about our parents and how irresponsible it is that they aren’t here' Amy says, laughily as the second twin shyly said, 'w-w-we we’re just discussing how the the theif got in.' Everyone paused and looked at each other. You realize someone has to be lying, but why would they be lying to you? 'why the hell should I tell you anything -' because kid, i am here to help you, so please can i talk to each of you individually please?' You snap at the older looking twin, Fine he mumbles.",
        "TODO",
        "0aca",
        "TODO",
        "0acb",
        "TODO",
        "0acc")

init_scenes()
