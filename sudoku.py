import games
from graphics import *

def main():
    sudokuWindow = GraphWin("Sudo", 470,470)
    sudokuWindow.setBackground("white")
   
    gameScreen = emptyGrid()
    game = cleanUp(games.game2)
    addGameValuesToList(game,gameScreen)

  
    for element in gameScreen:
        element.draw(sudokuWindow)

    matrixWindow, matrixScreenList = createMatrixToDraw("Matrices", 270,720) # handles creation and drawing

    sudokuWindow.getMouse()
    sudokuWindow.close()
    matrixWindow.getMouse()
    matrixWindow.close()

def emptyGrid():
    grid = []
    return addGrid(grid)

# def createMatrixToDraw2(window:GraphWin):
#     window.setBackground("white")
#     return createMatrixGrid(window.getWidth(),window.getHeight())

def createMatrixToDraw(name,width,height):
    window = GraphWin(name, width,height)
    window.setBackground("white")
    screen = createMatrixGrid(width,window.height)
    for element in screen:
        element.draw(window)
    return window, screen
    # return window, createMatrixGrid(width,window.height)


def addGrid(grid:list):
    box = Rectangle(Point(10,10),Point(460,460))
    box.setWidth(5)
    grid.append(box)
    for i in range(1,9):
        lineX = Line(Point(10,(10+50*i)),Point(460,(10+50*i)))
        lineY = Line(Point((10+50*i),10),Point((10+50*i),460))
        if(i%3==0):
            lineX.setWidth(3)
            lineY.setWidth(3)
        grid.append(lineX)
        grid.append(lineY)

    return grid

def createMatrixGrid(width,height):
    grid = []
    cellWidth = 25
    legendX = Rectangle(Point(10+cellWidth,10),Point(width-10,10+cellWidth))
    legendX.setWidth(2)
    legendX.setOutline(color_rgb(0,0,255))
    grid.append(legendX)
    legendC = Rectangle(Point(10,10+cellWidth),Point(35,height-(10+cellWidth*18)))
    legendC.setWidth(2)
    legendC.setOutline(color_rgb(0,75,0))
    grid.append(legendC)
    cBox = Rectangle(Point(10+cellWidth,10+cellWidth),Point(width-10,height-(10+cellWidth*18)))
    cBox.setOutline(color_rgb(0,75,0))
    cBox.setWidth(2)
    grid.append(cBox)
    legendR = Rectangle(Point(10,10+cellWidth*10),Point(35,height-(10+cellWidth*9)))
    legendR.setWidth(2)
    legendR.setOutline(color_rgb(0,150,0))
    grid.append(legendR)
    rBox = Rectangle(Point(10+cellWidth,10+cellWidth*10),Point(width-10,height-(10+cellWidth*9)))
    rBox.setOutline(color_rgb(0,150,0))
    rBox.setWidth(2)
    grid.append(rBox)
    legendA = Rectangle(Point(10,10+cellWidth*19),Point(35,height-10))
    legendA.setWidth(2)
    legendA.setOutline(color_rgb(0,225,0))
    grid.append(legendA)
    aBox = Rectangle(Point(10+cellWidth,10+cellWidth*19),Point(width-10,height-10))
    aBox.setOutline(color_rgb(0,225,0))
    aBox.setWidth(2)
    grid.append(aBox)

    for x in range(0,29):
        lineX = Line(Point(10,(10+cellWidth*x)),Point(width-10,(10+cellWidth*x)))
        grid.append(lineX)
    
    for i in range(0,11):
        lineY = Line(Point((10+cellWidth*i),10),Point((10+cellWidth*i),height-10))
        grid.append(lineY)

    return grid

def cleanUp(game:str):
    validCharacters = ["1","2","3","4","5","6","7","8","9"]
    pure = ""
    for char in game:
        try:
            _ = validCharacters.index(char)
            pure = f"{pure}{char}"
        except ValueError:
           pure = f"{pure} "

    return pure


def addGameValuesToList(game:str,list:list):
    gameObj = {"stringGame":game,"matrix":games.matrix3}

    for index, char in enumerate(gameObj["stringGame"]):
        col = (index)%9
        row = (int)((index)/9)
        if char != " ":
            # inverting the game starting position into rows, columns and segments/areas. 
            columns = gameObj["matrix"][f"c{col+1}"]
            for element in columns:
               if(char == element):
                inx = columns.index(char)
                columns[inx] = " "
            rows = gameObj["matrix"][f"r{row+1}"]
            for element in rows:
               if(char == element):
                inx = rows.index(char)
                rows[inx] = " "
        
            area = gameObj["matrix"][f"a{getAreaNumber(col,row)}"]
            try:
                inx = area.index(char)
                area[inx] = " "
            except:
                pass

        x = 35 + col*50 
        y = 35 + row*50
        list.append(Text(Point(x,y),char))
    
    printMatrix(gameObj)

# def updateGameMatrix() 

def printMatrix(gameObj):
    print("      1    2    3    4    5    6    7    8    9")
    print("      |    |    |    |    |    |    |    |    |")
    for index, entry in enumerate(gameObj["matrix"]):
        print(f"{entry}: {gameObj['matrix'][entry]}")
        if (index+1)%9==0:
            print("    |=|----|----|----|----|----|----|----|----|=|")

def addGameValuesToListOldGood(game:str,list:list):
    gameObj = {"stringGame":game,"matrix":games.matrix3}

    for index, char in enumerate(gameObj["stringGame"]):
        col = (index)%9
        row = (int)((index)/9)
        if char != " ":
            gameObj["matrix"][f"c{col+1}"].remove(char)
            gameObj["matrix"][f"r{row+1}"].remove(char)
            area = gameObj["matrix"][f"a{getAreaNumber(col,row)}"]
            try:
                _ = area.index(char)
                area.remove(char)
            except:
                pass

        x = 35 + col*50 
        y = 35 + row*50
        list.append(Text(Point(x,y),char))
    
    for entry in gameObj["matrix"]:
        print(f"{entry}: {gameObj['matrix'][entry]}")

def getAreaNumber(x:str,y:str):
    if int(x)<=2: 
        if int(y)<=2:
            return "1"
        elif int(y)<=5:
            return "4"
        else:
            return "7"
    elif int(x)<=5:
        if int(y)<=2:
            return "2"
        elif int(y)<=5:
            return "5"
        else:
            return "8"
    else:
        if int(y)<=2:
            return "3"
        elif int(y)<=5:
            return "6"
        else:
            return "9"

if __name__ == "__main__":
    main()