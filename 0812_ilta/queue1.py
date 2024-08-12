def enQue(item):
    global rear
    if isFull() : print("Queue_Full")
    else : 
        rear += 1
        Q.inset(rear , item) 
def deQue()