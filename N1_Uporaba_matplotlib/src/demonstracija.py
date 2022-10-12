import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plthist
from matplotlib.gridspec import GridSpec

def izris(slika, crta, tocke, podatki):
    #gs1 = GridSpec(2, 1)
    #plt.plot(crta, 'g--', label='crta')
    #plt.plot(tocke, 'c+', label='tocke')
    #plt.axis([0, 10, -10, 10])
    #plt.xlabel('X')
    #plt.ylabel('Y')
    #plt.legend()
    #plt.title('crta in tocke')
    #plt.show()
    #plthist.hist(podatki)
    #plthist.show()


    fig = plt.figure(tight_layout=True)
    gs = GridSpec(2, 2)

    ax = fig.add_subplot(gs[0, 0])

    ax.plot(crta, 'g--', label='crta')
    ax.plot(tocke, 'c+', label='tocke')
    ax.axis([0, 10, -10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.set_title('crta in tocke')

    ax = fig.add_subplot(gs[1, 0])
    ax.hist(podatki, label="podatki")
    ax.axis([0, 10, -10, 10])
    ax.set_xlabel('index')
    ax.set_ylabel('stevilo')
    ax.legend(alignment='left')
    ax.set_title('podatki')

    return 0

