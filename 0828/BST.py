'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key): 
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    
    def delete(self, key):
        # 루트부터 판단 , 삭제할 시, 다른 노드로 대체됨
        self.root = self._delete(self.root , key)

    def _delete(self,node,key):
        # 삭제 결과 그 자리에 있어야할 노드를 리턴

        # 노드 없으면 삭제안함
        if node is None:
            return node 

        # 현재 노드가 삭제 대상인지 판별
        # key 값과 비교해서
        # key < 현재 노드 일때는 왼쪽으로 
        if key < node.key:
            # 현재 노드의 왼쪽을 삭제할지 판단 후
            # 왼족 노드가 삭제 된다면 다른 노드로 대체
            node.left = self._delete(node.left , key)
        # key > 현재 노드 일때는 오른쪽으로
        elif key > node.key:
            # 현재 노드의 오른쪽을 삭제할지 판단 후
            # 왼족 노드가 삭제 된다면 다른 노드로 대체
            node.right = self._delete(node.right , key)
        else:
            # 1. 단말노드
            if node.left is None and node.right is None:
                node = None
            # 2. 자식이 하나 왼쪽 or 오른쪽
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # 3. 자식이 둘다 있음
            else:
                #3_1 왼쪽 서브트리 최댓값 
                #3_2 오른쪽 서브트리 최솟값 
                min_node_from_right = self._get_min(node.right)
                node.key = min_node_from_right.key
                # 내가 찾을 최소 노드를 여기 위치로 가지고옴
                # 그 최소 노드가 원래 있던 자리도 누군가 대체
                node.right = self._delete(node.right , min_node_from_right.key)
        return node 



    def _get_min(self,node):
        while node.left is not None:
            node = node.left
        return node
    def _get_max(self,node):
        while node.right is not None:
            node = node.right
        return node



    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key): # node : 현재바라보고 있는  노드 # key : 찾고자하는 값
        if node is None or node.key == key: # 노드에 값이 없거나(못찾음) 찾음
            return node # 그때의 노드 return
        if key < node.key: # node.key : 현재노드의 값  ==> 찾을 값보다 큰 노드의 값
            return self._search(node.left, key) # ==> 왼쪽값을 노드로하여 다시 search  
        else: # key > node.key
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

print()
bst.delete(4)
print("중위 순회 결과:", end=' ')
bst.inorder_traversal()

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
