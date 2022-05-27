from PIL import Image

SIZEX = 100
SIZEY = 75
IMAGE = "world map.png"
WIND = "weather.png"
DETAIL = "details.png"

MAP = Image.open(IMAGE).load()
MULT = ((Image.open(IMAGE).size[1])/SIZEY,Image.open(IMAGE).size[0]/SIZEX)
WINDMAP = Image.open(WIND).load()
DETAILS = Image.open(DETAIL).load()

def main():
    output = 'BOARD = [\n'
    for preY in range(SIZEY):
        output += '\t['
        for preX in range(SIZEX):
            output += str(int(MAP[int(preX*MULT[1]),int(preY*MULT[0])][0]/16)) + ','
        output = output[:-1] + '],\n'
    print(output[:-2] + '\n]\n\n')

    output = 'DETAILS = [\n'
    for preY in range(SIZEY):
        output += '\t['
        for preX in range(SIZEX):
            #its bad, too tired and too little time to ever fix
            color = DETAILS[int(preX*MULT[1]),int(preY*MULT[0])]
            if color[0] == color[1] == color[2] == 255:
                output += '0,' #blank
            elif color[0] < 153:
                output += str(  int((1 - color[0]/256) * 2)  ) + ',' #flag
            elif color[0] <250:
                output += str(  int(color[1]/256 * 5 + 0.5) + 3  ) + ',' #resource
            else:
                output += str(  int(color[2]/256 * 10 + 0.5) + 9  ) + ',' #city

        output = output[:-1] + '],\n'
    print(output[:-2] + '\n]\n\n')

    print('WIND = [')
    for preY in range(SIZEY):
        output = '\t['
        for preX in range(SIZEX):

            if MAP[int(preX*MULT[1]),int(preY*MULT[0])][0] > 18: #if ocean
                output += '0,'

            else:
                color = WINDMAP[int(preX*MULT[1]),int(preY*MULT[0])]

                r = color[0]/255
                g = color[1]/255
                b = color[2]/255

                if r == g == b:
                    output += '[0,0],'
                else:
                    #find hue
                    if r > max(g,b):
                        hue = (g-b)/(max(r,g,b)-min(r,g,b))
                    elif g > b:
                        hue = 2 + (b-r)/(max(r,g,b)-min(r,g,b))
                    else:
                        hue = 4 + (r-g)/(max(r,g,b)-min(r,g,b))
                    
                    hue = (60 * hue) % 360

                    #use hue
                    hue -= 120 #90 (starts at green) + 30 (360/6/2) (goes to nearest instead of above)
                    hue *= -1
                    hue %= 360
                    hue /= 60 # 360/6
                    hue = int(hue)

                    #find value
                    value = max(r,g,b)

                    #use value
                    value *= 4
                    value = int(value)
                    
                    output += '[' + str(hue) + ',' + str(value) + '],'
        print(output[:-1] + '],')
        #output = output[:-1] + '],\n'
    #print(output[:-2] + '\n]')

    #MAKE SURE TO DELETE THE ',' AT THE END ARE REPLACE IT WITH A ']'

if __name__ == '__main__': 
    main()