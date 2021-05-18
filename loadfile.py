


def load_file(path: str):
    """Loads a text file containing the data to create a directed graph. It 
       excepts a specific format. Returns a dictionary with the graph.
    """
    graph = {}
    f = open(path, "r")
    lines = f.readlines()

    decomented_lines = []

    # discard comments and creates a new list
    for line in lines:
        if not line.startswith('#'):
            decomented_lines.append(line)

    try:
        # a little hack, below code requires last line to have a newline character.
        if not '\n' in decomented_lines[-1]:
            decomented_lines[-1] += '\n'

        # remove blank lines
        while '\n' in decomented_lines:
            decomented_lines.remove('\n')

        item_list = []

        # creates a new list with the components of the graph
        for line in decomented_lines:
            items = line.split(";")
            item_list.append(items)

        # final loop convers the strings in the graph
        for item in item_list:
            has_color = True
            node_name = item[0].split('"')[1]
            graph[node_name] = {"connects_to": [], "color": "white"}

            connect_to = item[1]

            if '\n' in connect_to:
                has_color = False
                connect_to = connect_to.replace("\n", "")

            connect_to = connect_to.replace('[', '')
            connect_to = connect_to.replace(']', '')
            connect_to = connect_to.replace('"', '')
            connect_to = connect_to.split(',')
            graph[node_name]["connects_to"] = connect_to

            # because stating a color for a node is optional whe have to
            # check every time if the line actually haves color data, else
            # it defauls to "white"
            
            if has_color:
                color = item[2]
                if color =='\n':
                    graph[node_name]["color"] = "white" 
                else:       
                    color = color.replace('\n', '')
                    color = color.replace('"', '')
                    graph[node_name]["color"] = color

        return graph
    except Exception:
        print("\nError reading input file, check for formatting errors...\n")
        raise