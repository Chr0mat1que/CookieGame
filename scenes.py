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
    add_scene("0", "Hello World", "a", "0a", "b", "0b", "c", "0c")

init_scenes()
