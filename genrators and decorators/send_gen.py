def chai_customer():
    print("welcome sir !what type of chai you want")
    order = yield
    while True:
        print(f"preparing: {order}")
        order =yield

stall = chai_customer()
next(stall) 

stall.send("ro cha")