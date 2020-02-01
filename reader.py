import networkx as nx
import matplotlib.pyplot as plt

from xml.dom.minidom import parse
import xml.dom.minidom
import math
import numpy as np

import os

def calculate_geographical_distance(latlong1, latlong2):
	R = 6373.0

	lat1 = math.radians(latlong1[0])
	lon1 = math.radians(latlong1[1])
	lat2 = math.radians(latlong2[0])
	lon2 = math.radians(latlong2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

	length = R * c
	return length

def read_file(file):
	with open("topologies/" + file, 'r') as nodes_lines:
		for idx, line in enumerate(nodes_lines):
			if line.replace("\n", "") == "1":
				return read_txt_file("topologies/" + file)

def read_txt_file(file):
	graph = nx.Graph()
	nNodes = 0
	nLinks = 0
	with open(file, 'r') as nodes_lines:
		for idx, line in enumerate(nodes_lines):
			if idx > 2 and idx <= nNodes + 2: # skip title line
				info = line.replace("\n", "").replace(",", ".").split("\t")
				graph.add_node(info[0], name=info[1], pos=(float(info[2]), float(info[3])))
			elif idx > 2 + nNodes and idx <= 2 + nNodes + nLinks: # skip title line
				info = line.replace("\n", "").split("\t")
				graph.add_edge(info[1], info[2], id=int(info[0]), weight=int(info[3]))
			elif idx == 1:
				nNodes = int(line)
			elif idx == 2:
				nLinks = int(line)

	return graph
