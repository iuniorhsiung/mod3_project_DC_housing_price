# Find all regions with similar characteristic based on both Wilcoxon and Mann Whitney tests
index_wc = test_matrix['index_wctest'] == 1
index_mu = test_matrix['index_mutest'] == 1
index_kt = test_matrix['index_kttest'] == 0
#test_matrix[index_wc]
#test_matrix[index_mu]
test_matrix[index_wc & index_mu & index_kt][0:40]

#Find names of matched regions from above cell
df_list[1]['Region_1'][0]
df_list[18]['Region_18'][0]
df_list[35]['Region_35'][0]
df_list[65]['Region_65'][0]

# Set up data time frame
time_frame = pd.date_range('2012-02-01','2019-10-01', 
              freq='MS').strftime("%Y-%b").tolist()
