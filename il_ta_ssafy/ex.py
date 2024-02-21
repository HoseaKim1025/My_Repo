import math
# 당구대 넓이 : 254 * 127 cm
# 공 직경 : 5.73 cm

start = [0, 0]
end = [math.sqrt(2), math.sqrt(2)]

a = abs(end[0] - start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)
radian = math.atan(b/a)

print(r, math.degrees(radian), radian)

# math.radians()