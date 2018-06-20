def setup():
    # size(600, 600)
    fullScreen()

def draw(): 
    background(150)
    print(mouseX, mouseY)
    w = mouseX    # width of rect
    h = mouseY    # hieght of rect
    
    w=map(w, 0, width, 0, width * 1/6)
    h=map(h, 0, height, 0, width * 1/6)
        
        
        
        # blue
    fill(0, 0, 255)
    rect(0, 0, w, h) #1
    rect(2*w, 2*h, w, h) #3

    # green
    fill(0, 255, 0)
    rect(w, h, w, h) #2
    rect(4*w, 4*h, w, h) #5      

    # red
    fill(255, 0, 0)
    rect(3*w, 3*h, w, h) #4
    rect(5*w, 5*h, w, h) #6
