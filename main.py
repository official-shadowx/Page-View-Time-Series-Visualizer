import pandas as pd
import matplotlib.pyplot as plt

def draw_line_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

    plt.plot(df.index, df['value'])
    plt.title("Page Views Over Time")
    plt.savefig("line_plot.png")