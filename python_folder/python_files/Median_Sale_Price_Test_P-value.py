Create a function to detect the hypothesis testing results. 0: reject null, 1: fail to reject null
def test_p_value(p = .05, name = 'ttest'):
    name_list = []
    for i in range(len(test_matrix)):
        if test_matrix["p_" + name][i] < p:
            name_list.append(0) 
        else:
            name_list.append(1)   
    test_matrix['index_' + name] = name_list
    
    
test_p_value(p = .000001, name = 'ttest')
test_p_value(p = .000001, name = 'wctest')
test_p_value(p = .000001, name = 'kstest')
test_p_value(p = .000001, name = 'mutest')
test_p_value(p = .000001, name = 'kttest')
#test_matrix
#test_matrix.shape

# Save the final testing results for median_sale_price in data folder
test_matrix.to_csv('../data/TM_Median Sale Price.csv')