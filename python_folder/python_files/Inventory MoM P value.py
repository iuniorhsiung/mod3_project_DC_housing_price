
# Create a function to detect the hypothesis testing results. 0: reject null, 1: fail to reject null

def test_p_value_3(p = .05, name = 'ttest'):
    name_list = []
    for i in range(len(test_matrix_3)):
        if test_matrix_3["p_" + name][i] < p:
            name_list.append(0) 
        else:
            name_list.append(1)   
    test_matrix_3['index_' + name] = name_list
test_p_value_3(p = .05, name = 'ttest')
test_p_value_3(p = .05, name = 'wctest')
test_p_value_3(p = .05, name = 'kstest')
test_p_value_3(p = .05, name = 'mutest')
test_matrix_3

#save inventory_mom test matrix to data folder
test_matrix_3.to_csv('data/TM_Inventory MoM.csv')

