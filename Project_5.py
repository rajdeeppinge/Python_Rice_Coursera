# implementation of card game - Memory

import simplegui
import random
    
# helper function to initialize globals
def new_game():
    global lst1, lst, state, index1, index2, count, exposed
    count = 0
    label.set_text("Turns = " + str(count))
    index1 = -20
    index2 = -20
    state = 0
    # may write this in loop form also
    exposed = [False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False]	
    lst1 = [i for i in range(8)]
    lst = lst1 + lst1
    random.shuffle(lst)
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, index1, index2, count
        
    for i in range(len(lst)):
        if pos[0] > 50*i and pos[0] < 50*(i+1) and exposed[i] == False:
            if state == 0:
                state = 1
                index1 = i
                count += 1
                label.set_text("Turns = " + str(count))
            elif state == 1:
                state = 2
                index2 = i
            else:
                state = 1
                count += 1
                label.set_text("Turns = " + str(count))
                if lst[index1] != lst[index2]:
                    exposed[index1] = False
                    exposed[index2] = False
                index1 = i
                
            exposed[i] = True
                
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(lst)):
        if exposed[i] == True:
            canvas.draw_text(str(lst[i]), (50*i+20,55), 20, "White")
        else:
            canvas.draw_polygon([(50*i, 0), (50*(i+1), 0), (50*(i+1), 100), (50*i, 100)], 5, 'Black', 'Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric