import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Virat_Kohli.csv")

def show_pie_plot(df,key):
    counts=df[key].value_counts()
    count_labels=counts.index
    count_values=counts.values
    fig=plt.figure(figsize=(10,10))
    plt.pie(count_values,labels=count_labels)
    plt.show()

def show_bar_graph(counts):
    count_labels=counts.index
    count_values=counts.values
    fig=plt.figure(figsize=(20,10))
    plt.bar(count_labels,count_values,color="cyan",width=0.7)
    plt.show()

#####---------------------------------------------number of matches he has played at different positions

positions=(df["Pos"].unique())
df["Pos"]=df["Pos"].map({
    1.0 :"Batting at 1",
    2.0 :"Batting at 2",
    3.0 :"Batting at 3",
    4.0 :"Batting at 4",
    5.0 :"Batting at 5",
    6.0 :"Batting at 6",
    7.0 :"Batting at 7"
})
position_count=df["Pos"].value_counts()
# show_pie_plot(df,"Pos")

#####-------------------------------------------------number of matches vs different countries
# show_pie_plot(df,"Opposition")

#####-------------------------------------------------total run scored in different positions
run_by_pos=df.groupby("Pos")["Runs"].sum()
# show_bar_graph(run_by_pos)

#####--------------------------------------------------total sixes scored in different positions
six_by_pos=df.groupby("Pos")["6s"].sum()
# show_bar_graph(six_by_pos)

#####--------------------------------------------------number of centuries scored by him in 1st and 2nd innings
centuries=df.query("Runs >= 100")
# print(centuries)
innings=centuries.groupby("Inns")["Runs"].count()
# print(innings)
# fig=plt.figure(figsize=(10,10))
# plt.pie(innings.values,labels=innings.index)
# plt.show()


#####--------------------------------------------------calculate the dismissals of Kohli
#show_pie_plot(df,"Dismissal")

#####--------------------------------------------------max runs against every countries
max_runs=df.groupby("Opposition")["Runs"].max()
show_bar_graph(max_runs)

#####------------------------------------------------analyse strike rate



#####------------------------------------------------analyse 4s against all countries



####--------------------------------------------plot graph of run vs matches

# plt.xlabel("Pos")
# plt.ylabel("Runs")
# fig2=plt.figure(figsize=(20,10))
# plt.plot(np.arange(132),df["Runs"])
# plt.show()

