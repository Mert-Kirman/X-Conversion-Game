# +X- Game

Python program which simulates a game called the +x- game. This is a single player game which is played on a board; where 

the player will enter board size, place "+" signs on the board and try to turn all squares with the "+" sign to "-" by 

targeting the squares and changing their signs. The x name is because the signs should change in an x pattern centered 

around the targeted square.

## How It Works

There are two phases to the +X- Game: 

- In the first phase the player sets a size for the game board which consists of "-" in all the squares. Then player 

decides how many "+" signs to place on the board, meaning player creates a custom board before starting the game. 

- In the second phase of the game, the player tries to turn all squares with the "+" sign to "-" by targeting 

the squares and changing their signs. The caveat here is that targeted square is not the only square to be replaced by the

opposite sign but upper and lower corners of the target square also are reversed hence the name +X-. The player continues targeting

and replacing "+" with "-" and vice versa until there are no "+" signs left on the board.

### Prerequisites

An IDE or text editor to run the python code.

## Running the tests

Player will enter the size of the game board in the console. After this, coordinates for the target square to place "+" sign 

will be entered in the form of y-coordinates (vertical) and x-coordinates (horizontal) with a whitespace between them as shown below:

&emsp;&ensp; Y X

- 2 5
- 4 3
- 2 3

and so on.

In the second phase of the game player will start replacing "+" sign with "-" sign by choosing a target square. The inputs 

for this target square will be the same as previously discussed. The player can exit the game by typing "exit" in the console.

- Limitations: A valid board size is between 5 and 9, both inclusive.

