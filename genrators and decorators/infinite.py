def infinte_chai():
    count = 1
    while True:
        yield f"refil #{count}"
        count +=1

refill = infinte_chai()
user2 =infinte_chai()

for _ in range (8):
            print(next(refill)) 