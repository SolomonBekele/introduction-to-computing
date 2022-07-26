import math

def compute_and_plot(deg):
    print "#" * int(math.sin(deg)*40 + 40)

for deg in range(0, 361, 10):
    angle = (math.pi * deg * 1.0) / 180
    compute_and_plot(angle)
