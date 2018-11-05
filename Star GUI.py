# Date: October 25, 2017
# Author: Edward Tang
# Purpose: This program is designed to prompt the user for their preferences for a shape's pattern, type, size and colour. It will then display the shape (made from asterisks) based on the user's selections.
# Input: Mouse, Keyboard
# Output: Screen
# ==============================================================================================================================================================================================================

from tkinter import *

main = Tk()
main.title("Shape Generator")
main.resizable(False,False)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window with four labels and a close button.
# Input: Title name, four string values and the width and height of the window
# Output: Screen
# ========================================================================================================

def window4Labels(title,text1,text2,text3,text4,width,height):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height,bg="#fcfcfc")
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    Label(window,text=text1,font=("Arial",12,"bold"),bg="#fcfcfc").place(x=5,y=5)
    Label(window,text=text2,font=("Arial",10,"normal"),bg="#fcfcfc").place(x=5,y=30)
    Label(window,text=text3,font=("Arial",10,"normal"),bg="#fcfcfc").place(x=5,y=55)   
    Label(window,text=text4,font=("Arial",10,"normal"),bg="#fcfcfc").place(x=5,y=80)
    Button(window,text="Close",font=("Arial",10,"bold"),relief=FLAT,cursor="hand2",command=lambda:window.destroy(),bg="tomato2").place(x=width-60,y=height-40)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window with three labels and a close button.
# Input: Title name, three string values and the width and height of the window
# Output: Screen
# =============================================================================================================

def window3Labels(title,text1,text2,text3,width,height):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height,bg="#fcfcfc")
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    Label(window,text=text1,font=("Arial",10,"normal"),bg="#fcfcfc",wraplength=425,justify="left").place(x=5,y=5)
    Label(window,text=text2,font=("Arial",10,"normal"),bg="#fcfcfc",wraplength=425,justify="left").place(x=5,y=50)
    Label(window,text=text3,font=("Arial",10,"normal"),bg="#fcfcfc",wraplength=320,justify="left").place(x=5,y=95)
    Button(window,text="Close",font=("Arial",10,"bold"),relief=FLAT,cursor="hand2",command=lambda:window.destroy(),bg="tomato2").place(x=width-67.5,y=height-47.5)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a solid square, when given a shape size and Text widget.
# Input: Size of shape, name of Text widget
# Output: Screen (in Text widget)
# ==================================================================================================================

def solidSquare(canvas):
    shapeSize = sSize.get()
    for count in range(1, shapeSize + 1):
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a solid triangle, when given a shape size and Text widget.
# Input: Size of shape, name of Text widget
# Output: Screen (in Text widget)
# ==========================================================================================================================

