from turtle import *

def interpolate_linear(p1, p2, t):
    poutx = p1[0] + t * (p2[0] - p1[0])
    pouty = p1[1] + t * (p2[1] - p1[1])
    return (poutx, pouty)

def bezier_point(points, t):
    if len(points) == 2:
        return interpolate_linear(points[0], points[1], t);
    else:
        newpoints = []
        for i in range(len(points) - 1):
            newpoints.append(interpolate_linear(points[i], points[i + 1], t))
        
        return bezier_point(newpoints, t)

def bezier_cruve(points, detail):
    curve = []
    step = 1.0 / detail
    for i in range(detail + 1):
        x = bezier_point(points, step * i)
        curve.append(x)
    
    return curve

def turtle_points(points):
    setpos(points[0][0], points[0][1])
    for i in range(1, len(points)):
        goto(points[i][0], points[i][1])

points = [(0.0, 0.0), (100.0, 0.0), (100.0, 100.0)]

color('black')
turtle_points(bezier_cruve(points, 10))
