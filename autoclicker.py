import tkinter as tk
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import threading
import time

mouse = Controller()
clicking = False

BUTTONS = {
    "Left": Button.left,
    "Right": Button.right,
    "Middle": Button.middle
}

def clicker():
    while True:
        if clicking:
            selected_button = BUTTONS[click_type.get()]
            mouse.click(selected_button, 1)
            time.sleep(click_speed.get())
        else:
            time.sleep(0.1)

def on_press(key):
    global clicking
    if key == KeyCode.from_char('\x03'):
        clicking = not clicking
        status_label.config(text="Status: RUNNING" if clicking else "Status: STOPPED", 
                            fg="green" if clicking else "red")

root = tk.Tk()
root.title("Fast Auto-Clicker")
root.geometry("300x280")

tk.Label(root, text="Click Delay (seconds):", font=("Arial", 10)).pack(pady=5)
click_speed = tk.DoubleVar(value=0.001) 
tk.Entry(root, textvariable=click_speed, justify='center').pack()

tk.Label(root, text="Click Type:", font=("Arial", 10)).pack(pady=5)
click_type = tk.StringVar(value="Left")
dropdown = tk.OptionMenu(root, click_type, *BUTTONS.keys())
dropdown.pack()

status_label = tk.Label(root, text="Status: STOPPED", fg="red", font=("Arial", 12, "bold"))
status_label.pack(pady=20)

tk.Label(root, text="Hotkey: Ctrl + C", font=("Arial", 10, "bold")).pack()

click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()

listener = Listener(on_press=on_press)
listener.start()

root.mainloop()
