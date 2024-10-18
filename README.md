🇺🇸ENG:
I wrote the code in one sitting, so towards the end I didn't care so much about beauty and practicality that I just wanted to see the result quickly, despite the crutches.

	que+=1
	if que%2==0 or que%7==0:
		continue
In this part of the code I organized the que (que) variable. Every 2nd and 7th frame is skipped to reduce the file processing time.

	f=lambda arg: sin(arg)*sin(((tx+ty)/2)+((an+pix)/2))*256
	r=f(r*an/(tx+1))
	g=f(g*an/(ty+1))
	b=f(b*(an**2)) 
The most interesting part of the code - it determines by the color of the pixel on the original gif what color it will be on the processed gif.

🇷🇺RUS:
Код я писал в один присест, поэтому под конец стало так плевать на красоту и практичность, что я просто хотел побыстрее увидеть результат, несмотря на костыли.

	que+=1
	if que%2==0 or que%7==0:
		continue
В этой части кода я организовал переменную que (очередь). Каждый 2-й и 7-й кадр пропускаются, чтобы сократить время обработки файла.

	f=lambda arg: sin(arg)*sin(((tx+ty)/2)+((an+pix)/2))*256
	r=f(r*an/(tx+1))
	g=f(g*an/(ty+1))
	b=f(b*(an**2)) 
Самая интересная часть кода - тут определяется по цвету пикселя на оригинальной гифке какого цвета он будет на обработанной гифке.
