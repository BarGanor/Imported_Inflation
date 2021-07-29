from largest_partners import *
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib as plt




def get_matching_index(df1, df2):
    matching_index_lst = []

    for index in df1.index:
        if index in df2.index:
            matching_index_lst.append(index)
    return matching_index_lst




# pca_cpi = PCA()
# principalComponents_cpi = pca_cpi.fit_transform(x)
# principal_cpi_Df = pd.DataFrame(data=principalComponents_cpi)
