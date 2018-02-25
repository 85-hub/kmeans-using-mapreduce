import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load( open("final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)



feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

text_file = open("dataset.txt", "r+")
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
    text_file.write(str(f1))
    text_file.write("\t")
    text_file.write(str(f2))
    text_file.write("\n")
plt.show()
text_file.close()

