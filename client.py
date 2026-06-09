import socket
from tkinter import *

# creating the main window
root = Tk()
root.title("Client")

# listbox to display messages
listbox = Listbox(root, width=50, height=15)
listbox.pack()

def receive():
    try:
        msg = s.recv(1024).decode("utf-8")
        listbox.insert('end', "Server: " + msg)
    except:
        listbox.insert('end', "[Error] Could not receive message.")

def send():
    msg = entry.get()
    if msg:
        listbox.insert('end', "You: " + msg)
        try:
            s.send(bytes(msg, "utf-8"))
        except:
            listbox.insert('end', "[Error] Could not send message.")
        entry.delete(0, END)

# buttons
Button(root, text="Recieve", command=receive).pack()
Button(root, text="Send", command=send).pack()

# text entry box
entry = Entry(root, width=50)
entry.pack(side=BOTTOM)

# connecting to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

try:
    s.connect((HOST_NAME, PORT))
    print("Connected to server!")
except Exception as e:
    print("Could not connect to server:", e)
    exit()

root.mainloop()