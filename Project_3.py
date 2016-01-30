# template for "Stopwatch: The Game"

import simplegui

# define global variables
interval = 100
time = 0
stops = 0
correctStop = 0
isRunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    #pass
    D = time%10
    C = (time/10)%10
    B = (time/100)%6
    A = time/600
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isRunning
    isRunning = True
    timer.start()
    
def stop():
    global isRunning
    if isRunning == True:
        timer.stop()
        isRunning = False
        global stops
        stops += 1
        global correctStop
        if time%10 == 0:
            correctStop += 1
    
def reset():
    timer.stop()
    global isRunning
    isRunning = False
    global time
    time = 0
    global stops
    stops = 0
    global correctStop
    correctStop = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    #print time

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [150, 160], 30, "White")
    canvas.draw_text(str(correctStop) + "/" + str(stops), [300, 20], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)

# start frame
frame.start()


# Please remember to review the grading rubric
