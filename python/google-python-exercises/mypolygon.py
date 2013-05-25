from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

"""fd(bob, 100)
lt(bob)
fd(bob, 100)
"""

def square(t,l):
  for i in range(4):
    fd(t,l)
    lt(t)

def rectangle(t,l,n):
  i=0
  sides=360/n
  while i < sides:
    fd(t,l)
    lt(t,n)
    i+=1

#square(bob,200)
rectangle(bob,50,60)
wait_for_user()
