#Create dataset of 4 matched regions, based on inventory_mom
df_temp_3 = pd.DataFrame(list(zip(time_frame, inventory_mom['Inventory MoM _1'], inventory_mom['Inventory MoM _18'], inventory_mom['Inventory MoM _35'], inventory_mom['Inventory MoM _65'])), 
               columns =['Time', df_list[1]['Region_1'][0], df_list[18]['Region_18'][0], df_list[35]['Region_35'][0], df_list[65]['Region_65'][0]])

# plot of 4 matched regions, based on inventory_mom
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,1], label = 'American University Park / Friendship Heights / Tenleytown')
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,2], label = 'Chevy Chase-DC')
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,3], label = 'Foxhall Village')
sns_plot = sns.lineplot(df_temp_3['Time'], df_temp_3.iloc[:,4], label = 'Southeast Chevy Chase')

plt.legend()
plt.title("Time Series - Inventory Month-over-Month",fontsize = 15)
plt.xlabel("Time", fontsize = 15)
plt.ylabel("Inventory Month-over-Month", fontsize = 15)
sns.set(rc={'figure.figsize':(15,10)})
plt.xticks(range(5, 100, 12))
#plt.xlim()
plt.show()

#save image of visualization
sns_plot.figure.savefig("../data_visualizations/Time Series - Inventory Month-over-Month_Group.png")


