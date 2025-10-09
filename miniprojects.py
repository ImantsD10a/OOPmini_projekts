#bibliotēkas sistēma
class Gramata:
    def __init__(self,nosaukums, autors):
        self.nosaukums = nosaukums
        self.autors = autors
        self.ir_aizņemta = False
    
    def aizņemts (self):
       if not self.ir_aizņemta:
         self.ir_aizņemta = True
         print("Grāmata {self.nosaukums} ir aizņemta")
       else:
          print("Grāmata {self.nosaukums} nav aizņemta")
    
    def atdot(self):
       if self.ir_aizņemta:
         self.ir_aizņemta = False
         print("Grāmata {self.nosaukums} ir atdota")
       else:
          print("Grāmata {self.nosaukums} nav atdota")


class Bibliotēka:
   def __init__ (self):
      self.gramatas = ()
    
    
def pievienot_gramatu(self, gramata):
   self.gramatas.append (gramata)
   print("Pievienot grāmatu:{self.nosaukums} {self.autors} ")

def paradit_gramatas(self):
   print("Bibliotēkas grāmatas:{}")  
   for g in self.gramatas:
      stat = "Aizņemta" 
      if g.ir_aizņemta:
        else: "Pieejama"
        print("{g.nosaukums} {g.autors} - {stat}")
      


#prog darb
if __name__ == "__main__":
    bibl = Bibliotēka()

    g1 = Gramata ("aaa","aaa")

    g2 = Gramata ("bbb","bbb")

    bibl.pievienot_gramatu(g1)
    bibl.pievienot_gramatu(g2)

    bibl.paradit_gramatas()

    g1.aiznemt()
    bibl.paradit_gramatas()

    g1.atdot()
    bibl.paradit_gramatas()