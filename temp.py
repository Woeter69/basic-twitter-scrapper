characters={}
class Character:
  def __init__(self,name,hp,power,role): # the attributes after self are just normal attributes passed in a function.
    
    '''THIS IS IMPORTANT STEP in OOP as we're defining the name/hp/power/role which user entered to object attributes. See the self.name as aang.name = "Aang" where aang is the object (or self) and "Aang" is its value. Same with hp/power/role.'''
    
    self.name = name 
    self.hp = hp
    self.power = power
    self.role = role.lower()
    characters[self.name] = self # Adding the Names User Entered/Object Name as key and the object as its key that is the current object (aang/katara/zuko)
    
  def show_info(self):
    print(f"[{self.role.upper()}] {self.name} --> HP {self.hp} Power {self.power}]") #Modifiable String again using self (Current Object)

# Using the Class(Template) to make objects
aang=Character("Aang",500,45,"hero") 
katara=Character("Katara",200,80,"hero")
zuko=Character("Zuko",600,90,"villan")

user_input = input("Enter Hero/Villan Name to check stats")

for object in characters.values():
  if object.name.lower() == user_input.lower():
    object.show_info() #Calling object functions





  


  
