x=0
y=0


def setup():
    size(400,400)
   
def draw():
    global x
    line(x,y,200,200)
    x=x+20
    rect(mouseX, mouseY,50,50)
