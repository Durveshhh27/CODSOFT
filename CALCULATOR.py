import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 14), bd=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, font=("Arial", 14), bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

        for i in range(4):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        current_text = self.result_var.get()
        if text == "=":
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
