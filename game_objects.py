game_objects = []

def add(game_object):
    game_objects.append(game_object)

def update():
    for game_object in game_objects:
        game_object.update()

def render(canvas):
    for game_object in game_objects:
        game_object.render(canvas)