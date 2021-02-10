#!/usr/bin/python

from neighbor import neighbor

neighbor1 = neighbor("Kelly", "Brookfield", 53045, True)
print(neighbor1.name)
print(neighbor1.street)
print(neighbor1.zip)
print(neighbor1.in_county)
