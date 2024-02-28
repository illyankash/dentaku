import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("電卓")

        self.total = 0
        self.entered_number = 0
        self.current = ""
        self.operator = ""

        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('C', 4, 0), ('=', 4, 2),
        ]
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, height=2, width=5, command=lambda t=text: self.click(t))
            button.grid(row=row, column=col)

    def click(self, text):
        if text.isdigit() or text == '.':
            self.current += text
            self.update_display(self.current)
        elif text in ['+', '-', '*', '/']:
            if self.current != "":
                self.entered_number = float(self.current)
                self.total = self.entered_number
                self.current = ""
            self.operator = text
        elif text == '=':
            if self.current != "":
                if self.operator != "":
                    self.calculate(float(self.current))
                else:
                    self.total = float(self.current)
            self.update_display(str(self.total))
            self.current = str(self.total)
        elif text == 'C':
            self.clear()

    def calculate(self, second_number):
        if self.operator == '+':
            self.total += second_number
        elif self.operator == '-':
            self.total -= second_number
        elif self.operator == '*':
            self.total *= second_number
        elif self.operator == '/':
            if second_number != 0:
                self.total /= second_number
            else:
                self.update_display("Error")
                self.total = 0
        self.operator = ""

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

    def clear(self):
        self.display.delete(0, tk.END)
        self.current = ""
        self.total = 0
        self.operator = ""

if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
