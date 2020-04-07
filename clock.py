from Tkinter import *
from datetime import datetime
root = Tk()
time1 = ''
clock = Label(root, font=('times', 80, 'bold'), bg='YELLOW')
clock.pack(fill=BOTH, expand=2)
def tick():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    if time != now:
        now = time
        clock.config(text=time)
    clock.after(200, tick)
tick()
root.mainloop()
