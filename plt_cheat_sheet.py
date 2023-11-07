__version__ = '0.0.0'
__author__ = 'https://github.com/fear2225'

# External
from matplotlib import pyplot as plt

# Internal

# Consts

# ============================================================
def CollatzTeorem(n: int) -> (list, list):
    '''
    Collatz theorem
    :param n: number to prove
    :return: [steps], [step result]
    '''
    step = 1
    result = [n]
    while n != 1:       # every num return to 1
        if n % 2:       # if odd n*3 + 1
            n *= 3
            n += 1
        else:           # if even n / 2
            n /= 2

        # store steps
        result.append(n)
        step += 1

    return [*range(step)], result


def four_figures():
    '''source: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.axes.Axes.plot.html'''
    # type aliasing for better writing
    ax1: plt.Axes   # Axes object
    ax2: plt.Axes   # matplotlib object
    ax3: plt.Axes   # of rectangle shape
    ax4: plt.Axes   # figure

    fig: plt.Figure # Figure object

    # ==AXES DEFINE==
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    # define many figures
    # Axes objects unpacks like
    # ((columns), (columns))
    # outer bracket for rows

    # ==MAIN WINDOW OPTIONS==
    # prettify space between figures
    plt.subplots_adjust(
        left=0.05,
        bottom=0.05,
        right=0.98,
        top=0.95,
        wspace=0.15,
        hspace=0.15
    )

    # ==PLOT==
    ax1.plot(*CollatzTeorem(26), linestyle='--', color='m', label='26',
             marker='v', markeredgecolor='k', markersize=8)     # marker opt
    ax1.plot(*CollatzTeorem(25), marker='_', linestyle='-',  color='r', label='25')
    ax1.grid()      # add grid to plot
    ax1.legend()    # add legend

    # ==STEP==
    # where option: 'pre', 'mid', 'post'
    ax2.step(*CollatzTeorem(13), where='pre', color='#005bff')
    ax2.hlines(1, 0, 8, color='r', label='horizontal')
    ax2.vlines(5, 0, 40, color='k', label='vertical')
    ax2.grid()
    ax2.legend()
    ax2.set_title('ax2 title')

    # ==LaTeX & LOG SCALE==
    # LaTeX format
    # online converter: http://primat.org/mathred/mathred.html
    ax3.plot(*CollatzTeorem(27), color='k', label=r'$\left[\frac{m}{c^{2}}\right]$')
    ax3.legend()
    ax3.set_ylabel('value [log]')     # set y axis title
    ax3.set_xlabel('$steps$')   # $LaTeX format$
    # add text by chords
    ax3.text(77, 9232, 'x=77, y=9232', color='m')
    ax3.set_yscale('log')       # log y scale

    # ==FILL==
    x, y = CollatzTeorem(19)
    ax4.plot(x, y, color='red', linestyle=':')
    ax4.fill_between(x, y, [0 for _ in x], color='b', alpha=.6)
    x, y = CollatzTeorem(17)
    ax4.plot(x, y, color='gold', linestyle='-.')
    ax4.fill_between(x, y, [0 for _ in x], color='k', alpha=.9)
    ax4.grid()

    plt.show()


def main_test():
    four_figures()
    pass


# ============================================================
if __name__ == '__main__':
    main_test()
    pass
