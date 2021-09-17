# Website-TC1001S
Videogames with python for TC1001S.

## Authors

- Juan Muniain Otero
- Federico Pérez Zorrilla
- Víctor Andrés Lepe Méndez

## Contributions

To enhance your gaming experience, the team decided to remaster three games included within the freegames package. Some of the changes made by each member are noted below:

### Juan:

**Pac man:** I introduced a board reminiscent of the original 1980 version (excluding the center spawn point for ghosts). I also added another ghost which spawns at the center of the board, and also changed pac-mans start position.

**Snake:** I decided to increase the snake speed by reducing the miliseconds taken to update its position.

**Cannon:** I added a scoring system similar to the one found in the pac-man game, so you can see how many targets you hit!

### Fede:

**Snake:** I made it so the snake does not die when touching a border, instead, it reappears on the other side of the map.

**Cannon:** I applied gravity effect to the targets, for this I also adjusted the horizontal speed.

### Victor:

**Pac man:** I changed the ghost speed from 1 to 2 spaces. Also changed the way ghost behave, ghost are now smarter using the original pacman AI (check source code comments for implementation details)

**Cannon:** Changed cannon ball speed to make the game more enjoyable, it's easier to play now.


## Website

On this website you can play various games with Python 3
- Snake (Remastered)
- Pacman (Remastered)
- Cannon (Remastered)
- Paint
- Memory

## Games

To play the games make sure to follow the next steps:
1. Have Python3 installed in your computer.
2. Have pip installed. To install pip, run this command via your terminal:
```
python3 get-pip.py
```
3. Have free games installed. To install this module, run the following command:
```
pip install freegames
```

## Installing on MobaXterm (Windows)

To install the required software, run the following commands:

1. apt-get install python3
2. apt-get install python3-tkinter
3. apt-get install python3-pip
4. pip3 install freegames
