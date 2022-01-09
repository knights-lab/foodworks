import math
import matplotlib.pyplot as plt
import os
import subprocess
import tempfile
import seaborn as sns


def get_fig_size(fig_width, fig_height=None):
    """Convert dimensions in centimeters to inches.
    If no height is given, it is computed using the golden ratio.
    """
    if not fig_height:
#         golden_ratio = (1 + math.sqrt(5))/2
        golden_ratio = 11 / 8.5
        fig_height = fig_width / golden_ratio

    size = (fig_width, fig_height)
    return size


"""
The following functions can be used by scripts to get the sizes of
the various elements of the figures.
"""


def label_size():
    """Size of axis labels
    """
    return 12


def font_size():
    """Size of all texts shown in plots
    """
    return 12


def ticks_size():
    """Size of axes' ticks
    """
    return 8


def axis_lw():
    """Line width of the axes
    """
    return 0.6


def plot_lw():
    """Line width of the plotted curves
    """
    return 1.5


def figure_setup():
    """Set all the sizes to the correct values and use
    tex fonts for all texts.
    """
    params = {'text.usetex': False,
              'figure.dpi': 350,
              'font.size': font_size(),
              'font.serif': [],
              'font.sans-serif': [],
              'font.monospace': [],
              'axes.labelsize': label_size(),
              'axes.titlesize': font_size(),
              'axes.linewidth': axis_lw(),
              'legend.fontsize': font_size(),
              'xtick.labelsize': ticks_size(),
              'ytick.labelsize': ticks_size(),
              'font.family': 'DejaVu Sans'}
    sns.set(context="paper", style="ticks", palette="colorblind", rc=params)

    
def stylize_axes(ax):
    """Customize axes spines, title, labels, ticks, and ticklabels."""
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
    ax.yaxis.grid(True, linestyle="dotted")
    ax.xaxis.grid(True, linestyle="dotted")

    ax.xaxis.set_tick_params(bottom='on', direction='out', width=axis_lw())
    ax.yaxis.set_tick_params(left='on', direction='out', width=axis_lw())

    
def stylize_fig(fig):
#     sns.despine(fig, offset=10, trim=True)
    pass

    
def save_plot(fig, pltname, artists=()):
    fig.savefig(os.path.join("plots", pltname + ".svg"), dpi=350, bbox_extra_artists=artists, bbox_inches='tight', transparent=False)
    fig.savefig(os.path.join("plots", pltname + ".png"), dpi=350, bbox_extra_artists=artists, bbox_inches='tight', transparent=False)
    fig.savefig(os.path.join("plots", pltname + ".pdf"), dpi=350, bbox_extra_artists=artists, bbox_inches='tight', transparent=False)

    
def custom_legend(fig, colors, labels, markers, legend_location="center left", legend_boundary = (1,.5)):
    # Create custom legend for colors"
    patches = [ plt.plot([],[], marker=markers[i], ms=12, ls="", mec=None, color=colors[i], label="{:s}".format(labels[i]) )[0]  for i in range(len(labels)) ]
    artist = fig.legend(patches, labels, loc=legend_location, bbox_to_anchor=legend_boundary, fontsize=12)
    return artist

