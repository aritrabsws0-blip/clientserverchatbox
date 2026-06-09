import socket
from tkinter import *

# creating the main window
root = Tk()
root.title("Server")

# listbox to show chat messages
listbox = Listbox(root, width=50, height=15)
listbox.pack()

def receive():
    try:
        msg = client.recv(1024).decode("utf-8")
        listbox.insert('end', "Client: " + msg)
    except:
        listbox.insert('end', "[Error] Could not receive message.")

def send():
    msg = entry.get()
    if msg:
        listbox.insert('end', "You: " + msg)
        try:
            client.send(bytes(msg, "utf-8"))
        except:
            listbox.insert('end', "[Error] Could not send message.")
        entry.delete(0, END)

# buttons
Button(root, text="Receive", command=receive).pack()
Button(root, text="Send", command=send).pack()

# text entry box
entry = Entry(root, width=50)
entry.pack(side=BOTTOM)

# set up the socket and wait for client to connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))
s.listen(4)

print("Waiting for client to connect...")
client, address = s.accept()
print("Connected to:", address)

root.mainloop()