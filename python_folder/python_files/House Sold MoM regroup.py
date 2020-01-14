#Create dataset of 4 matched regions, based on homes_sold_mom
df_temp_2 = pd.DataFrame(list(zip(time_frame, homes_sold_mom['Homes Sold MoM _1'], homes_sold_mom['Homes Sold MoM _18'], homes_sold_mom['Homes Sold MoM _35'], homes_sold_mom['Homes Sold MoM _65'])), 
               columns =['Time', df_list[1]['Region_1'][0], df_list[18]['Region_18'][0], df_list[35]['Region_35'][0], df_list[65]['Region_65'][0]])

# plot of 4 matched regions, based on homes_sold_mom
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,1], label = 'American University Park / Friendship Heights / Tenleytown')
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,2], label = 'Chevy Chase-DC')
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,3], label = 'Foxhall Village')
sns_plot = sns.lineplot(df_temp_2['Time'], df_temp_2.iloc[:,4], label = 'Southeast Chevy Chase')

plt.legend()
plt.title("Time Series - Homes Sold Month-over-Month",fontsize = 15)
plt.xlabel("Time", fontsize = 15)
plt.ylabel("Homes Sold Month-over-Month", fontsize = 15)
sns.set(rc={'figure.figsize':(15,10)})
plt.xticks(range(5, 100, 12))
#plt.xlim()
plt.show()

#save image of visualization
sns_plot.figure.savefig("data_visualizations/Time Series - Homes Sold Month-over-Month_Group.png")