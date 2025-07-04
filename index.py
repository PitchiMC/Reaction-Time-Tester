import tkinter as tk
import random
import time

# Initialize the main window
window = tk.Tk()
window.title("Reaction Time Test - by Pitchi")
window.geometry("450x350")

# Create and place the initial info label
InfoLabel = tk.Label(window, font=("Helvetica", 12), text="Click the BUTTON below when you're ready!")
InfoLabel.pack(pady=20)

# Create and place the start button
startButton = tk.Button(window, text="Start", width=25, height=4, font=("Helvetica", 12))
startButton.pack(pady=20)

# Global variables to keep track of state
started = False
start_time = 0
reaction_button = None

def startTest():
    global started, start_time, reaction_button

    if started:
        # Reset the test if the button is clicked prematurely
        InfoLabel.config(text="You clicked too early! Click the button to start again.")
        if reaction_button:
            reaction_button.destroy()
            reaction_button = None
        started = False
        return
    
    # Set the started flag to True and reset the info label
    started = True
    InfoLabel.config(text="Wait for it...")

    # Wait for a random time between 1 to 5 seconds
    delay = random.randint(1, 5)
    window.after(delay * 1000, showReactionButton)


def showReactionButton():
    global start_time, reaction_button

    # Display the new button and record the start time
    start_time = time.time()
    reaction_button = tk.Button(window, text="Click me!", width=25, height=4, font=("Helvetica", 12), command=recordReactionTime)
    reaction_button.pack(pady=20)


def recordReactionTime():
    global started, start_time, reaction_button

    # Calculate reaction time and update the info label
    reaction_time = time.time() - start_time
    InfoLabel.config(text=f"Reaction time: {reaction_time:.3f} seconds! Click the button to try again.")

    # Reset the state
    reaction_button.destroy()
    reaction_button = None
    started = False

# Bind the start button to the startTest function
startButton.config(command=startTest)

# Start the main event loop
window.mainloop()