import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.io import to_html
import networkx as nx
import plotly.express as px


from variables.models import Variable
from django.db.models import Count

colorScheme = {
    "background_color": 'rgba(0, 0, 0, 0)',
    "trace1_color": "#913535",
    "trace2_color": "#283148",
    "text_color": "#283148",
    "highlight_color": "#8ea6b4",
}


def varIDBarChart(name='id'):
    """
    This function displays all variables in a sorted order with the combined number of direct children 
    and parents for each. 
    """
    var_names = []
    var_alias = []
    parents_number = []
    children_number = []


    for entry in Variable.objects.all():
        var_names.append(entry.name)
        var_alias.append(entry.metadata['alias'])
        parents_number.append(entry.parents.count())
        children_number.append(entry.children.count())

    if (name == 'id'):
        display_name = var_names
        display_height = len(var_names) * 20
    elif(name == 'alias'):
        display_name = var_alias
        display_height = len(var_alias) * 20

    trace1 = go.Bar(y=display_name,
                    x=children_number,
                    orientation='h',
                    name="children",
                    text=children_number,
                    textposition="auto",
                    marker=dict(
                        color=colorScheme['trace1_color']
                    ),
                    )
    trace2 = go.Bar(y=display_name,
                    x=parents_number,
                    text=parents_number,
                    textposition="inside",
                    orientation='h',
                    name="parents",
                    marker=dict(
                        color=colorScheme['trace2_color']),

                    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='stack',
        width=1200,
        height=display_height,
        yaxis=dict(
            showticklabels=True,
            dtick=1,
            tickangle=0,
            tickfont=dict(family='serif',
                          size=10,
                          color=colorScheme['text_color'],
                          ),
            categoryorder='total ascending',
        ),
        xaxis=dict(
            mirror=True,  # TODO: try with bigger top margin
            showticklabels=True,
            dtick=1,
            tick0=0,
        ),
        paper_bgcolor=colorScheme['background_color'],
        plot_bgcolor=colorScheme['background_color'],
        title=f"There are {len(var_names)} variables in the database."
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = fig.to_html(full_html=False)
    return plot_div


