## TREE = [1, 2, 3, 4, 5, None, None, None, None, 6]
## _IDX = [0, 1, 2, 3, 4, 5,    6,    7,    8,    9]
## Level= [0, 1, 1, 2, 2, 2,    2,    3,    3,    3]

## 부모 노드 의 index 구하기
# class Tree:
#     def __init__(self,tree_list):
#         self.tree = tree_list

#         self.height = self.get_level(len(tree_list))
    
#     def __getitem__(self, idx):
#         return self.tree[idx]
    
#     def get_level(self,idx):
#         height = 0
#         tree_len_without_root = idx
        
#         if len(self.tree) == 1:
#             return 0

#         while tree_len_without_root > 0:
#             height += 1
#             tree_len_without_root -= 2 * height

#         return height + 1
    
#     def get_level(self):
#         pass
        

# a = Tree([1,1,1,1,1,1,1,1])
# print(a.height)