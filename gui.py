from tkinter import *

# if __name__ == '__main__':
width = 400
height = 200

master = Tk()
master.geometry('500x250')
master.title('Morse Code')
master.resizable(0, 0)
# master.columnconfigure(0, weight=1)
# master.rowconfigure(1, weight=1)

sideBar = Frame(master, width = 200, height = 250, bg = 'black', pady = 10, bd = 10)
sideBar.grid(row = 0, column = 0)

mainFrame = Frame(master, width = 300, height= 250, bg = 'blue', bd = 10)
mainFrame.grid(row = 0, column = 1)

# button = Button(sideBar, text='End', width = 25, bg = "#95bdfc", fg = "#353542", activebackground = "#8289b5", border = 0) #command=r.destroy,
# # button.grid(row = 0, column = 0)
uwu = Button(mainFrame, width = 25)
uwu.grid(column= 0, row= 0)

master.mainloop()