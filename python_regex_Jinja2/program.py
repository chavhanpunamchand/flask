
orgindict = {"C":100,"Abc":233,"VSD":34,"VVVV" : "VV","484": "axx"}
#orgindict.C     ---> attr(orgindict,"C")    --> True
from collections import OrderedDict

print(OrderedDict(sorted(orgindict.items())))

import sys
sys.exit(0)

#https://www.webforefront.com/django/usebuiltinjinjafilters.html

# regex patterns for -->
# list --. from jinja templates--> not able to understand...


values = list(orgindict.keys())
values.sort()

newdict = {}
for key in values:
    newdict[key] = orgindict.get(key)

print(newdict)



