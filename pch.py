#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as msgbox
__about__ = """Copy-paste your PCH and press run. After result you can find in Clipboard buffer."""

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        def show_error(*args):
            import traceback
            a = traceback.format_exception(*args)
            msgbox.showerror(a[-1], "\n".join(a[:-1]))        
        self._root().report_callback_exception = show_error
        self.master = master

    def create_widgets(self):
        button_main_row = 1
        self.label = tk.Label(self, text=__about__)
        self.label.pack(fill = "both")
        self.sc_text = scrolledtext.ScrolledText(self, height=10)
        self.sc_text.pack(fill = "both")
        
        self.run_button = tk.Button(self,
                                          text="Run",
                                          command=self.run)
        self.run_button.pack(fill = "both")
        self.out_text = scrolledtext.ScrolledText(self, height=10)
        self.out_text.pack(fill = "both")
        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.QUIT.pack(side = "bottom", fill = "both")

    def msgbox(self, msg):
        msgbox.showinfo("Info", msg)

    def print_func(self, msg):
        self.out_text.insert(tk.END, msg+'\n')

    def get_text(self):
        return self.sc_text.get(1.0, tk.END)

    def run(self):
        """This is main function with business logick"""
        txt = self.get_text()
        array = txt.split(", ")
        tx = '\n'.join(array)
        #Output to text widget
        self.print_func(tx)
        #Copy to Clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(tx)

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.master.title(__about__)
    app.mainloop()

if __name__ == '__main__':
    main()
