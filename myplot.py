def myplot():
    import numpy as np
    import pandas as pd
    import datetime
    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots(1,1, figsize=(12,8))
    ax2 = ax1.twinx()

    df = pd.read_csv("population_ratio.csv", index_col = 0)
    bottom = np.zeros(len(df.index))

    labels = ["Under 15 years old","15 to 64 years old", "65 years old and over"]
    colors = ["dodgerblue","#ff7f00","limegreen"]

    for i in range(3):
        ax1.bar(df.index, df.iloc[:,i],width=0.8,align='center', zorder=10-0.1*i, bottom=bottom, label=labels[i],
               color=colors[i])
        bottom += df.iloc[:,i]

    ax1.set_title("Transition in Japan's population by generation",fontsize=20)
    ax1.legend(fontsize=14)
    ax1.tick_params(labelsize=14)
    ax1.set_xlabel("Years", fontsize=16)
    ax1.set_ylabel("Number of people (Unit: 10 thousand)", fontsize=16)

    ax2.plot(df["15歳未満割合"],color="midnightblue", linewidth=4, label="Under 15 years old")
    ax2.plot(df["高齢者割合"],color="darkgreen", linewidth=4, label="65 years old and over")
    ax2.set_ylim(0,45)
    ax2.legend(fontsize=14)
    ax2.tick_params(labelsize=14)
    ax2.set_ylabel("Percentage of people (Unit: %)", fontsize=16)
    plt.show()
    return

myplot()