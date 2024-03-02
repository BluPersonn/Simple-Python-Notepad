import tkinter as tk
window = tk.Tk()
window.title("Simple Sticky Notes!")
window.minsize(width = 1000, height = 300)
window.configure(background = "black")

currentFont = ("Consolas", 15)

textBox = tk.Text(background = "#252525", foreground = "white", width = 100, height = 25,font = currentFont)

def changeToConsolas():
    global textBox
    global currentFont
    currentFont = ("Consolas", 15)
    textBox.configure(font = currentFont)

def changeToComic():
    global textBox
    global currentFont
    currentFont = ("Comic Sans MS", 12)
    textBox.configure(font = currentFont)

def changeToTimes():
    global textBox
    global currentFont
    currentFont = ("Times New Roman", 17)
    textBox.configure(font = currentFont) 

saveSlot1, saveSlot2, saveSlot3 = "You don't have anything saved in this slot!", "You don't have anything saved in this slot!", "You don't have anything saved in this slot!"

def load(slot):
    global saveSlot1
    global saveSlot2
    global saveSlot3
    textBox.delete("1.0", tk.END)
    if slot == 1:
        textBox.insert("1.0", saveSlot1)
    elif slot == 2:
        textBox.insert("1.0", saveSlot2)
    elif slot == 3:
        textBox.insert("1.0", saveSlot3)

def save(slot, data):
    global saveSlot1
    global saveSlot2
    global saveSlot3
    if slot == 1:
        saveSlot1 = data
    elif slot == 2:
        saveSlot2 = data
    elif slot == 3:
        saveSlot3 = data

textBox.pack()
textBox.place(x = 135, y = 3)
fontLabel = tk.Label(text = "Font:", background = "black", foreground = "white").place(x = 5, y = 10)
savesLabel = tk.Label(text = "Saves:", background = "black", foreground = "white").place(x = 1250, y = 10)
consolasFontButton = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", command = changeToConsolas, text = "Consolas").place(x = 5, y = 30)
comicFontButton = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", command = changeToComic, text = "Comic Sans MS").place(x = 5, y = 60)
timesFontButton = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", command = changeToTimes, text = "Times New Roman").place(x = 5, y = 90)

saveButton1 = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", text = "Save to Slot 1", command = lambda: save(1, textBox.get("1.0", tk.END))).place(x = 1250, y = 30)
loadButton1 = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", text = "Load from Slot 1", command = lambda: load(1)).place(x=1250, y = 60)

saveButton2 = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", text = "Save to Slot 2", command = lambda: save(2, textBox.get("1.0", tk.END))).place(x = 1250, y = 90)
loadButton2 = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", text = "Load from Slot 2", command = lambda: load(2)).place(x=1250, y = 120)

saveButton3 = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", text = "Save to Slot 3", command = lambda: save(3, textBox.get("1.0", tk.END))).place(x = 1250, y = 150)
loadButton3 = tk.Button(activebackground = "white", activeforeground = "black", background= "black", foreground = "white", text = "Load from Slot 3", command = lambda: load(3)).place(x=1250, y = 180)

copyrightLabel = tk.Label(text = "© BluPersonn", background = "black", foreground = "white").place(x = 0, y = 675)

window.mainloop()