def solidTriangle(canvas):
    shapeSize = sSize.get()
    shapeWidth=0
    for count in range(1, shapeSize + 1):
        shapeWidth = shapeWidth + 1
        for count in range(1, shapeWidth + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a solid diamond, when given an ODD shape size and Text widget.
# Input: Size of shape, name of Text widget
# Output: Screen (in Text widget)
# ==============================================================================================================================

def solidDiamond(canvas):      
    shapeSize = sSize.get()
    spaceWidth = shapeSize // 2 + 1
    shapeWidth = -1
    for count in range(1, shapeSize // 2 + 2):           
        spaceWidth = spaceWidth - 1
        shapeWidth = shapeWidth + 2
        for count in range(1, spaceWidth + 1):
            canvas.insert(END,"  ")
        for count in range(1, shapeWidth + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")            
    for count in range(1, shapeSize // 2 + 1):           
        spaceWidth = spaceWidth + 1
        shapeWidth = shapeWidth - 2
        for count in range(1, spaceWidth + 1):
            canvas.insert(END,"  ")
        for count in range(1, shapeWidth + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a solid cross, when given a shape size and Text widget.
# Input: Size of shape, name of Text widget
# Output: Screen (in Text widget)
# ==========================================================================================================================

def solidCross(canvas):        
    shapeSize = sSize.get()
    for count in range(1, shapeSize + 1):            
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"  ")
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")        
    for count in range(1, shapeSize + 1):
        for count in range(1, shapeSize * 3 + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")
    for count in range(1, shapeSize + 1):   
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"  ")
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")
    canvas.delete("end-1c linestart")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a hollow square, when given a shape size and Text widget.
# Input: Size of shape, name of Text widget
# Output: Screen (in Text widget)
# ==========================================================================================================================
    
def hollowSquare(canvas):
        shapeSize = sSize.get()
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")
        if shapeSize > 1:
            for count in range(1, shapeSize - 1):
                canvas.insert(END,"* ")
                for count in range(1, shapeSize - 1):
                    canvas.insert(END,"  ")
                canvas.insert(END,"*\n")
            for count in range(1, shapeSize + 1):
                canvas.insert(END,"* ")
            canvas.insert(END,"\n")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a hollow triangle, when given a shape size and Text widget.
# Input: Size of shape, name of Text widget
# Output: Screen (in Text widget)
# ==========================================================================================================================
            
def hollowTriangle(canvas):
    shapeSize = sSize.get()
    shapeWidth=0
    for count in range(1, shapeSize):
        shapeWidth = shapeWidth + 1
        canvas.insert(END,"* ")
        if shapeWidth - 2 > 0:
            for count in range(1, shapeWidth - 1):
                canvas.insert(END,"  ")
        if shapeWidth > 1:
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")
    for count in range(1, shapeWidth + 2):
        canvas.insert(END,"* ")
    canvas.insert(END,"\n")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a hollow diamond, when given an ODD shape size and Text widget.
# Input: Size of shape (odd number), name of Text widget
# Output: Screen (in Text widget)
# =============================================================================================================================

def hollowDiamond(canvas):
        shapeSize = sSize.get()
        spaceWidth = shapeSize - shapeSize // 2
        shapeWidth = -1
        for count in range(1, shapeSize // 2 + 2):
            spaceWidth = spaceWidth - 1
            shapeWidth = shapeWidth + 2
            for count in range(1, spaceWidth + 1):
                canvas.insert(END,"  ")
            canvas.insert(END,"* ")
            if shapeWidth > 1:
                for count in range(1, shapeWidth - 1):
                    canvas.insert(END,"  ")
                canvas.insert(END,"* ")
            canvas.insert(END,"\n")
        for count in range(1, shapeSize // 2 + 1):
            spaceWidth = spaceWidth + 1
            shapeWidth = shapeWidth - 2
            for count in range(1, spaceWidth + 1):
                canvas.insert(END,"  ")
            canvas.insert(END,"* ")
            if shapeWidth > 1:
                for count in range(1, shapeWidth - 1):
                    canvas.insert(END,"  ")
                canvas.insert(END,"* ")
            canvas.insert(END,"\n")    

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to use asterisks to produce a hollow cross, when given a shape size and Text widget.
# Input: Size of shape (odd number), name of Text widget
# Output: Screen (in Text widget)
# =============================================================================================================================

def hollowCross(canvas):
    shapeSize = sSize.get()
    #Topmost line on the cross
    for count in range(1, shapeSize + 1):
        canvas.insert(END,"  ")
    for count in range(1, shapeSize + 1):
        canvas.insert(END,"* ")
    canvas.insert(END,"\n")
    #Top part of the cross with hollow centre        
    for count in range(1, shapeSize):
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"  ")        
        canvas.insert(END,"* ")        
        if shapeSize > 2:            
            for count in range(1, shapeSize - 1):
                canvas.insert(END,"  ")
        canvas.insert(END,"*\n")
    #Topmost line of cross centre
    if shapeSize > 1:        
        for count in range(1, shapeSize + 2):
            canvas.insert(END,"* ")        
        for count in range(1, shapeSize - 1):
            canvas.insert(END,"  ")
        for count in range(1, shapeSize + 2):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")
    #Middle lines of cross centre     
    for count in range(1, shapeSize - 1):
        canvas.insert(END,"* ")
        if shapeSize > 2:
            for count in range(1, shapeSize * 3 - 1):
                canvas.insert(END,"  ")
        canvas.insert(END,"*\n")
    if shapeSize == 1:
        canvas.insert(END,"* ")
        canvas.insert(END,"  ")
        canvas.insert(END,"*\n")
    #Bottom-most line of cross centre
    if shapeSize > 1:        
        for count in range(1, shapeSize + 2):
            canvas.insert(END,"* ")
        for count in range(1, shapeSize - 1):
            canvas.insert(END,"  ")
        for count in range(1, shapeSize + 2):
            canvas.insert(END,"* ")
        canvas.insert(END,"\n")
    #Bottom part of the cross with hollow centre        
    for count in range(1, shapeSize):        
        for count in range(1, shapeSize + 1):
            canvas.insert(END,"  ")            
        canvas.insert(END,"* ")        
        if shapeSize > 2:           
            for count in range(1, shapeSize - 1):
                canvas.insert(END,"  ")                
        canvas.insert(END,"*\n")
    #Bottom-most line on the cross
    for count in range(1, shapeSize + 1):
        canvas.insert(END,"  ")
    for count in range(1, shapeSize + 1):
        canvas.insert(END,"* ")

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to clear the contents of a given Text widget.
# Input: Text widget
# Output: Screen (Text widget is cleared)
# ==================================================================================
    
def clearShape(canvas):
    canvas.config(state=NORMAL)
    canvas.delete(1.0,END)
    canvas.config(state=DISABLED)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to receive a set amount of option values (for Radiobutton widgets, Slider widgets, etc.) and restore them to default values. It will also receive a Text widget and clear its contents.
# Input: Four option values and a Text widget
# Output: Screen
# ==================================================================================

def setDefaults(option1,option2,option3,option4,canvas):
    option1.set(value=1)
    option2.set(value=1)
    option3.set(value=10)
    option4.set(value="000000")
    output.set(value="")
    clearShape(canvas)
    
# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to check if a user-inputted string value corresponds to a valid hexadecimal value.
# Input: String value
# Output: True/False according to the validity of the string as a hexadecimal value
# ======================================================================================================================

def checkHex(colour):
    validColours = "0123456789abcdefABCDEF"
    if len(colour.get()) == 6:
        for char in colour.get():
            if not char in validColours:
                return False
            else:
                continue
        return True
    else:
        return False

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed toggle a Text widget background between a white and black background (day and night modes).
# Input: Menu widget name, Text widget name
# Output: Screen (Text widget background colour is changed)
# ===============================================================================================================================

def nightModeToggle(menu,textBox):
    if exposureState.get() == "Bright":
        textBox.config(bg="black")
        menu.entryconfigure(1,label="Toggle Night Mode (ON)")
        exposureState.set("Dark")
    else:
        textBox.config(bg="white")
        menu.entryconfigure(1,label="Toggle Night Mode (OFF)")
        exposureState.set("Bright")        
        

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to take selected shape pattern, type, size and colour preferences and display an asterisk shape based on them in a Text widget. It will also perform checks before producing the shake
#          (odd number for diamond patterns, valid hex colour input) and display any errors in a Label widget.
# Input: Shape pattern, type, size, colour, Text widget name, Label widget name
# Output: Screen
# ==========================================================================================================================================================================================================================
    
def drawShape(canvas):
    clearShape(canvas)
    shapeWidth = 0
    output.set("")
    if shapePattern.get() == 3 and sSize.get() % 2 == 0:
        output.set("ERROR: Size of diamond must be odd")
    else:
        #Check if hex colour input is valid; if not, default the shape colour to black
        if checkHex(shapeColour) == True:
            canvas.config(state=NORMAL,fg=str("#"+shapeColour.get()))
        else:
            output.set("ERROR: Invalid colour code")
            canvas.config(state=NORMAL,fg="#000000")
        if shapePattern.get() == 1 and shapeType.get() == 1:
            solidSquare(canvas)            
        elif shapePattern.get() == 2 and shapeType.get() == 1:
            solidTriangle(canvas) 
        elif shapePattern.get() == 3 and shapeType.get() == 1:
            solidDiamond(canvas)
        elif shapePattern.get() == 4 and shapeType.get() == 1:
            solidCross(canvas)            
        elif shapePattern.get() == 1 and shapeType.get() == 2:
            hollowSquare(canvas)
        elif shapePattern.get() == 2 and shapeType.get() == 2:
            hollowTriangle(canvas)
        elif shapePattern.get() == 3 and shapeType.get() == 2:
            hollowDiamond(canvas)
        elif shapePattern.get() == 4 and shapeType.get() == 2:
            hollowCross(canvas)
    canvas.config(state=DISABLED)

#MAIN CODE

sSize = IntVar()
sSize.set(10)
shapePattern = IntVar()
shapePattern.set(1)
shapeType = IntVar()
shapeType.set(1)
exposureState = StringVar()
exposureState.set("Bright")
output = StringVar()
shapeColour = StringVar()
shapeColour.set("000000")

#Option Header Labels
Label(main,text="Shape",font=("Arial",11,"bold"),bg="#fcfcfc").place(x=15,y=5)
Label(main,text="Type",font=("Arial",11,"bold"),bg="#fcfcfc").place(x=100,y=5)
Label(main,text="Size",font=("Arial",11,"bold"),bg="#fcfcfc").place(x=67.5,y=115)
Label(main,text="Colour (hex)",font=("Arial",11,"bold"),bg="#fcfcfc").place(x=42.5,y=180)

#Shape Pattern Radiobuttons
Radiobutton(main,text="Square",font=("Arial",10,"normal"),bg="#fcfcfc",variable=shapePattern,value=1).place(x=15,y=25)
Radiobutton(main,text="Triangle",font=("Arial",10,"normal"),bg="#fcfcfc",variable=shapePattern,value=2).place(x=15,y=45)
Radiobutton(main,text="Diamond",font=("Arial",10,"normal"),bg="#fcfcfc",variable=shapePattern,value=3).place(x=15,y=65)
Radiobutton(main,text="Cross",font=("Arial",10,"normal"),bg="#fcfcfc",variable=shapePattern,value=4).place(x=15,y=85)

#Shape Type Radiobuttons
Radiobutton(main,text="Solid",font=("Arial",10,"normal"),bg="#fcfcfc",variable=shapeType,value=1).place(x=100,y=25)
Radiobutton(main,text="Hollow",font=("Arial",10,"normal"),bg="#fcfcfc",variable=shapeType,value=2).place(x=100,y=45)

#Shape Size Scale
Scale(main,variable=sSize,orient="horizontal",bg="#fcfcfc",bd=0,highlightthickness=0,cursor="hand2",length=150,from_=1,to=20).place(x=15,y=132)

#Hex Colour Entry & Label
Label(main,text="#",font=("Arial",12,"bold"),bg="#fcfcfc").place(x=47.5,y=204)
entry = Entry(main, textvariable=shapeColour,font="Arial",bg="#d6d6d6",width=6,relief=FLAT)
entry.place(x=64.5,y=205)

#"Canvas/Background" Text
canvas = Text(main,bd=2,relief=GROOVE,height=60,width=120,bg="white")
canvas.place(x=190,y=10)
canvas.config(state=DISABLED)

#Error Output Label
outputText = Label(main,textvariable=output,font=("Arial",9,"normal"),bg="#fcfcfc",fg="red3",wraplength=170,justify="left").place(x=17.5,y=360)

#"Draw Shape", "Delete Shape" & "Exit" Buttons
Button(main,text="Draw Shape",width=14,height=1,font=("Arial",12,"bold"),relief=FLAT,bg="chartreuse3",command=lambda:drawShape(canvas)).place(x=15,y=240)
Button(main,text="Delete Shape",width=14,height=1,font=("Arial",12,"bold"),relief=FLAT,bg="tomato2",command=lambda:clearShape(canvas)).place(x=15,y=280)
Button(main,text="Exit",width=14,height=1,font=("Arial",12,"bold"),bg="#9b9b9b",relief=FLAT,command=lambda:main.destroy()).place(x=15,y=320)

menu = Menu(main)

#"File" Menu
fileMenu = Menu(menu,tearoff=0)
fileMenu.add_command(label="Restore Defaults",command=lambda:setDefaults(shapePattern, shapeType, sSize, shapeColour,canvas))
fileMenu.add_command(label="Toggle Night Mode (OFF)", command=lambda:nightModeToggle(fileMenu,canvas))
fileMenu.add_command(label="Exit",command=lambda:main.destroy())
menu.add_cascade(label="File", menu=fileMenu)

#"Help" Menu
helpMenu = Menu(menu,tearoff=0)
helpMenu.add_command(label="About",command=lambda:window4Labels("About","Shape Generator","Version: 2.0","Author: Edward Tang","E-Mail: 335433173@gapps.yrdsb.ca",300,110))
helpMenu.add_command(label="Instructions",command=lambda:window3Labels("Instructions",
"Select your shape pattern, type, size and colour using the options available on the left. Defaults are square, solid, 10 and black respectively.",
"The size ranges from 1-20, but for diamond shapes, the size must be an odd number.",
"Click the 'Draw Shape' button to generate your shape, or click the 'Delete Shape' button to erase your shape.",440,150))
menu.add_cascade(label="Help", menu=helpMenu)

main.config(width=1165,height=985,menu=menu,bg="#fcfcfc")

mainloop()
