# board-game-generator
A small program that genortates hexgrids
I made it to genorate a board game board for a board game design competition

Right now not the best implimentation, just a heads up.

Dependes on **PIL** or python imaging library

## Features
Makes an image like this:
![Full size](https://www.dropbox.com/s/8z0zy8tdqo4tq9r/image2.png?dl=1)
Cropped:![Cropped Image](https://i.ibb.co/zfgbhXd/image2.png)

### Supports:
- Biomes
- Weather arrow on water
- Details

### Other stuff:
- All images can be changed
- Background color (where no tiles are on the side) can be changed
- Any diamensions or size grid

## How to use
### Custom images
1. Place the _background images_ in there, included are the images: `desert.png`, `forest.png`, `ice.png`, `mountain.png`, `ocean bad.png`, `ocean.png`, `plains.png`, `forest.png`, and `savana.png` (Make sure that the images that you put here are seemless) (may be any height and width, but note the images are not scaled, so these will need to be scaled if `HEXSIZE` is altered)
2. Edit `gridTest.py` and the list `picsUnloaded` should be the list of images that you wish to use for the background
3. Place the _detail images_ in there, included are the images: `flag.png`, `flag2.png`, `gold.png`, `lumber.png`, `metal.png`, `stone.png`, `sugar.png`, and `building1.png`, `building2.png`,`building3.png` ... `building9.png`, `building10.png`
4. Edit the `gridTest.py` and the list `detailsUnloaded` should be the list of the images that you wish to use for details
The index (item number minus one) that the items are in `picsUnloaded` and `detailsUnloaded` lists are the index that programs reference the varrious thing by

### Make a map data
1. Place three image that provide the information of the map
	- `world map.png`
		- The only part of the image that matters is the red channel (the other channels you can use to help you understand what is what if you want, but will be ingnored)
		- The value of the red channel (0-255) will be divided by 16 and rounded down. That will be the biome index used.
		- The number divided by (to allow for more biomes) can be altered by changing the last number in line `19` of `map reader.py` 
	- `weather.png`
		- read as **HSV**
		- saturation is ignored
		- value is the strength of the wind arrow (chunks broken into)
			- The value of the image divided in to 4 64-sized chunks is the strength
			- That can be changed b changing the nuumber line `80` of `map reader.png`
	- `details.png`
		- The this is poorly designed and will probably not be optimal for your use case so you might want to rewrite it (`map reader.py` lines `23` to `39`)
		- If its white
			- detail is 0 (nothing)
		- If red is between 250-255 (and not white)
			- it will make a detail 9 to 19 depending on blue value
		- If red is between 153-249
			- it will make a detail 3-8 depending on green value
		- If red is between 128-152
			- Will make a detail 2
		- If red is between 0-127
			- Will make detail 1
	- These images images must be the size of the board in hexes (or larger, will just get part of them ignored)
2. Set the values of `SIZEX` and `SIZEY` in `map reader.py` to the dimensions of the board
3. Run the program `map reader.py`
4. Copy everything blasted into the terminal
5. Paste it in the program `gridTest.py` replacing lines `13`-`247`
6. Remove the comma `,` at the end
7. Add a closing square braket `]` at the end
Should look simular to how it looked before you pasted it hopefully

### Changing varrious things:
Do What is listed in the program `gridTest.py`
#### Image resolution
Alter `HEXSIZE`
This is the number of pixels in the height of a hex
Note: you might want to scale up or down background images to match
#### Land tile boarders
Alter `BRIGHTNESSSIZE`
This changes the width (relative to hexsize) of the lightened or darkened edges
Alter `BRIGHTNESSPOWER`
This changes how stong the effect of the lightening and darkening has on the color
#### Weather arrows
Alter `TRIWIDTH`
This changes the width (relative to hexsize) of the arrows
Alter `WINDPOWER`
This changes how strong the effect of the darkening that the darkening has on the arrows
#### Ocean tile boarders
Alter `WATERBORDSIZE`
This changes the width (relative to hexsize) of the darkened edges
Alter `WATERBORDPOWER`
This changes how stong the effect of the darkening has on the color
#### Color of background with out tiles
Alter line `318`

### Creating an Image
1. Run `gridTest.py`
2. Wait for it to finish (single theaded so will take a while) (shows progress in the terminal)
3. The image should open in you defualt image viewer 
