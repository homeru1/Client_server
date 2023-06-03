from tkinter import *
from tkinter.ttk import *

import Client
import socket

import matplotlib


def Init():
    matplotlib.use('Agg')
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('1000x600')
    return window

def clicked():
    ip_dest = input_ip.get()
    port_dest = input_port.get()
    if ip_dest == '':
        ip_dest = socket.gethostname()
    if port_dest == '':
        port_dest = 5000
    encoded_msg = Client.Encode(input_msg.get(1.0, END),combo.current())
    Client.start_client(encoded_msg, ip_dest,port_dest)
    

def SetValue():
    combo['values'] = (Client.ReturnCertificates())
    combo.current(0)


if __name__ == "__main__":
    window = Init()

    ip = Label(window, text="Enter Ip adress (empty for default):",font=('Arial', 12))
    ip.grid(column=0, row=0)
    input_ip = Entry(window,width=15)
    input_ip.grid(column=1, row=0)

    port = Label(window, text="Enter port (empty for default):",font=('Arial', 12))
    port.grid(column=0, row=1)
    input_port = Entry(window,width=15)
    input_port.grid(column=1, row=1)


    btn = Button(window, text="Send", command=clicked)
    btn.grid(column=3, row=0)

    btn_for_cert = Button(window, text="Refresh Certificates", command=SetValue)
    btn_for_cert.grid(column=1, row=2)

    combo = Combobox(window)
    SetValue()
    combo.grid(column=0, row=2,ipadx=250)

    msg = Label(window, text="Enter message:",font=('Arial', 12))
    msg.grid(column=0, row=4)
    input_msg = Text(width=100, height=25)
    input_msg.grid(columnspan=2)

    window.mainloop()

