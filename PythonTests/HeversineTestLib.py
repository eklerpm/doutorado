from haversine import haversine

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

km = haversine(lyon, paris)
# 392.21671780659625  # in kilometers
meter = km * 1000
print("meters: ",meter)


print("kilometers: ",km)

s = haversine(lyon, paris, miles=True)
# 243.71209416020253  # in miles
print("miles: ",s)


haversine(lyon, paris, nautical_miles=True)
# 211.7801622966963  # in nautical miles
print("nautical_miles: ",s)
