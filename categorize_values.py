"""
Securities classification
"""
# list of various types

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(myMixedTypeList)

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))