def clockangles(rotation=int(input()), longitude=float(input())):
    longitude1 =round(longitude,2)
    time = (rotation / 360) * longitude1
    ht = int(time)
    mt = int(((time - ht)*0.6)*100)
    if (ht == 12):
        ht = 0;
    if (mt == 60):
        mt = 0;
    angle = abs(int(ht * 30 + mt * 0.5) - int(mt * 6))
    return min(360 - angle, angle)


print("%.2f" % clockangles())