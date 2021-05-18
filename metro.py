
#!/usr/bin/python
import sys
from drawgraph import draw_graph
from loadfile import load_file


def usage():
    print("Usage: ")
    print(
        "  <graph file> <starting estation/node> <ending station/node> [color(defauls to 'white')]")


def find_all_paths(graph, start, end, path=[]):
    """ Creates all the possible routes between 2 nodes. Returns a lists with
        the routes found.
    """
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]['connects_to']:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_stops(graph, path, color):
    """Given a graph and a known path, find the stops based on the specified
       color, returns a list with the nodes the train has to stop.
    """
    stops = []
    for node in path:
        if color == "white":
            stops.append(node)
        elif graph[node]["color"] == color or graph[node]["color"] == "white":
            stops.append(node)
    return stops


def find_best_routes(graph, paths=[], color=None):
    """ Given known paths, find the best routes based on the selected color.
        Returns a tuple of lists with best routes. first element of the tuple
        is are the original paths and the second the "optimized" routes. We
         need this info to ensure a proper graph drawing.
    """

    best_par = ([], [])
    color_paths = []
    best_score = 99999

# generates stops based on selected color
    for path in paths:
        current_path = find_stops(graph, path, color)
        score = len(current_path)
        if score <= best_score:
            color_paths.append(current_path)
            best_score = score

    # eval best color routes based on length
    i = 0
    for path in color_paths:
        if len(path) <= best_score:
            best_par[1].append(path)
            best_par[0].append(paths[i])
        i += 1
    return best_par


def paths_to_string(paths=[]):
    """Returns a nice printable string representing the input route.    
    """
    i = 0
    text = ""
    for path in paths:
        while(i < len(path)-1):
            text += "["+path[i]+"]->"
            i += 1
        text += "["+path[i]+"] "
        i = 0
    return text


def path_to_string(path):
    """ Same as path_to_string, but only for a single route 
    """
    i = 0
    text = ""
    while i < len(path)-1:
        text += "["+path[i]+"]->"
        i += 1
    text += "["+path[i]+"]"
    
    return text


def draw_results(color, graph, best_paths):
    print(paths_to_string(best_paths[1]))
    for i in range(0, len(best_paths[0])):
        draw_graph(color+"_"+str(i+1), graph,
                   best_paths[0][i], best_paths[1][i], path_to_string(best_paths[1][i]))


def main(argv):
    if len(argv) < 1:
        print("ERROR : Specify the file path with the graph data!")
    if len(argv) < 2:
        print("ERROR : Specify a starting node!")
    if len(argv) < 3:
        print("ERROR : Specify an ending node!")
        usage()
        return 0
    else:
        filepath = argv[0]
        start = argv[1]
        end = argv[2]
        if len(argv) == 4:
            color = argv[3]
        else:
            color = "white"

    graph = load_file(filepath)
    paths = find_all_paths(graph, start, end)

    if color == "red":
        best_paths = find_best_routes(graph, paths, "red")
        draw_results("red", graph, best_paths)

    elif color == "green":
        best_paths = find_best_routes(graph, paths, "green")
        draw_results("green", graph, best_paths)

    else:
        best_paths = find_best_routes(graph, paths, "white")
        draw_results("white", graph, best_paths)


if __name__ == "__main__":
    main(sys.argv[1:])
