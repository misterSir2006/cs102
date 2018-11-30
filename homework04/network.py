from api import get_friends
import time
import jgraph

def get_network(users_id:int, as_edgelist=True) -> list:
    users_ids = get_friends(user_id)['response']['items']
    edges = []
    matrix = [[0] * num for i in range(num)]

    for userTU in range(num):
    	friends = get_friends(users_ids[userTU])['response']['items']
    	for userPA in range(userTU + 1, num):
    		if users_ids[userPA] in friends:
    			if as_edgelist:
    				edges.append((userTU, userPA))
    			else:
    				matrix[userTU][userPA] = 1
    				matrix[userPA][userTU] = 1
    if as_edgelist:
    	return edges
    return matrix


def plot_graph(user_id: int) -> None:
	surnames = get_friends(user_id, 'last_name')['response']['items']
	vertices = [i['last_name'] for i in surnames]
	edges = get_network(user_id, True)

	OT = igraph.Graph(vertex_artts={'shape': 'circles', 'label': vertices, 'size': 10}, edges=edges, directed=False)

	DI = len(vertices)
	vision = {
    	'vertex_label_list': 1.6,
    	'vertex_size': 20,
    	'edge_color': 'gray',
    	'layout': DI.layout_fruchterman_reingold(maxiter=100000, area=n**2, repulserad=n**2)
    }
	DI.simplify(multiple=True, loops=True)
	clusters = DI.community_multilevel()
	HA = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
	DI.vs['color'] = pal.get_many(clusters.membership)
	igraph.plot(DI, **vision)

if __name__ == '__main__':
	user_id = int(input('Введите id пользователя - '))
	num = get_friends(user_id)['response']['count']
	plot_graph(user_id)