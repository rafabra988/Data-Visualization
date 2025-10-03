import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd


fig, ax = plt.subplots()

def animar(i):

    df = pd.read_csv('tips.csv')

    x = df['total_bill']
    y = df['tip']

    ax.clear()
    ax.scatter(x,y)
    ax.legend()
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_title("Gorgeta rempo real", fontweight = 'bold')

ani = animation.FuncAnimation(fig, animar, interval = 1000)
plt.show()
