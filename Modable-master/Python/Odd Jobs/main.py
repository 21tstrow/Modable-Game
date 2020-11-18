#1366 x 768
#Calculating Functions:

##pygame.font.init()
##screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
##pygame.display.set_caption('SMART DUMMY')

def wR(x):
  w = pygame.display.get_surface().get_size()[0]
  x *= (w / 1920)
  return int(x)

def hR(x):
  w = pygame.display.get_surface().get_size()[1]
  x *= (w / 1050)
  return int(x)

def mainpath():
    if platform.system() == "Windows":
        f = "C:\\Users"
    elif platform.system() == "Darwin":
        f = "/Users"
    elif platform.system() == "Linux":
        f = None
    else:
        print("System not found!")
    return pathlib.Path(f).glob('**/*') 


def search(path, file):
    for x in path:
        if (x.name == file):
            return x

def findImage(file):
    m = mainpath()
    fname = search(m, file)
    print(fname)
    print("Done")

#Classes:
##Background Object Tree
class BackgroundObject():
  def __init__(self, image):
    self.image = image

class InteractableBackgroundObject(BackgroundObject):
  def __init__(self,image,loc, fxn):
    super().__init__(image)
    self.x, self.y, self.w, self.h = loc
    self.function = fxn

  def toString(self):
      return "Interactable Background Object image: " + str(self.image) + " @ (" + str(self.x) + "," + str(self.y) + ") that is " + str(self.w) + "x" + str(self.h)


##Sprite Tree
class Sprite():
  def __init__(self, image, size, location):
    self.image = image
    self.size = size
    self.x, self.y = location

class Npc(Sprite):
  
  def __init__(self, dialougePath):
    pass

ibo1 = InteractableBackgroundObject("Derp.png",(3,4,5,6), "FXN")
print(ibo1.toString())

#Backgrounds:



backgrounds = []
