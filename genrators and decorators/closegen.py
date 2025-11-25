def local_chai():
    yield "masala chai"
    yield "ginger tea"


def imported_chai():
    yield "MACHA"
    yield "ulong tea"

def full_name():
    yield from local_chai()
    yield from imported_chai()

for chai in full_name():
    print(chai)


def chai_stall():
            try:
                  while True:
                        order = yield "waiting for the chai order"
                    
            except:
                  print("stall is closed")

stall = chai_stall()
print(next(stall))
stall.send("ro chai")
stall.close()                  