import sys

input = sys.stdin.readline

T = int(input())

def find (node1, node2):
    while node1 != node2:
        if node1 > node2:
            node1 //= 2
        else:
            node2 //= 2
    return node1

for _ in range(T):
    node1_, node2_ = map(int, input().split())
    print(find(node1_, node2_) * 10)