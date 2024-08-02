import matplotlib.pyplot as plt


defaultmarkersize = plt.rcParams['lines.markersize']

params = {
    # 'xtick.labelsize': 18,'ytick.labelsize': 18,'axes.labelsize': 20, 
    # 'legend.fontsize': 16, 'text.usetex': False,
    # 'legend.fontsize': 16, 
    # 'text.size': 'x-large', 
    'axes.labelsize': 'x-large',
    'xtick.labelsize': 'x-large', 'ytick.labelsize': 'x-large',
    'xtick.direction': 'in', 'ytick.direction': 'in',
    'xtick.minor.visible': True, 'ytick.minor.visible': True,
    'xtick.bottom': True, 'xtick.top': True,
    'ytick.left': True, 'ytick.right': True,
    'xtick.minor.size': 5, 'xtick.major.size': 10,
    'ytick.minor.size': 5, 'ytick.major.size': 10,
    'figure.figsize' : (6, 6),
    'lines.markersize': defaultmarkersize*1.25,

    # 'xtick.minor.bottom': True, 'xtick.minor.top': True,
    # 'xtick.bottom': True, 'xtick.top': True,
    # 'xtick.major.top': True, 'xtick.major.bottom': True,
    # 'xtick.minor.top': True, 
    # 'xtick.minor.size': 5,     'xtick.major.size': 10,
    # 'ytick.direction': 'in', 'ytick.left': True, 'ytick.right': True,
    # 'ytick.minor.size': 5,     'ytick.major.size': 10,
}
    # 'figure.figsize' : (10, 10)}

# plt.rcParams['axes.spines.top'] = False
# plt.rcParams['axes.spines.bottom'] = False
# plt.rcParams['axes.spines.left'] = False
# plt.rcParams['axes.spines.right'] = False

# plt.tick_params(which='minor',direction='in',axis='both',
#                 bottom='on', top='on', left='on', right='on', length=5)
# plt.tick_params(which='major',direction='in',axis='both',
#                 bottom='on', top='on', left='on', right='on', length=10)

# plt.clf()
plt.rcParams.update(params)


def bigger_size():
    params = {
        'xtick.labelsize': 40,'ytick.labelsize': 40,'axes.labelsize': 40, 
        'legend.fontsize': 16, 'text.usetex': False,
        'legend.fontsize': 16, 
        # 'text.size': 'x-large', 
        'axes.labelsize': 20,
        'xtick.labelsize': 18, 'ytick.labelsize': 18,
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.bottom': True, 'xtick.top': True,
        'ytick.left': True, 'ytick.right': True,
        'xtick.minor.size': 5, 'xtick.major.size': 10,
        'ytick.minor.size': 5, 'ytick.major.size': 10,
        'figure.figsize' : (6, 6),
        'lines.markersize': defaultmarkersize*1.5,

        # 'xtick.minor.bottom': True, 'xtick.minor.top': True,
        # 'xtick.bottom': True, 'xtick.top': True,
        # 'xtick.major.top': True, 'xtick.major.bottom': True,
        # 'xtick.minor.top': True, 
        # 'xtick.minor.size': 5,     'xtick.major.size': 10,
        # 'ytick.direction': 'in', 'ytick.left': True, 'ytick.right': True,
        # 'ytick.minor.size': 5,     'ytick.major.size': 10,
    }
        # 'figure.figsize' : (10, 10)}

    # plt.rcParams['axes.spines.top'] = False
    # plt.rcParams['axes.spines.bottom'] = False
    # plt.rcParams['axes.spines.left'] = False
    # plt.rcParams['axes.spines.right'] = False

    # plt.tick_params(which='minor',direction='in',axis='both',
    #                 bottom='on', top='on', left='on', right='on', length=5)
    # plt.tick_params(which='major',direction='in',axis='both',
    #                 bottom='on', top='on', left='on', right='on', length=10)

    # plt.clf()
    plt.rcParams.update(params)

