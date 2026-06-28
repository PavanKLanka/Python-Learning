class Human:
    def __init__(self, n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
           if self.occupation == "t":
               print(self.name,"Tennis Player")
           elif self.occupation == "a":
               print(self.name,"Actor")

    def do_speaks(self):
            print(self.name, " Says how are you doing")



# tom = Human("Tom",'a')
# tom.do_work()
# tom.do_speaks()


mar = Human("Sha",'t')
mar.do_work()
mar.do_speaks()