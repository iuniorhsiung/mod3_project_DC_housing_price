#Create dataset of first 8 regions in dataset for visualization purposes, using median_sale_price
df_temp = pd.DataFrame(list(zip(time_frame, median_sale_price['Median Sale Price_0'], median_sale_price['Median Sale Price_1'], median_sale_price['Median Sale Price_2'], median_sale_price['Median Sale Price_3'], median_sale_price['Median Sale Price_4'], median_sale_price['Median Sale Price_5'], median_sale_price['Median Sale Price_6'], median_sale_price['Median Sale Price_7'])), 
               columns =['Time', df_list[0]['Region_0'][0], df_list[1]['Region_1'][0], df_list[2]['Region_2'][0], df_list[3]['Region_3'][0], df_list[4]['Region_4'][0], df_list[5]['Region_5'][0], df_list[6]['Region_6'][0], df_list[7]['Region_7'][0]])

# plot of first 8 regions in dataset, using median_sale_price
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,1], label = df_temp.columns[1])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,2], label = df_temp.columns[2])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,3], label = df_temp.columns[3])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,4], label = df_temp.columns[4])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,5], label = df_temp.columns[5])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,6], label = df_temp.columns[6])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,7], label = df_temp.columns[7])
sns_plot = sns.lineplot(df_temp['Time'], df_temp.iloc[:,8], label = df_temp.columns[8])


plt.legend()
plt.title("Time Series - Median House Price",fontsize = 25)
plt.xlabel("Time", fontsize = 15)
plt.ylabel("Median House Price", fontsize = 25)
sns.set(rc={'figure.figsize':(15,10)})
plt.xticks(range(5, 100, 12))
#plt.xlim()
plt.show()

#save image of visualization
sns_plot.figure.savefig("../data_visualizations/Time Series - Median House Price.png")