def reset():
    params = {
        # 'xtick.labelsize': 18,'ytick.labelsize': 18,'axes.labelsize': 20, 
        # 'legend.fontsize': 16, 'text.usetex': False,
        # 'legend.fontsize': 16, 
        # 'text.size': 'x-large', 
        'axes.labelsize': 'x-large',
        'xtick.labelsize': 'x-large', 'ytick.labelsize': 'x-large',
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.bottom': True, 'xtick.top': True,
        'ytick.left': True, 'ytick.right': True,
        'xtick.minor.size': 5, 'xtick.major.size': 10,
        'ytick.minor.size': 5, 'ytick.major.size': 10,
        'figure.figsize' : (6, 6),
        'lines.markersize': defaultmarkersize*1.25,

        # 'xtick.minor.bottom': True, 'xtick.minor.top': True,
        # 'xtick.bottom': True, 'xtick.top': True,
        # 'xtick.major.top': True, 'xtick.major.bottom': True,
        # 'xtick.minor.top': True, 
        # 'xtick.minor.size': 5,     'xtick.major.size': 10,
        # 'ytick.direction': 'in', 'ytick.left': True, 'ytick.right': True,
        # 'ytick.minor.size': 5,     'ytick.major.size': 10,
    }
        # 'figure.figsize' : (10, 10)}

    # plt.rcParams['axes.spines.top'] = False
    # plt.rcParams['axes.spines.bottom'] = False
    # plt.rcParams['axes.spines.left'] = False
    # plt.rcParams['axes.spines.right'] = False

    # plt.tick_params(which='minor',direction='in',axis='both',
    #                 bottom='on', top='on', left='on', right='on', length=5)
    # plt.tick_params(which='major',direction='in',axis='both',
    #                 bottom='on', top='on', left='on', right='on', length=10)

    # plt.clf()
    plt.rcParams.update(params)



def pan_nav(event):
    ax_tmp = plt.gca()
    if event.key == ',':
        lims = ax_tmp.get_xlim()
        adjust = (lims[1] - lims[0]) * 0.2
        ax_tmp.set_xlim((lims[0] - adjust, lims[1] - adjust))
        plt.draw()
    elif event.key == '.':
        lims = ax_tmp.get_xlim()
        adjust = (lims[1] - lims[0]) * 0.2
        ax_tmp.set_xlim((lims[0] + adjust, lims[1] + adjust))
        plt.draw()
    elif (event.key == 'down') | (event.key == '<'):
        lims = ax_tmp.get_ylim()
        adjust = (lims[1] - lims[0]) * 0.1
        ax_tmp.set_ylim((lims[0] - adjust, lims[1] - adjust))
        plt.draw()
    elif (event.key == 'up') | (event.key == '>'):
        lims = ax_tmp.get_ylim()
        adjust = (lims[1] - lims[0]) * 0.1
        ax_tmp.set_ylim((lims[0] + adjust, lims[1] + adjust))
        plt.draw()
    elif event.key == 'Z':
        lims = ax_tmp.get_ylim()
        adjust = (lims[1] - lims[0]) * 0.1
        ax_tmp.set_ylim((lims[0] + adjust, lims[1] - adjust))
        plt.draw()
    elif event.key == 'z':
        lims = ax_tmp.get_ylim()
        adjust = (lims[1] - lims[0]) * 0.1
        ax_tmp.set_ylim((lims[0] - adjust, lims[1] + adjust))
        plt.draw()
    elif event.key == 'X':
        lims = ax_tmp.get_xlim()
        adjust = (lims[1] - lims[0]) * 0.1
        ax_tmp.set_xlim((lims[0] + adjust, lims[1] - adjust))
        plt.draw()
    elif event.key == 'x':
        lims = ax_tmp.get_xlim()
        adjust = (lims[1] - lims[0]) * 0.1
        ax_tmp.set_xlim((lims[0] - adjust, lims[1] + adjust))
        plt.draw()

def connect_pannav(fig):
    fig.canvas.mpl_connect('key_press_event', pan_nav)

def dark():
    plt.style.use('dark_background')

def light():
    plt.style.use('classic')