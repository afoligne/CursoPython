'''from matplotlib import pyplot


def faz_grafico(lista_numeros):
    fig1, ax1 = pyplot.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(lista_numeros)
    pyplot.show()'''


import matplotlib.pyplot as plt

# Create some mock data


def faz_grafico(lista_numeros):
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(lista_numeros, lista_numeros, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(lista_numeros, lista_numeros, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()