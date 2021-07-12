from django.db.models import Count, Q
from plots.network_graph import get_variable_graph
import networkx as nx


def makeAlias(entry):
    """
    This function improves the readability of the variable names by removing the 
    underscores for easy display.
    """
    if entry.metadata.get('alias') is None:    
        name0 = entry.name
        aliasList = []
        for word in name0.split("_"):
  
            if word.isupper():
                aliasList.append(word)
            else:
                aliasList.append(word.title())

        alias = " ".join(aliasList)
        entry.metadata['alias'] = alias.replace("  "," ")
        entry.save()


def variableType(entry):
    """
    This singles out the output variables (often the variables of interest), 
    input variables (often the variables requiring user input) as well as 
    intermediate variables. 
    This is used further as an option for display of the graph structure of the 
    variables interdependencies. 
    """
    if entry.parents.count() == 0 and entry.children.count() > 0:
        if entry.metadata is None:
            entry.metadata = {"variable-type": "output"}
        else:
            entry.metadata["variable-type"] = "output"
    elif entry.children.count() == 0 and entry.parents.count() > 0:
        if entry.metadata is None:
            entry.metadata = {"variable-type": "input"}
        else:
            entry.metadata["variable-type"] = "input"
    elif entry.children.count() == 0 and entry.parents.count() == 0:
        if entry.metadata is None:
            entry.metadata = {"variable-type": "orphan"}
        else:
            entry.metadata["variable-type"] = "orphan"
    else:
        if entry.metadata is None:
            entry.metadata = {"variable-type": "intermediary"}
        else:
            entry.metadata["variable-type"] = "intermediary"
    entry.save()


def get_input_offsprings(entry):
    """
    This gives a list of all the input variables (bottom layer) needed for user input to 
    compute each variable. 
    One can write UI for this list only for each variable to be computed.
    """
    input_offsprings = []
    G = nx.DiGraph()
    H = get_variable_graph(entry.name, G)
    for node, nodeAttr in H.nodes(data=True):
        if nodeAttr["type"] == "input":
            input_offsprings.append(node)

    entry.metadata["input_offspring"] = input_offsprings
    entry.save()


