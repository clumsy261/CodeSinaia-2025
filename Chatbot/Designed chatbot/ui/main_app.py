import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox
from pathlib import Path
import json
import webbrowser
import os

from ux.messages import send_message, clear_chat
from ux.json_handling import load_chat, save_chat

ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

figma_link = "https://www.figma.com/design/cuNtrpjCHpGHbauYEfwbeJ/CodeSinaia_UI_Students?node-id=0-1&t=mcJ6qFdLuzdR6EcY-1"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_app():
    
    # daca nu exista directorul data, se creeaza unul nou
    if not Path("data").exists():
        Path("data").mkdir(parents=True, exist_ok=True)
    
    # daca nu exista fisierul json, se creeaza unul nou
    if not Path("data/history.json").exists():
        with open("data/history.json", "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
    
    root = tk.Tk()
    
    #TODO: de ce dă eroare? REZOLVĂ
    # upper left image logo
    try:
        root.iconbitmap(relative_to_assets("code_sinaia_logo.ico"))  # Ensure you have a code_sinaia_logo.ico file in the assets directory
    except tk.TclError:
        messagebox.showerror("Error", "Icon file not found. Please ensure 'code_sinaia_logo.ico' is in the assets directory.")
        return
    
    
    window_width = 800
    window_height = 600
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    display_x = (screen_width // 2) - (window_width // 2)
    display_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{display_x}+{display_y}")
    root.title("Code Sinaia 2025 - Chatbot App")
    
    # Buttons
    def on_send():
        send_message(entry, chat_log)
    def on_clear():
        clear_chat(chat_log)
    def on_load():
        load_chat(chat_log)
    def on_save():
        save_chat(chat_log)
        
    #TODO: insert the code here
    root.configure(bg = "#D9D9D9")


    canvas = Canvas(
        root,
        bg = "#D9D9D9",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        30.0,
        73.0,
        770.0,
        455.0,
        fill="#A9A9A9",
        outline="")

    canvas.create_rectangle(
        30.0,
        465.0,
        770.0,
        505.0,
        fill="#A9A9A9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_send() ,
        relief="flat",
        activebackground="#D9D9D9",
        background="#D9D9D9"
    )
    button_1.place(
        x=30.0,
        y=517.0,
        width=130.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_clear(),
        relief="flat",
        activebackground="#D9D9D9",
        background="#D9D9D9"
    )
    button_2.place(
        x=195.0,
        y=517.0,
        width=130.0,
        height=40.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:on_load(),
        relief="flat",
        activebackground="#D9D9D9",
        background="#D9D9D9"
    )
    button_3.place(
        x=610.0,
        y=517.0,
        width=130.0,
        height=40.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_save(),
        relief="flat",
        activebackground="#D9D9D9",
        background="#D9D9D9"
    )
    button_4.place(
        x=439.0,
        y=516.0,
        width=130.0,
        height=40.0
    )

    canvas.create_text(
        260.0,
        16.999999999999993,
        anchor="nw",
        text="CLUMSY CHATBOT",
        fill="#000000",
        font=("Inter", 32 * -1)
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: webbrowser.open("https://github.com/clumsy261/CodeSinaia-2025"),
        relief="flat",
        activebackground="#D9D9D9",
        background="#D9D9D9"
    )
    button_5.place(
        x=709.0,
        y=575.0,
        width=61.0,
        height=20.0
    )

    canvas.create_rectangle(
        -4.0,
        562.0,
        800.0,
        566.0,
        fill="#C4C4C4",
        outline="")

    canvas.create_text(
        323.0,
        575.0,
        anchor="nw",
        text="™CodeSinaia 2025",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        30.0,
        575.0,
        anchor="nw",
        text="©2025 Inproted",
        fill="#000000",
        font=("Inter", 14 * -1)
    )
    
    # Chat log (Text widget)
    chat_log = Text(root, bg="#C5C5C5", bd=0, state=tk.DISABLED, wrap="word")
    chat_log.place(x=30.0, y=73.0, width=740.0, height=361.0)

    # Entry box
    entry = Entry(root, bd=0)
    entry.place(x=30.0, y=465.0, width=740.0, height=40.0)
    entry.configure(bg="#C5C5C5", font=("Inter", 14 * -1), highlightthickness=0, relief="flat")
    
    
    root.bind('<Return>', lambda event=None: on_send()) # Send message on Enter key press
    root.resizable(False, False)
    root.mainloop()