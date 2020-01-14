#Create dataset of first 8 regions in dataset for visualization purposes, using homes_sold_mom
df_temp_2 = pd.DataFrame(list(zip(time_frame, homes_sold_mom['Homes Sold MoM _0'], homes_sold_mom['Homes Sold MoM _1'], homes_sold_mom['Homes Sold MoM _2'], homes_sold_mom['Homes Sold MoM _3'], homes_sold_mom['Homes Sold MoM _4'], homes_sold_mom['Homes Sold MoM _5'], homes_sold_mom['Homes Sold MoM _6'], homes_sold_mom['Homes Sold MoM _7'])), 
               columns =['Time', df_list[0]['Region_0'][0], df_list[1]['Region_1'][0], df_list[2]['Region_2'][0], df_list[3]['Region_3'][0], df_list[4]['Region_4'][0], df_list[5]['Region_5'][0], df_list[6]['Region_6'][0], df_list[7]['Region_7'][0]])

# plot of first 8 regions in dataset, using homes_sold_mom
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,1], label = df_temp_2.columns[1])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,2], label = df_temp_2.columns[2])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,3], label = df_temp_2.columns[3])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,4], label = df_temp_2.columns[4])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,5], label = df_temp_2.columns[5])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,6], label = df_temp_2.columns[6])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,7], label = df_temp_2.columns[7])
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,8], label = df_temp_2.columns[8])


plt.legend()
plt.title("Time Series - Homes Sold Month-over-Month",fontsize = 15)
plt.xlabel("Time", fontsize = 15)
plt.ylabel("Homes Sold Month-over-Month", fontsize = 15)
sns.set(rc={'figure.figsize':(15,10)})
plt.xticks(range(5, 100, 12))
#plt.xlim()
plt.show()

#save image of visualization
sns_plot.figure.savefig("data_visualizations/Time Series - Homes Sold Month-over-Month.png")

