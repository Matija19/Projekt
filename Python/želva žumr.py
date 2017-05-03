import turtle
turtle.speed(0)
def zelva_se_sprehaja(sprehod, d):
# na koncu vsakega koraka želvo obrnemo na sever
  for korak in sprehod:
    if korak == 'S':
        turtle.forward(d)
    elif korak == 'J':
        turtle.left(180)
        turtle.forward(d)
        turtle.left(180)
    elif korak == 'V':
        turtle.left(90)
        turtle.forward(d)
        turtle.right(90)
    elif korak == 'Z':
        turtle.right(90)
        turtle.forward(d)
        turtle.left(90)
