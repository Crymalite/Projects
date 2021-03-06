# Python Version 2.7.3
# File: minesweeper.py

from tkinter import *
import tkMessageBox
import random
import math
from collections import deque

class Minesweeper:

    def __init__(self, master):

        # import images
        self.tile_plain = PhotoImage(file = "tile_plain.gif")
        self.tile_clicked = PhotoImage(file = "tile_clicked.gif")
        self.tile_mine = PhotoImage(file = "tile_mine.gif")
        self.tile_flag = PhotoImage(file = "tile_flag.gif")
        self.tile_wrong = PhotoImage(file = "tile_wrong.gif")
        self.tile_no = []
        for x in range(1, 9):
            self.tile_no.append(PhotoImage(file = "tile_"+str(x)+".gif"))

        # set up frame
        frame = Frame(master)
        frame.pack()

        # show "Minesweeper" at the top
        self.label1 = Label(frame, text="Skull Finder")
        self.label1.grid(row = 0, column = 0, columnspan = 10)

        # create flag and clicked tile variables
        self.flags = 0
        self.correct_flags = 0
        self.clicked = 0

        # create buttons
        self.buttons = dict({})
        self.mines = 0
        self.minelist = dict({})
        x_coord = 1
        y_coord = 0
        worked = False
        randy = random.randrange(1, 42)
        for x in range(1, 8):
            randy = random.randrange(1, 42)
            while self.minelist.has_key(randy) == True:
                randy = random.randrange(1, 42)
            
            if self.minelist.has_key(randy) == False:
                self.minelist[randy] = True
                worked = True
            else:
                worked = False
            
        for x in range(0, 49):
            mine = 0
            # tile image changeable for debug reasons:
            gfx = self.tile_plain
            # currently random amount of mines
            if self.minelist.has_key(x):
                mine = 1
                self.mines += 1
            # 0 = Button widget
            # 1 = if a mine y/n (1/0)
            # 2 = state (0 = unclicked, 1 = clicked, 2 = flagged)
            # 3 = button id
            # 4 = [x, y] coordinates in the grid
            # 5 = nearby mines, 0 by default, calculated after placement in grid
            self.buttons[x] = [ Button(frame, image = gfx),
                                mine,
                                0,
                                x,
                                [x_coord, y_coord],
                                0 ]
            self.buttons[x][0].bind('<Button-1>', self.lclicked_wrapper(x))
            self.buttons[x][0].bind('<Button-3>', self.rclicked_wrapper(x))

            # calculate coords:
            y_coord += 1
            if y_coord == 7:
                y_coord = 0
                x_coord += 1
        
        # lay buttons in grid
        for key in self.buttons:
            self.buttons[key][0].grid( row = self.buttons[key][4][0], column = self.buttons[key][4][1] )

        # find nearby mines and display number on tile
        for key in self.buttons:
            nearby_mines = 0
            if self.check_for_mines(key-6):
                nearby_mines += 1
            if self.check_for_mines(key-7):
                nearby_mines += 1
            if self.check_for_mines(key-8):
                nearby_mines += 1
            if self.check_for_mines(self.getnextl(key)):
                nearby_mines += 1
            if self.check_for_mines(self.getnextr(key)):
                nearby_mines += 1
            if self.check_for_mines(key+6):
                nearby_mines += 1
            if self.check_for_mines(key+7):
                nearby_mines += 1
            if self.check_for_mines(key+8):
                nearby_mines += 1
            # store mine count in button data list
            self.buttons[key][5] = nearby_mines
            #if self.buttons[key][1] != 1:
            #    if nearby_mines != 0:
            #        self.buttons[key][0].config(image = self.tile_no[nearby_mines-1])

        #add mine and count at the end
        self.label2 = Label(frame, text = "Mines: "+str(self.mines))
        self.label2.grid(row = 11, column = 0, columnspan = 5)

        self.label3 = Label(frame, text = "Flags: "+str(self.flags))
        self.label3.grid(row = 11, column = 4, columnspan = 5)

    ## End of __init__

    def check_for_mines(self, key):
        try:
            if self.buttons[key][1] == 1:
                return True
        except KeyError:
            pass

    def lclicked_wrapper(self, x):
        return lambda Button: self.lclicked(self.buttons[x])

    def rclicked_wrapper(self, x):
        return lambda Button: self.rclicked(self.buttons[x])

    def lclicked(self, button_data):
        if self.can_use(button_data[3]) == False:
            return False
        elif button_data[3] <= 7:
            self.victory()
        elif button_data[1] == 1: #if a mine
            # show all mines and check for flags
            for key in self.buttons:
                if self.buttons[key][1] != 1 and self.buttons[key][2] == 2:
                    self.buttons[key][0].config(image = self.tile_wrong)
                if self.buttons[key][1] == 1 and self.buttons[key][2] != 2:
                    self.buttons[key][0].config(image = self.tile_mine)
            # end game
            self.gameover()
        else:
            #change image
            if button_data[5] == 0:
                button_data[0].config(image = self.tile_clicked)
                self.clear_empty_tiles(button_data[3])
            else:
                button_data[0].config(image = self.tile_no[button_data[5]-1])
            # if not already set as clicked, change state and count
            if button_data[2] != 1:
                button_data[2] = 1
                self.clicked += 1
            if self.clicked == 100 - self.mines:
                self.victory()

    def rclicked(self, button_data):
        # if not clicked
        if button_data[2] == 0:
            button_data[0].config(image = self.tile_flag)
            button_data[2] = 2
            button_data[0].unbind('<Button-1>')
            # if a mine
            if button_data[1] == 1:
                self.correct_flags += 1
            self.flags += 1
            self.update_flags()
        # if flagged, unflag
        elif button_data[2] == 2:
            button_data[0].config(image = self.tile_plain)
            button_data[2] = 0
            button_data[0].bind('<Button-1>', self.lclicked_wrapper(button_data[3]))
            # if a mine
            if button_data[1] == 1:
                self.correct_flags -= 1
            self.flags -= 1
            self.update_flags()

    def check_tile(self, key, queue):
        try:
            if self.buttons[key][2] == 0:
                if self.buttons[key][5] == 0:
                    self.buttons[key][0].config(image = self.tile_clicked)
                    queue.append(key)
                    self.buttons[key][2] = 1
                    self.clicked += 1
                else:
                    self.buttons[key][0].config(image = self.tile_no[self.buttons[key][5]-1])
                    self.buttons[key][2] = 1
                    self.clicked += 1
        except KeyError:
            pass

    def check_clicked(self, key):
        try:
            if self.buttons[key][2] == 0:
                return False
            elif self.buttons[key][2] == 1:
                return True
        except KeyError:
            return False

    def can_use(self, key):
        if key >= 42:
            return True
        else:
            if self.check_clicked(key-6) == True:
                return True
            elif self.check_clicked(key-7) == True:
                return True
            elif self.check_clicked(key-8) == True:
                return True
            elif self.check_clicked(key-1) == True:
                return True
            elif self.check_clicked(key+1) == True:
                return True
            elif self.check_clicked(key+6) == True:
                return True
            elif self.check_clicked(key+7) == True:
                return True
            elif self.check_clicked(key+8) == True:
                return True
            else:
                return False

    def getnextl(self, key):
        a = math.floor(key / 7)
        b = math.floor((key - 1) / 7)
        if a != b:
            return key
        else:
            return key - 1

    def getnextr(self, key):
        a = math.floor(key / 7)
        b = math.floor((key + 1) / 7)
        if a != b:
            return key
        else:
            return key + 1

    def clear_empty_tiles(self, main_key):
        queue = deque([main_key])

        while len(queue) != 0:
            key = queue.popleft()
            #self.check_tile(key-6, queue)      #top right
            self.check_tile(key-7, queue)     #top middle
            #self.check_tile(key-8, queue)     #top left
            self.check_tile(self.getnextl(key), queue)      #left
            self.check_tile(self.getnextr(key), queue)      #right
            #self.check_tile(key+9, queue)      #bottom right
            #self.check_tile(key+10, queue)     #bottom middle
            #self.check_tile(key+11, queue)     #bottom left
    
    def gameover(self):
        tkMessageBox.showinfo("Game Over", "You Lose!")
        global root
        root.destroy()

    def victory(self):
        tkMessageBox.showinfo("Game Over", "You Win!")
        global root
        root.destroy()

    def update_flags(self):
        self.label3.config(text = "Flags: "+str(self.flags))

### END OF CLASSES ###

def main():
    global root
    # create Tk widget
    root = Tk()
    # set program title
    root.title("Skull Finder")
    # create game instance
    minesweeper = Minesweeper(root)
    # run event loop
    root.mainloop()

if __name__ == "__main__":
    main()
