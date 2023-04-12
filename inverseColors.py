def color_invert(rg):
  red_inverse = 255 - rg[0]
  green_inverse = 255 - rg[1]
  blue_inverse = 255 - rg[2]
  return (red_inverse,green_inverse, blue_inverse)

print(color_invert((165, 170, 221)))