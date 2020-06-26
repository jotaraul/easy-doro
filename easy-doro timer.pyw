import tkinter as tk
from playsound import playsound


def countdown():
	global count
	global n_pomodoros
	
    # change text in label        
	minutes = count // 60
	if minutes < 10: 
		minutes = str(0)+str(minutes)
	seconds = count % 60
	if seconds < 10: 
		seconds = str(0)+str(seconds)
	label['text'] = str(minutes) + ":" + str(seconds)
	window.title("Easy-doro timer ("+str(minutes)+')')
	
	if count > 0:
        # call countdown again after 1000ms (1s)
		count -= 1
		window.after(1000, countdown)
	else:
		window.title("Easy-doro timer")
		n_pomodoros += 1
		label_n_pomodoros['text'] = "Completed pomodoros: " + str(n_pomodoros)
		playsound('ship_bell_sound.mp3')
		
def handle_click_start(event):
	global count
	label['fg'] = 'blue'
	if not count:
		count = 30*60
		window.after(1000, countdown)
	else:
		count = 30*60
	print("The button start was clicked!")
	
def handle_click_relax(event):
	global count
	label['fg'] = 'green'
	if not count:
		count = 10*60
		window.after(1000, countdown)
	else:
		count = 10*60
	print("The button relax was clicked!")
	
	
window = tk.Tk()
window.title("Easy-doro timer")
window.geometry("300x200")

frame = tk.Frame()

label = tk.Label(master=frame,text="", font=('Helvetica', 48), fg='blue')
#label.place(x=35, y=15)
label.pack()

button_start = tk.Button(master=frame,text="Start easy-doro",width=25,height=2,bg="blue",fg="yellow")
button_start.bind("<Button-1>", handle_click_start)
button_start.pack()

button_relax = tk.Button(master=frame,text="Start relax",width=25,height=2,bg="blue",fg="yellow")
button_relax.bind("<Button-1>", handle_click_relax)
button_relax.pack()

n_pomodoros = 0
label_n_pomodoros = tk.Label(master=frame,text="Completed easy-doros: "+str(n_pomodoros))
label_n_pomodoros.pack()


frame.pack()

# call countdown first time    
count = 30*60
countdown()
# window.after(0, countdown, 5)

window.mainloop()