def control(x,y):
    if process(x,y) > x*y:
        return process(x,y)
    else:
        return x*y