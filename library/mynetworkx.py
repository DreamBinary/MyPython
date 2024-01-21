import networkx as nx
import matplotlib.pyplot as plt
G = nx.dodecahedral_graph()
nx.draw(G)
nx.draw(G, pos=nx.spring_layout(G))  # use spring layout
plt.show()