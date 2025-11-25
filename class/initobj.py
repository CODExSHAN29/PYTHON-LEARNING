class chaiorder:
    def __init__(self,type_,size):
        self.type = type_
        self.size =size

    def summary(self):
        return f"{self.size} ml of {self.size}chai"
order =chaiorder("masala",300)
