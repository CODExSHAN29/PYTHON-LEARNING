def serve_chai():
    yield "cup 1: masala chai"
    yield "cup 2 : lemon chai"


stall = serve_chai()


for cup in stall :
    print(cup)