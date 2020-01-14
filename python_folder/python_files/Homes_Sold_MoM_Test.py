
# homes_sold_mom is the final dataset(panda.dataframe) with only homes sold MoM for each region. Say n regions
# Create a list combine_list containing any two regions out of n region: list(itertools.combinations(range(A.shape[1]), 2))
# Run a loop to perform hypothesis testings: T test, Wilcoxon test, KS test, Mann-Whitney rank test, KS test 

import itertools
from statsmodels.stats.weightstats import ttest_ind as t_test
from scipy.stats import wilcoxon
from scipy.stats import ks_2samp 
from scipy.stats import mannwhitneyu

combine_list = list(itertools.combinations(range(homes_sold_mom.shape[1]), 2))

#statistic, p-value, degree of freedom for two-sample t test
t_stat = []
p_val_t = []
df = []

# statistic and p-value for Wilcoxon test 
non_stat = []
p_val_wc = []

# statistic and p-value for KS test 
ks_stat = []
p_val_ks = []

# statistic and p-value for Mann-Whitney rank test  test 
mu_stat = []
p_val_mu = []

for i in range(len(combine_list)):
    temp1, temp2, temp3 = t_test(homes_sold_mom.iloc[:,combine_list[i][0]], homes_sold_mom.iloc[:,combine_list[i][1]], alternative = "two-sided", usevar = "unequal")
    t_stat.append(float(temp1)) 
    p_val_t.append(float(temp2))
    df.append(float(temp3))
    temp4, temp5 = wilcoxon(homes_sold_mom.iloc[:,combine_list[i][0]], homes_sold_mom.iloc[:,combine_list[i][1]], alternative = "two-sided", zero_method = "zsplit")
    non_stat.append(float(temp4))
    p_val_wc.append(float(temp5)) 
    temp6, temp7 = ks_2samp(homes_sold_mom.iloc[:,combine_list[i][0]], homes_sold_mom.iloc[:,combine_list[i][1]], alternative = "two-sided", mode = 'asymp')
    ks_stat.append(float(temp6))
    p_val_ks.append(float(temp7))
    temp8, temp9 = mannwhitneyu(homes_sold_mom.iloc[:,combine_list[i][0]], homes_sold_mom.iloc[:,combine_list[i][1]], alternative = "two-sided")
    mu_stat.append(float(temp8))
    p_val_mu.append(float(temp9))

test_matrix_2 = pd.DataFrame(list(zip(combine_list, t_stat, p_val_t, df, non_stat, p_val_wc, ks_stat, p_val_ks, mu_stat, p_val_mu)), 
               columns =['combinatory', 'Stat_ttest', 'p_ttest', 'df_ttest', 'Stat_wctest', 'p_wctest', 'Stat_kstest', 'p_kstest', 'Stat_mutest', 'p_mutest'])
#test_matrix_2 contains the test results for our homes_sold_mom hypothesis tests

