# https://www.acmicpc.net/problem/14725
import sys
sys.stdin = open("./input/14725.txt")
input = sys.stdin.readline
# ----------------------------------------

def set_house(ant_house: object, foods: list):
    if not len(foods):
        return
    
    parent, *child = foods
    ant_house[parent] = ant_house.get(parent, {})
    set_house(ant_house[parent], child)

def print_parent(ant_house, level):
    for parent in sorted(ant_house):
        print("--" * level + parent)
        print_parent(ant_house[parent], level + 1)

# ----------------------------------------
house = {}
for _ in range(int(input())):
    _, *foods = input().split()
    set_house(house, foods)

print_parent(house, 0)