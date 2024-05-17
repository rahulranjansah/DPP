import time
import bisect

l1 = [1,2,4]
l2 = [1,3,1]
# new = []


# for i in l2:
#     for element in l1:
#         if i < element:

start_time = time.time()

# new = [*l1, *l2]
# new = sorted(new)

# new = []
# for i in l1:
#     for j in l2:
#         if j <= i:
#             new.append(j)
#         else:
#             new.append(i)


# merged_list = [*list1, *list2]
# for i in (range(len(merged_list)-1)):
#     for _ in merged_list:
#         if merged_list[i-1] >= merged_list[i-2]:
#             new.append(merged_list[i-1])
#             new.append(merged_list.pop())

#     # return new

# for elemnts in zip(list1, list2):
#     print(elemnts)
    # if i <= j:
    #     new.append(i)
    #     new.append(j)
    # else:
    #     new.append(j)
    #     new.append(i)

# for i in l2:
#     bisect.insort(l1,i)

spliced = [None]*(len(l1)+len(l2))
spliced[::2] = l1
spliced[1::2] = l2

end_time = time.time()

print(spliced)
print("Time taken: ", (end_time - start_time) * 1000, "ms")

