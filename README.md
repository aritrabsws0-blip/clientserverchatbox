# Python Chat Application

A simple two-way chat application built using Python's socket module and Tkinter for the GUI.
Both the server and client have their own chat window with Send and Receive buttons.

---

## Requirements

- Python 3.x
- No external libraries needed (socket and tkinter are part of Python's standard library)

---

## Project Structure

```
chat-app/
│
├── server.py       # Server side of the chat application
├── client.py       # Client side of the chat application
└── README.md       # This file
```

---

## How to Run

### Step 1 - Open two terminal windows

You need two separate terminals — one for the server and one for the client.

### Step 2 - Run the Server

In the first terminal, type:

```
python server.py
```

A GUI window titled **"Server"** will open and wait for the client to connect.

### Step 3 - Run the Client

In the second terminal, type:

```
python client.py
```

A GUI window titled **"Client"** will open and connect to the server automatically.

---

## How to Use

1. Type your message in the **entry box** at the bottom of the window.
2. Click **Send** to send the message to the other side.
3. Click **Recieve** to fetch the latest message sent by the other side.
4. All messages appear in the **listbox** at the top of the window.

---

## Error Handling

- If the client cannot connect to the server, an error message is printed in the terminal and the program exits cleanly.
- If a message cannot be sent or received (e.g. connection dropped), an error message is shown inside the chat window instead of crashing the program.

---

## Notes

- Always start **server.py before client.py**, otherwise the client will have nothing to connect to.
- Both programs must run on the **same machine** since they use the local hostname.
- The receive buffer is set to **1024 bytes**, so very long messages may get cut off.

---

## Author

Made as a Python socket programming project using Tkinter for the GUI.
