
import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys, re, math

CLUSTERS_FILENAME = 'clusters.txt'

clusters = []
delta_clusters = dict()

def read_from_clusters_cache_file(clusters_file):
    f = open(clusters_file, 'r')
    data = f.read()
    f.close()
    del f
    return data

def read_clusters():
    cluster_data = read_from_clusters_cache_file(CLUSTERS_FILENAME)
    for line in cluster_data.strip().split("\n"):
        data = line.strip().split("\t")
        centroid_id, coords = data
        salary, stock = coords.strip().split(";")
        clusters.append((centroid_id, float(salary), float(stock)))
        delta_clusters[centroid_id] = (0, 0, 0)

def get_distance_coords(lat1, long1, lat2, long2):
	#Calculate euclidian distance between two coordinates
    dist = math.sqrt(math.pow(lat1 - lat2,2) + math.pow(long1 - long2,2))
    return dist

def get_nearest_cluster(latitude, longitude):
    nearest_cluster_id = None
    nearest_distance = 10000000000
    for cluster in clusters:
        dist = get_distance_coords(latitude, longitude, cluster[1], cluster[2])
        if dist < nearest_distance:
            nearest_cluster_id = cluster[0]
            nearest_distance = dist
    return nearest_cluster_id


read_clusters()
#print clusters
regexWords = re.compile("\s+")
for line in sys.stdin:
    line = line.strip()
    data = line.strip().split("\t")
    salary, stock=data
    slry = float(salary)
    #print slry
    stck= float(stock)
    #print stck
    nearest_cluster_id = get_nearest_cluster(slry, stck)
    #print nearest_cluster_id
    print nearest_cluster_id + "\t" + str(slry) + "\t" + str(stck) 
    #sumy, sumx, cont = delta_clusters[nearest_cluster_id]
    #delta_clusters[nearest_cluster_id] = (sumy + slry, sumx + stck, cont+1)
    #print "cont " + str(cont)

#print delta_clusters
        
#for key in delta_clusters:
 #   sumy, sumx, cont = delta_clusters[key]
  #  print key + "\t" + str(sumy)+";"+str(sumx)+";"+str(cont)