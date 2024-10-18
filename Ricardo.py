from PIL import Image, ImageDraw,ImageSequence
from colorsys import hsv_to_rgb as htr
from math import pi, sin, tan, cos
import numpy as np

def color(rgb,tx,ty):
	global pix
	r,g,b=rgb
	f=lambda arg: sin(arg)*sin(((tx+ty)/2)+((an+pix)/2))*256
	r=f(r*an/(tx+1))
	g=f(g*an/(ty+1))
	b=f(b*(an**2))
	r,g,b=map(lambda x: int(round(x)),(r,g,b))
	return (r,g,b)

def processing(gif):
	global an,que,pix,size
	tx=ty=0
	
	for frame in ImageSequence.Iterator(gif):
		que+=1
		if que%2==0 or que%7==0:
			continue
		an+=5.6
		
		frame=frame.resize((size,size),resample=Image.NEAREST)
		frame=np.array(frame.convert('RGB'))
		frame=frame.tolist()
		
		yPix=len(frame)
		xPix=len(frame[0])
		#print(xPix,yPix)
		anim=Image.new('RGB', (xPix, yPix), (0,0,0))
		draw = ImageDraw.Draw(anim)
		point=draw.point
		for y in range(yPix):
			for x in range(xPix):
				point((x,y),color(frame[y][x],tx,ty))
				pix+=1
				tx+=1/4
			ty+=1/4
		frames.append(anim)

def main():
	gif=Image.open(inPath)
	gif=processing(gif)
	frames[0].save(outPath,save_all=True,append_images=frames[1:],optimaze=False,duration=4,loop=0)

pix=an=1
size=256
inPath='Input/Ricardo.gif'
outPath='Output/Ricardo.gif'

frames=[]
que=1

main()