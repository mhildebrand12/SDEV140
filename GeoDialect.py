import tkinter as tk

class GeoDialectHomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoDialect Home Page")
        self.root.geometry("800x600")

        # Main title label
        self.title = tk.Label(self.root, text="GeoDialect", font=("Helvetica", 36))
        self.title.pack()

        # Cocky label
        self.cocky = tk.Label(self.root, text="I bet I can guess your region of origin.", font=("Calibri", 24))
        self.cocky.pack()
        
        # Exit button
        self.exitButton = tk.Button(self.root, text="Exit", font=("Comic Sans", 12), command=self.root.quit)
        self.exitButton.pack()

        def quit(self):
            self.root.destroy()

root = tk.Tk()
app = GeoDialectHomePage(root)
root.mainloop()
