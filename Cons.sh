#!/bin/bash


Gens=( "Binary_Tree" "HaK" "Kruskal" "Prym" "rDFS" "Sidewinder" "Wilsons" )
Sols=("BFS" "DFS" "DIJ" "AStar")


for i in "${!Gens[@]}"; do
	for j in "${!Sols[@]}"; do
		printf "%s %s\n" "${Gens[i]}" "${Sols[j]}"
		python Generators.py 10 10 ${Gens[i]} ${Sols[j]}
done
done
