#!/bin/bash
list1 = [1,2,3]
list2 = [2,4,5]

dummy = []
i, j = 0, 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        dummy.append(list1[i])
        i += 1
    elif list1[i] == list2[j]:
        dummy.append(list1[i])
        dummy.append(list2[j])
        i += 1
        j += 1
    else:
        dummy.append(list2[j])
        j += 1

while i < len(list1):
    dummy.append(list1[i])
    i += 1

while j < len(list2):
    dummy.append(list2[j])
    j += 1

print(dummy)
