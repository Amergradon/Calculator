import tkinter as tk
class Button:
    def __init__(self, master, text, font, bg="#FFFFFF", fg="#000000", activebg="#F0F0F0", activefg="#000000", command=None):
        self.text = text
        self.bg = bg
        self.fg = fg
        self.activebg = activebg
        self.activefg = activefg
        self.command = command
        if text != "=" and text != "delete" and text != "Square root" and text != "Clear":
            self.btn = tk.Button(master, font=font, text=text, borderwidth=0, command=self._command, bg=bg, fg=fg)
        else:
            self.btn = tk.Button(master, font=font, text=text, borderwidth=0, command=command, bg=bg, fg=fg)
        self.btn.bind("<Enter>", self.enterbutton)
        self.btn.bind("<Leave>", self.leavebutton)

    def _command(self):
        self.command(self.text)

    def enterbutton(self, event):
        self.btn.config(bg=self.activebg, fg=self.activefg)
    def leavebutton(self, event):
        self.btn.config(bg=self.bg, fg=self.fg)

    def get_number(self):
        return self.text
    def grid(self, row=0, column=0, sticky=""):
        self.btn.grid(row=row, column=column, sticky=sticky)