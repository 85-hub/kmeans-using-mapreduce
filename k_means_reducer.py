import sys, random
import numpy as np

clusters = []
slry=np.zeros((5,), dtype=np.float)
stck=np.zeros((5,), dtype=np.float)
count=np.zeros((5,), dtype=np.int)
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #print data_mapped
    centroid_id, salary , stock = data_mapped
    #print centroid_id + "\t" + salary + "\t" + stock
    slry[int(centroid_id)]+= float(salary)
    stck[int(centroid_id)]+=float(stock)
    count[int(centroid_id)]+=1

print slry
print "\n"
print stck
print "\n"
print count
i=0
centroid_id=0
for i in range(len(count)):
    if (count[i]!=0) :
        clusters.append((centroid_id, float(slry[i]/count[i]), float(stck[i]/count[i])))
    centroid_id+=1

print clusters

file1 = open("clusters.txt","w+")
i=0
for i in range(len(clusters)):
    cen_id, sly, stk=str(clusters[i]).split(",")
    print cen_id
    print sly
    print stk
    cen_id=cen_id[:0] + cen_id[1:]
    print cen_id
    print sly
    stk=stk[:-1]
    print stk

    file1.write(cen_id)
    file1.write("\t")
    file1.write(sly)
    file1.write(";")
    file1.write(stk)
    file1.write("\n")
file1.close()


