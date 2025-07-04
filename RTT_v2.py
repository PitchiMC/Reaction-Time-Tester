import tkinter as tk
import random
import time



window = tk.Tk()
window.title("ReactionTimeTest_v2 - by Pitchi")
window.geometry("450x220")
window.configure(bg="gray")


InfoLabel = tk.Label(window, font=("Helvetica", 12), text="Click the BUTTON below when you're ready!", background="gray")
InfoLabel.pack(pady=20)

button = tk.Button(window, text="Start", width=25, height=4, font=("Helvetica", 12), background="green", activeforeground="darkgreen")
button.pack(pady=20)


started = False
start_time = 0



def startTest():
    global started, start_time

    if started:
        InfoLabel.config(text="You clicked too early! Click the button to start again.")
        resetButton()
        return

    started = True
    InfoLabel.config(text="Wait for it...")
    button.config(text="wait...", command=None)

    delay = random.randint(1, 5)
    window.after(delay * 1000, showReactionButton)



def showReactionButton():
    global start_time

    start_time = time.time()
    button.config(text="Click me!", background="red")

    button.unbind("<ButtonPress-1>")
    button.bind("<ButtonPress-1>", recordReactionTime)

    InfoLabel.config(text="CLICK")



def recordReactionTime(event=None):
    global started, start_time

    reaction_time = time.time() - start_time
    InfoLabel.config(text=f"Reaction time: {reaction_time:.3f} seconds! Click the button to try again.")

    button.config(state="disabled")

    window.after(300, resetButton)



def resetButton():
    global started

    button.config( text="Start", font=("Helvetica", 12), background="green", activeforeground="darkgreen", command=startTest, state="normal")
    button.unbind("<ButtonPress-1>")
    started = False



button.config(command=startTest)

window.mainloop()
