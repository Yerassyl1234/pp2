from cmath import pi, tan


def areaPolygon(numsides,lengthsides):
    area = (pow(lengthsides,2)*numsides)/(4*tan(pi/numsides))
    return area
a = int(input())
b = int(input())
print(areaPolygon(a,b))