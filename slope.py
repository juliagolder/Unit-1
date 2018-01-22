#Julia Golder
#1/22/18
#slope.py - how to calculate the slope of a line with two points


x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

slope = (y2-y1)/(x2-x1)
print('The slope is', (y2-y1)/(x2-x1))
b = y1 - slope*x1
m = slope

print('The equation of the line is', 'Y=', m, '*x +', b )