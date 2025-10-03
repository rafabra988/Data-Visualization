import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd


fig, ax = plt.subplots()

def animar(i):

    df = pd.read_csv('tips.csv')

    ax.clear()
    ax.bar(df['total_bill'],df['tip'])
    ax.legend(['Quantidade de gorjeta em relação a conta'])
    ax.set_xlabel("Total da conta")
    ax.set_ylabel("Gorjeta")
    ax.set_title("Gorgeta tempo real", fontweight = 'bold')

ani = animation.FuncAnimation(fig, animar, interval = 1000)
plt.show()
