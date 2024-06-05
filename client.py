import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.username = simpledialog.askstring("Username", "Enter your username")
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 5556))  # Changed port to 5556
        self.client_socket.send(self.username.encode('utf-8'))

        self.text_area = scrolledtext.ScrolledText(root)
        self.text_area.pack(padx=20, pady=10)
        self.text_area.config(state=tk.DISABLED)
        
        self.message_entry = tk.Entry(root)
        self.message_entry.pack(padx=20, pady=10)
        
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=20, pady=10)
        
        threading.Thread(target=self.receive_messages).start()
        
    def send_message(self):
        message = self.message_entry.get()
        self.client_socket.send(message.encode('utf-8'))
        self.message_entry.delete(0, tk.END)
        
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.text_area.config(state=tk.NORMAL)
                self.text_area.insert(tk.END, message + '\n')
                self.text_area.config(state=tk.DISABLED)
            except:
                break

root = tk.Tk()
app = ChatClient(root)
root.mainloop()
