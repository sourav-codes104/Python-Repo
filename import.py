#module = a file containing code you want to include in your program
#         use 'import' to include a module (built-in or your own)
#         useful to break up a large program reusable seperate files.

import geometry as g

result = g.perimeter_square(7,4)
result = g.circum_circle(34)
result = g.area_square(45)
result = g.area_circle(34)
print(result)
