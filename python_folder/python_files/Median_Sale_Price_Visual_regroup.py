
#Create dataset of 4 matched regions, based on median sale price
df_temp = pd.DataFrame(list(zip(time_frame, median_sale_price['Median Sale Price_1'], median_sale_price['Median Sale Price_18'], median_sale_price['Median Sale Price_35'], median_sale_price['Median Sale Price_65'])), 
               columns =['Time', df_list[1]['Region_1'][0], df_list[18]['Region_18'][0], df_list[35]['Region_35'][0], df_list[65]['Region_65'][0]])
#df_temp1 = df_temp.set_index(df['Time'])

# plot of 4 matched regions, based on median sale price
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,1], label = 'American University Park / Friendship Heights / Tenleytown')
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,2], label = 'Chevy Chase-DC')
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,3], label = 'Foxhall Village')
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,4], label = 'Southeast Chevy Chase')

plt.legend()
plt.title("Time Series - Median House Price",fontsize = 20)
plt.xlabel("Time", fontsize = 20)
plt.ylabel("Median House Price", fontsize = 20)
sns.set(rc={'figure.figsize':(15,10)})
plt.xticks(range(5, 100, 12))
#plt.xlim()
plt.show()

#save image of visualization
sns_plot.figure.savefig("../data_visualizations/Time Series - Median House Price_Group.png")



