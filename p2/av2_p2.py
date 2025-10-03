import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Rectangle
import pandas as pd


fig, ax = plt.subplots()

def animar(i):

    df = pd.read_csv('IRIS.csv')

    ax.clear()
    ax.scatter(df['sepal_length'],df['sepal_width'])
    ax.legend(['Largura/tamanho sepal da ires da flor'])
    ax.set_xlabel("largura da sepa")
    ax.axvspan(6,8, facecolor='#B3C2E8', alpha=0.5 )
    ax.text(5.4,4, 'Antes', fontsize=16, color='black')
    ax.text(6.1,4, 'Depois', fontsize=16, color='grey')
    retangulo = Rectangle((5.4,2.4), 1.1, 0.66, fill=False, color='red', linewidth=4)
    plt.gca().add_patch(retangulo)
    ax.set_ylabel("Tamanho da sepa")
    ax.set_title("Sepas tempo real", fontweight = 'bold')

ani = animation.FuncAnimation(fig, animar, interval = 1000)
plt.show()
