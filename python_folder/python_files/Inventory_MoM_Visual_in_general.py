#Create dataset of first 8 regions in dataset for visualization purposes, using inventory_mom
df_temp_3 = pd.DataFrame(list(zip(time_frame, inventory_mom['Inventory MoM _0'], inventory_mom['Inventory MoM _1'], inventory_mom['Inventory MoM _2'], inventory_mom['Inventory MoM _3'], inventory_mom['Inventory MoM _4'], inventory_mom['Inventory MoM _5'], inventory_mom['Inventory MoM _6'], inventory_mom['Inventory MoM _7'])), 
               columns =['Time', df_list[0]['Region_0'][0], df_list[1]['Region_1'][0], df_list[2]['Region_2'][0], df_list[3]['Region_3'][0], df_list[4]['Region_4'][0], df_list[5]['Region_5'][0], df_list[6]['Region_6'][0], df_list[7]['Region_7'][0]])


 #plot of first 8 regions in dataset, using inventory_mom
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,1], label = df_temp_3.columns[1])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,2], label = df_temp_3.columns[2])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,3], label = df_temp_3.columns[3])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,4], label = df_temp_3.columns[4])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,5], label = df_temp_3.columns[5])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,6], label = df_temp_3.columns[6])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,7], label = df_temp_3.columns[7])
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,8], label = df_temp_3.columns[8])


plt.legend()
plt.title("Time Series - Inventory Month-over-Month",fontsize = 15)
plt.xlabel("Time", fontsize = 15)
plt.ylabel("Inventory Month-over-Month", fontsize = 15)
sns.set(rc={'figure.figsize':(15,10)})
plt.xticks(range(5, 100, 12))
#plt.xlim()
plt.show()

#save image of visualization
sns_plot.figure.savefig("../data_visualizations/Time Series - Inventory Month-over-Month.png")

