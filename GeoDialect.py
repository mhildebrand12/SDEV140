import tkinter as tk
from PIL import ImageTk, Image

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
        self.exitButton.pack(side="right", padx=50, pady=50)

        # Start button
        self.startButton = tk.Button(self.root, text="Start", font=("Comic Sans", 12), command=self.open_second_page) #changed command from GeoDialectTestPage
        self.startButton.pack(side="right", padx=50, pady=50)

        # America Image
        self.img = Image.open("America.png")
        self.img = self.img.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

        # display image
        self.label = tk.Label(self.root, image = self.photo)
        self.label.pack()

    def quit(self):
        self.root.destroy()

    def open_second_page(self):
        # Hide the main window
        self.root.withdraw()

        # Create the second window
        topLevel = tk.Toplevel(self.root) #changed from test_page = GeoDialectTestPage()
        app = GeoDialectTestPage(topLevel) #changed from test_page = test_page

        # Close the main window when the second window is closed
        topLevel.protocol("WM_DELETE_WINDOW", self.quit)

class GeoDialectTestPage:
    def __init__(self, topLevel):
        self.topLevel = topLevel
        self.topLevel.title("GeoDialect Test Page")
        self.topLevel.geometry("800x600")
        self.texts = ["Which would you use to adress a group of people?", "What would you call a soft drink?","What do you call the thing from which you might drink water from?", "What do you call a long sandwich that contains cold cuts, lettuce, etc.?", "What do you call it when it is raining and the sun is out?"]
        self.northeast_texts = ["Yous", "Soda", "Bubbler", "Grinder", "Sunshower"]
        self.westcoast_texts = ["You all", "Tonic", "Drinking Fountain", "Hoagie", "Liquid Sun"]
        self.rockystates_texts = ["You guys", "Cola", "Water Bubbler", "Hero", "Pineapple Rain"]
        self.midwest_texts = ["You", "Pop", "Water Fountain", "Sub", "No Term"]
        self.south_texts = ["Y'all", "Coke", "Fountain", "Po' Boy", "The Devil is Beating His Wife"]
        self.current_text_index = 0
        self.num_questions_asked = 0 # New variable to track number of questions asked
        self.test_value = 0

        # Dictionary to store button values
        self.button_values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        # Main title label
        self.title = tk.Label(self.topLevel, text="GeoDialect", font=("Helvetica", 36))
        self.title.pack()

        # Add a label to the second window
        self.label = tk.Label(self.topLevel, text=self.texts[0])
        self.label.pack(padx=50, pady=50) # adds some padding to the label

        # Northeast button
        self.northeastButton = tk.Button(self.topLevel, text=self.northeast_texts[0], font=("Comic Sans", 12), command=lambda: self.button_clicked(1)) 
        self.northeastButton.pack(side="right", padx=50, pady=0)
        self.test_value = self.test_value + 1


        # West Coast button
        self.westcoastButton = tk.Button(self.topLevel, text=self.westcoast_texts[0], font=("Comic Sans", 12), command=lambda: self.button_clicked(2)) 
        self.westcoastButton.pack(side="right", padx=10, pady=45)
        self.test_value = self.test_value + 2

        # Rocky States button
        self.rockystatesButton = tk.Button(self.topLevel, text=self.rockystates_texts[0], font=("Comic Sans", 12), command=lambda: self.button_clicked(3)) 
        self.rockystatesButton.pack(side="right", padx=10, pady=45)
        self.test_value = self.test_value + 3

        # Midwest button
        self.midwestButton = tk.Button(self.topLevel, text=self.midwest_texts[0], font=("Comic Sans", 12), command=lambda: self.button_clicked(4)) 
        self.midwestButton.pack(side="right", padx=30, pady=90)
        self.test_value = self.test_value + 4

        # South button
        self.southButton = tk.Button(self.topLevel, text=self.south_texts[0], font=("Comic Sans", 12), command=lambda: self.button_clicked(5)) 
        self.southButton.pack(side="right", padx=30, pady=90)
        self.test_value = self.test_value + 5

        self.buttons = [self.northeastButton, self.westcoastButton, self.rockystatesButton, self.midwestButton, self.southButton]

    # This method keeps track of the amount of times a button has been pressed
    def button_clicked(self, index):
        if self.current_text_index == len(self.texts):
            self.current_text_index = 0
        else:
            self.current_text_index += 1
        new_text = self.texts[self.current_text_index]
        self.label.config(text=new_text)
    # This method returns the values of the buttons
    def get_current_button_text(self):
        if self.current_text_index % 5 == 0:
            return self.northeast_texts[self.current_text_index // 5]
        elif self.current_text_index % 5 == 1:
            return self.westcoast_texts[self.current_text_index // 5]
        elif self.current_text_index % 5 == 2:
            return self.rockystates_texts[self.current_text_index // 5]
        elif self.current_text_index % 5 == 3:
            return self.midwest_texts[self.current_text_index // 5]
        elif self.current_text_index % 5 == 4:
            return self.south_texts[self.current_text_index // 5]

    # This method changes the text of the questions
    def change_text(self, index):
        new_text = self.texts[index-1]
        self.label.config(text=new_text)
    
    # This method changes the text of the northeast button
    def change_northeast_text(self, index):
        new_text = self.northeast_texts[index-1]
        self.label.config(text=new_text)
    
    # This method changes the text of the westcoast button
    def change_westcoast_text(self, index):
        new_text = self.westcoast_texts[index-1]
        self.label.config(text=new_text)

    # This method changes the text of the rockystates button
    def change_rockystates_text(self, index):
        new_text = self.rockystates_texts[index-1]
        self.label.config(text=new_text)

    # This method changes the text of the midwest button
    def change_midwest_text(self, index):
        new_text = self.midwest_texts[index-1]
        self.label.config(text=new_text)

    # This method changes the text of the south button
    def change_south_text(self, index):
        new_text = self.south_texts[index-1]
        self.label.config(text=new_text)

    def open_results_page(self):
        # Hide the main window
        self.topLevel.withdraw()

        # Create the results window
        if self.test_value >= 23:
            master = tk.Toplevel(self.topLevel) #changed from test_page = GeoDialectTestPage()
            app = GeoDialectSouthPage(master)
        elif 18 <= self.test_value <= 22:
            master = tk.Toplevel(self.topLevel) #changed from test_page = GeoDialectTestPage()
            app = GeoDialectMidwestPage(master)
        elif 13 <= self.test_value <= 17:
            master = tk.Toplevel(self.topLevel) #changed from test_page = GeoDialectTestPage()
            app = GeoDialectRockyStatesPage(master)
        elif 8 <= self.test_value <=12:
            master = tk.Toplevel(self.topLevel) #changed from test_page = GeoDialectTestPage()
            app = GeoDialectWestCoastPage(master)
        elif self.test_value > 8:
            master = tk.Toplevel(self.topLevel) #changed from test_page = GeoDialectTestPage()
            app = GeoDialectNortheastPage(master)

        # Close the main window when the second window is closed
        topLevel.protocol("WM_DELETE_WINDOW", self.quit)
        topLevel = tk.Toplevel

class GeoDialectNortheastPage:
    def __init__(self, master):
        self.master = master
        self.master.title =("GeoDialect Results Page")
        self.master.geometry("800x600")

        self.title = tk.Label(self.master, text="I Declare You... A Northeasterner!", font=("Helvetica", 36))
        self.title.pack()

        self.img = Image.open("Northeast.png")
        self.img = self.img.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

class GeoDialectWestCoastPage:
    def __init__(self, master):
        self.master = master
        self.master.title =("GeoDialect Results Page")
        self.master.geometry("800x600")

        self.title = tk.Label(self.master, text="I Declare You... A West Coaster!", font=("Helvetica", 36))
        self.title.pack()

        self.img = Image.open("West_Coast.png")
        self.img = self.img.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

class GeoDialectRockyStatesPage:
    def __init__(self, master):
        self.master = master
        self.master.title =("GeoDialect Results Page")
        self.master.geometry("800x600")

        self.title = tk.Label(self.master, text="I Declare You... A Rocky Stater!", font=("Helvetica", 36))
        self.title.pack()

        self.img = Image.open("Rocky_States.png")
        self.img = self.img.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

class GeoDialectMidwestPage:
    def __init__(self, master):
        self.master = master
        self.master.title =("GeoDialect Results Page")
        self.master.geometry("800x600")

        self.title = tk.Label(self.master, text="I Declare You... A Midwesterner!", font=("Helvetica", 36))
        self.title.pack()

        self.img = Image.open("Midwest.png")
        self.img = self.img.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

class GeoDialectSouthPage:
    def __init__(self, master):
        self.master = master
        self.master.title =("GeoDialect Results Page")
        self.master.geometry("800x600")

        self.title = tk.Label(self.master, text="I Declare You... A Southerner!", font=("Helvetica", 36))
        self.title.pack()

        self.img = Image.open("Southerner.png")
        self.img = self.img.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)


root = tk.Tk()
app = GeoDialectHomePage(root)
root.mainloop()