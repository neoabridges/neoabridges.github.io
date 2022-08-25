<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

## log(n) 搜索
<font size=5>Essential of se<font color="green">arch</font>ing</font> --- *architecture*，好的数据结构会使搜索高效简洁<br> [jwgg课件](slides/L8.pdf)

### 常见的log(n)搜索方式

- 二分搜索 <font color="purple">有序</font> 序列
- BST——二叉搜索树 <br> e.g.红黑树

### Red-Black-Tree
-  **红黑树的高度** <br> 
对于有<font color="Royalblue">n个内部节点</font>的红黑树，不存在黑色高度大于<font color="purple">log(n+1)</font>的节点；同时该红黑树的普通高度不超过<font color="purple">2log(n+1)</font>；基于红黑树的查找代价为<font color="purple">O(log n)</font>。

- **向红黑树中insert和delete元素** <br>
[参考解析link](https://www.cnblogs.com/fingerdancing/archive/2013/04/14/rbTree.html)🙋 <br> 
为保持红黑树结构，经过**二叉搜索树类似**插入元素后，需要进行染色来**fixup**

### 思考题
- 设计计算$\lfloor \sqrt{N} \rfloor$的算法，时间复杂度要求为$O(n)$

> 分析 : 若对小于$N$的整数进行二分查找，最多进行$log N = n$次查找，每次查找的代价为计算$x^2$的代价: $O(n)$次移位和加法操作，故代价为$O(n^2)$ <br>
> key : 每次都独立计算$x^2$可优化，使计算代价缩减到$O(1)$ <br>

找出每次查询目标的迭代公式即可： <br>
**注意**： `(1)` 要判断查询是否成功，既需要 $m^2$ 也需要 $(m+1)^2$ `(2)` 最后要返回的是 m 。<br>
设第*k*次的查询区间为(a, b)，则：$$ m= \frac{a+b}{2}, m^2 = \frac{(b+a)^2}{4} = \frac{1}{4}(a^2+b^2+2ab) $$ <br>
  *case 1* : $m^2 \leq N, (m+1)^2 > N$ ，查询成功，return m <br>
  *case 2* : $m^2 > N$ ，则第 *k+1* 次的查询区间为 $(a, \frac{b+a}{2})$ ，则：
  $$ m_l = \frac{a+ \frac{b+a}{2}}{2} = \frac{1}{4}(b+3a) , m_{l}^{2} = \frac{1}{16}(9a^2 + b^2 +6ab) $$ 
  *case 3* : 其他情况，第*k+1*次的查询区间为 $(\frac{b+a}{2}, b)$ ，则： 
  $$ m_r = \frac{b+ \frac{b+a}{2}}{2} = \frac{1}{4}(a+3b) , m_{r}^{2} = \frac{1}{16}(a^2 + 9b^2 + 6ab) $$ 

易知： $m$是$a，b$的线性组合，$m^2$是$a^2, b^2, ab$的线性组合，$(m+1)^2$是$m, m^2$的线性组合，因此下次查询只需要<font color="purple">更新 $a, b, a^2, b^2, ab$ 的系数</font>即可，代价为$O(1)$ ，预处理计算$a^2, b^2, ab$ 代价为$O(n)$ ，而递归式：$T(N) = T(\frac{N}{2})+O(1) \Longrightarrow T(N) = O(log N) = O(n)$ ，故最终算法复杂度为$O(n)$ 。

- [leetcode题解](https://leetcode.cn/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/) 🍺
