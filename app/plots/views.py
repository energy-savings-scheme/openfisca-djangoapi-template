from plots.plots import varIDBarChart
from plots.network_graph import network_graph
from django.shortcuts import render


def BarChart_id(request):
    """
    # GET a bar chart of all variables in the database

    # Returns
    - html bar chart of all variables sorted by variable ids.

    # NO URL parameter 
    - "/plots/id"

    """
    context = {'plot': varIDBarChart('id')}
    response = render(request, 'plots/plot_template.html', context)
    return response


def BarChart_alias(request):
    """
    # GET a bar chart of all variables in the database

    # Returns
    - html bar chart of all variables sorted by variable alias for more readability.

    # NO URL parameter 
    - "/plots/alias"

    """
    context = {'plot': varIDBarChart('alias')}
    response = render(request, 'plots/plot_template.html', context)
    return response




def NetworkGraph_shortest(request, var_id):
    """
    # GET dependency network graph of a single Variable

    # Returns
    - html directed graph for all children of a variable
        with the shortest path length as layout algorithm

    # URL parameter (required)
    The following url parameter must be specified
    - variable_name [str]: e.g. "/graph/<variable_name>

    """
    context = {'plot': network_graph(var_id, layout='shortest')}
    response = render(request, 'plots/plot_template.html', context)
    return response
