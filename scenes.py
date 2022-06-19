scenes = []
def add_scene(tag, description, a, a_next, b, b_next, c, c_next, images=[]):
    scene_info = {
        "tag": tag, # This tag is derrived from the choices required to get there, e.g. "0aba" for "A -> B -> A"
        "description": description, # This is the text providing the information relevant to the questions
        "a": a, # The first question or answer
        "a_next": a_next, # The tag linked to ^
        "b": b, # The second question or answer
        "b_next": b_next, # The tag linked to ^
        "c": c, # The third question or answer
        "c_next": c_next, # The tag linked to ^
        "images": images, # This is a list of image identifiers (by name, like Noemie_happy for Noemie_happy.png), defaults to empty list, max 6
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
        images=["peter_angry"])

    add_scene("0a",
        "'Who knows with those two, you were supposed to be here 1 hour ago, we can't wait forever' he says. You weren't late though, you are never late. \nYou appologize anyways, no point in arguing with a 12 year old. Where are your siblings? you ask nicely, wanting to start the job as soon as poosible. \n\nReluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy, 'Ethan, why are you with that man and who is he?' 'Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Noemie, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "What were you guys arguing about before?",
        "0ac",
        images = ["peter_scared"])

    add_scene("0b",
        "'First of all my name is not kid, its Ethan, second of all, I am not a kid i'm 13 and a half. My birthday was... last week, we went to wendys and ate... pizza!' Ok...ki- Ethan, sorry about that you say, no point in arguing with a 12 year old. Can I talk to your siblings? Best to start talking to some real adults. \n\nReluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy,'Ethan, why are you with that man and who is he?" "Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Noemie, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "What were you guys arguing about before?",
        "0ac",
        images = ["peter_scared"])

    add_scene("0c",
        "'Crime scene? HAHAH who do you think you are batman?' he laughed 'Its just a window' Well your dad asked me to be here and you do not hire a private investigator for a broken window, so can you lead me to an adult I can speak to? you say firmly \n\nReluctantly he brings you to his older siblings, they are all adults, the one who looks like they are in charge says to the boy,'Ethan, why are you with that man and who is he?" "Hell if i know he just walked in acting like sherlock-' Ethan says as You see the kid flinch and freeze, like he hadn't realized who he was talking to before he spoke. You couldnt see his face but you could fell the terror. You ignore it you really don't like getting involved. You ask for the person in charge, the woamn who you though was in charge walked forward and introduced herself 'Hi i'm Noemie, she/her, nice to meet you.' You introduce yourself and tell them why you are in their house. They take you to the living room and you just gawk, did a tornado hit this place, whats happened here you think. The couch on its back, the TV smashed in pieces, all the cabinets emptied in the floors, your walk up slowly to there are no broken pieces on the floor. He looks at the other side of it, and surely broken glass was on the floor at the other side. What do you ask?",
        "Can you take me to the bedrooms?",
        "0aa",
        "Where are your parents? Call them, or something, come on.",
        "0ab",
        "What were you guys arguing about before?",
        "0ac",
        images = ["peter_scared"])

    add_scene("0aa",
        "'What are you on about? What do you need our rooms for?' One of the older boys says hastily,too hastily, You snap your neck towards him and stare 'Bedrooms are off limits' Noemie says. is she trying to hide something? Probably not, no one like snooping around though. 'Is there a reason?' you ask?, 'You know what fine. I would like to talk to talk to you all 1 by 1 please'\n \nHe leads you through a long pathway to the bathroom, as you enter he starts to walk back, you call out hey Kid, as he turns around, he realized he will be your first victim. You sit him down on the toilet, awkward as it is you go along with it anyways. What do you ask next?",
        "Is there a reason we are in the bathroom?",
        "0aaa",
        "Ok kid, so whats your name?",
        "0aab",
        "Where where you when this happened?",
        "0aac",
        images = ["twin1_angry"])

    add_scene("0ab",
        "'No we can not, and can't you speak to us? What do you need them for let us help you.' Noemie says, you sigh and look around, is there a private room? We can stay in i would like to ask you all questions individually. You say to them. Noemie says smiling, 'Sure, you can the guest ro-' 'NO! the more talkative twin, you think they are twins anyways, screams, you cant go to the guest room, it... its messy verry messy actually, sorry how about the ... bathroom? 'Ok fine the bathrooms' Noemie grits, you comply.\n\nHe leads you through a long pathway to the bathroom, as you enter he starts to walk back, you call out hey Kid, as he turns around, he realized he will be your first victim. You sit him down on the toilet, awkward as it is you go along with it anyways. What do you ask next?",
        "Is there a reason we are in the bathroom?",
        "0aba",
        "Ok kid, so whats your name?",
        "0abb",
        "Where where you when this happened?",
        "0abc",
        images = ["amy_angry"])

    add_scene("0ac",
        "'We were talking about our parents and how irresponsible it is that they aren’t here' Noemie says, laughily as the second twin shyly said, 'w-w-we we’re just discussing how the the theif got in.' Everyone paused and looked at each other. You realize someone has to be lying, but why would they be lying to you? 'why the hell should I tell you anything -' because kid, i am here to help you, so please can i talk to each of you individually please?' You snap at the older looking twin, Fine he mumbles.\n\nHe leads you through a long pathway to the bathroom, as you enter he starts to walk back, you call out hey Kid, as he turns around, he realized he will be your first victim. You sit him down on the toilet, awkward as it is you go along with it anyways. What do you ask next?",
        "Is there a reason we are in the bathroom?",
        "0aca",
        "Ok kid, so whats your name?",
        "0acb",
        "Where where you when this happened?",
        "0acc",
        images = ["shy_twin2"])

    add_scene("0aaa",
            "'Yes, The Guest room was... occupied, will that be all?' he replies quickly, 'no it will not, occupied with what?' you ask, he obviously wanted to end this as fast as possible, 'Look i understand everyone has their secrets that they want to keep but i need to find whatever was stolen' 'Stolen?' He replies confused, 'nothing was stolen at all. everything was trashed but he never stole anything.'  'He? who is he?' and if he hadnt stolen anything what was he looking for' you ask quickly, hoping he would open up even for a split second. He realizes he said something he shouldnt have, he runs past you to the door, you give up trying to get anything out of him. Ok before you go whats your name son? He stops looks back and says Sam.\n \nOk Next person get in here you shout, You wait for a while, then you see the other twin peek through the door, take a deep breath and slowly walk past you to the toilet seat the same place Sam was seating in, but he doesnt sit, he just shuffles around in one place awkwardly. 'Ok Nate, lets talk, you are the only one who hasnt said anything at all, i mean im guessing Noemie doesnt only speak for you?' 'Yeah, youre right' he replies, 'Sam also speaks for me' Kid is smart you think, most people would have freked out about the fact that a random person already knew his name. 'Sam let it slip huh?' You stare at him and start laughing. Ok kid tell me what you think happened? *nOT DONE IM TIRED IM GOING TO BED*",
            "TODO",
            "0aaaa",
            "TODO",
            "0aaab",
            "TODO",
            "0aaac",
            images = ["twin1_angry"])
    add_scene("0aab",
              "'Sam, and please dont call me kid, its patronizing.' he replies. 'Ok Sam' you start,'Why are we here, why are we really here?' His face says it all, like how could he possibly know? So you continue gently, what happned, you can tell me anything, ok? you say, he looks at you, and says you have no idea and simply walks out, but at least you learn something as he is walking out he says watch out of Ethan. Ethan? You think?  You say sarcastically 'Ethan the 12 year old?' Yes, the 12 year old he replies. As he leaves you notice the clock on the wall, its 54 minutes ahead.\n \nOk Next person get in here you shout, You wait for a while, then you see the other twin peek through the door, take a deep breath and slowly walk past you to the toilet seat the same place Sam was seating in, but he doesnt sit, he just shuffles around in one place awkwardly. 'Ok Nate, lets talk, you are the only one who hasnt said anything at all, i mean im guessing Noemie doesnt only speak for you?' 'Yeah, youre right' he replies, 'Sam also speaks for me' Kid is smart you think, most people would have freked out about the fact that a random person already knew his name. 'Sam let it slip huh?' You stare at him and start laughing. Ok kid tell me what you think happened? *nOT DONE IM TIRED IM GOING TO BED*",
              "TODO",
              "0aaaa",
              "TODO",
              "0aaab",
              "TODO",
              "0aaac",
              images=["twin1_angry"])
    add_scene("0aac",
              "'I was out with Nate, we were skateboarding, Noemie started spam calling him to come home immediately, he told me and we came home to the mess'. He says slouching like he did not care you were there, but his eyes hanged on my everyword, he wanted me there. Why didnt she call you?' You ask. 'Becasue I wouldnt have answered her, we dont get along well, siblings things you know?'. 'You have other siblings right? why only her?' 'BECAUSE HE TREATS HER LIKE A QUEEN while...' he reduces his voice, but still stern, he doesnt want anyone to hear him, 'while the rest of us get her scraps... what ever man this is a joke im leaving' 'Wait Kid whats your name?' you quickly ask hoping something more slips out, 'Sam' he says as he walks past you without even looking back. Smart kid you think.\n \nOk Next person get in here you shout, You wait for a while, then you see the other twin peek through the door, take a deep breath and slowly walk past you to the toilet seat the same place Sam was seating in, but he doesnt sit, he just shuffles around in one place awkwardly. 'Ok Nate, lets talk, you are the only one who hasnt said anything at all, i mean im guessing Noemie doesnt only speak for you?' 'Yeah, youre right' he replies, 'Sam also speaks for me' Kid is smart you think, most people would have freked out about the fact that a random person already knew his name. 'Sam let it slip huh?' You stare at him and start laughing. Ok kid tell me what you think happened? *nOT DONE IM TIRED IM GOING TO BED*",
              "TODO",
              "0aaaa",
              "TODO",
              "0aaab",
              "TODO",
              "0aaac",
              images=["twin1_angry"])
init_scenes()
