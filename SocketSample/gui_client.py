import tkinter
import socket
from threading import Thread

def send(event=None):
    pass
    msg = input_msg.get()
    sock.send(bytes(msg, "utf-8"))
    input_msg.set("")
    if msg == "/bye":
        sock.close()
        win.quit()

def recvMessage():
    while True:
        msg = sock.recv(1024)
        chat_list.insert(tkinter.END, msg.decode("utf-8"))
        print(msg.decode())

def on_delete(event=None):
    input_msg.set("/bye")
    send()
    
win = tkinter.Tk()
win.title("채팅 프로그램")

frame = tkinter.Frame(win)
input_msg = tkinter.StringVar()

scroll = tkinter.Scrollbar(frame)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
chat_list = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scroll.set)
chat_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
frame.pack()

inputbox = tkinter.Entry(win, textvariable=input_msg)
inputbox.bind("<Return>", send)
inputbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES, padx=5, pady=5)
send_button = tkinter.Button(win, text="전송", command=send)
send_button.pack(side=tkinter.RIGHT, fill=tkinter.X, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", on_delete)

IP = input("접속될 아이피를 입력하세요:")
PORT = 9700
if not IP:
    IP = "localhost"
print("접속: {}:{}".format(IP, PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))
receive_thread = Thread(target=recvMessage)
receive_thread.daemon=True
receive_thread.start()

win.mainloop()

