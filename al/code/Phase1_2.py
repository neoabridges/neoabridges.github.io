# find all anagrams in an article

# A MIDSUMMER-NIGHT'S DREAM(src1.txt)
file_path = ("src.txt")

# toker
""" 
with open(file_path, 'r') as f:
    file = f.read()
file = file.split()
"""
#print(file)

def print_map(m):
    for k, v in m.items():
        print("{:<16}{}".format(k, v))
    
def generate_anagram_map(f):
    Map = {}
    for word in f:
        key = "".join(sorted(word))
        if word == key:
            pass
        elif key in Map.keys() and not word in Map[key]:
            Map[key].append(word)
        else:
            Map.update({key:[word]})
    for k in list(Map.keys()):
        if len(Map[k]) == 1:
            del Map[k]
    # return Map
    print_map(Map)



def pre_larger(A):
    P = {}
    for i in range(1, len(A)+1):
        j = i-1
        while j > 0 and A[j-1] <= A[i-1]:
            if j in P.keys():
                j = P[j]
            else:
                j -= 1
        if j > 0:
            P.update({i:j})
    return P

# n个k元素有序数组合并，要求在O(nklogk)时间内完成（可假设k = 2**x，x为整数）
'''
merge-merge
'''

# O(n)算法计算二叉树的高度
from def_lib.tree_def import Tree

def tree_height(self):
    if self.label is None:
        return -1
    elif not self.branches:
        return 0
    else:
        return max(tree_height(self.branches[0]), tree_height(self.branches[1])) + 1

Tree.height = tree_height # 引入作为class func

# O(n)算法计算二叉树的直径
"""
定义两点距离为它们之间最短距离的路径的长度，则定义树的直径为🌲中节点距离的最大值
leetcode reference src: https://leetcode.cn/problems/diameter-of-binary-tree/
"""
def tree_diameter(self):
    """
    我的理解：找到不交叉的高度最高的两棵（同父节点）子🌲
    if self.label is None:
        return -1
    if not t.branches:
        return 0
    else:
        d = tree_height(t.branches[0]) + tree_height(t.branches[1])
        return max(d, max(tree_diameter(t.branches[0]), tree_diameter(t.branches[1])))
    """
    # 改写tree_height()，以压缩时间复杂度
    res = 0
    def h(t):
        nonlocal res
        if t.label is None:
            return -1
        elif not t.branches:
            return 0

        l, r = h(t.branches[0])+1, h(t.branches[1])+1
        res = max(res, l+r)
        return max(l, r)
    h(self)
    return res

# 巧妙的思路：以任意的节点s为根，调用height得到hs，并保留对应叶节点w，接着再以w为根，调用height
# 得到hw，则d = hw，易知该算法只调用两次height，也为O(n)

Tree.diameter = tree_diameter
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了 返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
""" 

# 动态发现中值
import heapq
# 定义双堆 double heap
class dHeap:
    def __init__(self, l=[]):
        self.Hmin, self.Hmax = [], []   # 最小堆(较大元素)和最大堆(较小元素)
 
                
    def median(self):
        if not self.Hmax:
            return "heap is empty"
        if len(self.Hmin) == len(self.Hmax):
            return (self.Hmin[0]-self.Hmax[0])/2
        else:
            return -self.Hmax[0]
    
    def insert(self, l):
        assert isinstance(l, list)
        # make sure Hmin.size <= Hmax.size <= Hmin.size+1  
        for item in l:
            if not self.Hmax:
                    self.Hmax.append(-item)
            elif len(self.Hmax) == len(self.Hmin):  
                if item > -self.Hmax[0]:
                    heapq.heappush(self.Hmin, item)
                    HminTop = heapq.heappop(self.Hmin)
                    # since heapq doesn't support push MaxHeaP
                    # Hmax中保存的都是元素的相反数
                    heapq.heappush(self.Hmax, -HminTop)
                else:
                    heapq.heappush(self.Hmax, -item)
                    
            # NOW Hmin.size+1 == Hmax.size
            else:
                if item > -self.Hmax[0]:
                    heapq.heappush(self.Hmin, item)
                else:
                    heapq.heappush(self.Hmax, -item)
                    HmaxTop = -heapq.heappop(self.Hmax)
                    heapq.heappush(self.Hmin, HmaxTop)
    
    def del_median(self):
        if len(self.Hmax) == len(self.Hmin): 
            heapq.heappop(self.Hmax)
            HminTop = heapq.heappop(self.Hmin)
            heapq.heappush(self.Hmax, -HminTop)
        else:
            heapq.heappop(self.Hmax)

    def delete(self, item):
        delSet = [] # 待删数组
        
        
    def __repr__(self) -> str:
        return ''.join(str([-i for i in self.Hmax]) + str(self.Hmin))
    def __str__(self):
        def str_Hmin(heap, depth):
            res = ''
            curLast = min(2**(depth+1)-1, len(heap))
            if(len(heap) > 2**(depth+1)-1):
                res += str_Hmin(heap, depth+1)+'\n'
            for i in range(2**depth-1, curLast):
                res += str(heap[i]) + ' '
            return res
        def str_Hmax(heap, depth):
            res = ''
            curLast = min(2**(depth+1)-1, len(heap))
            for i in range(2**depth-1, curLast):
                res += str(-heap[i]) + ' '
            res += '\n'
            if(len(heap) > 2**(depth+1)-1):
                res += str_Hmax(heap, depth+1)
            return res
        return str_Hmin(self.Hmin, 0) + '\n\n' + str_Hmax(self.Hmax, 0)