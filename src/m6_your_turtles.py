"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Joshua Giambattista.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
import math

cynthia = rg.SimpleTurtle('turtle')
cynthia.pen=rg.Pen('purple',1)
cynthia.speed= 20
cynthia.go_to(rg.Point(0, 0))
for k in range(65):
    cynthia.forward(30)
    cynthia.left(150)
    cynthia.forward(30)
    cynthia.left(150)
    cynthia.forward(30)
    cynthia.go_to(rg.Point(math.cos(k), math.sin(k)))

robert = rg.SimpleTurtle('triangle')
robert.pen=rg.Pen('blue', 1)
robert.speed = 20
robert.pen_up()
robert.go_to(rg.Point(-100,150))
robert.pen_down()
for l in range(200):
    robert.forward(l+1)
    robert.left(l+1)



window.close_on_mouse_click()