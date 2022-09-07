<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

## 堆排序

- **求堆中第k大的元素**，代价为<font color="green">只与k有关的函数</font>

可能的算法思路：
> 1. 因为堆中第k大的元素至多在第k层，故直接前k层子堆**Heap Sort**，代价为<font color="purple">$O(k2^k)$ </font>。 
2. 与`1.`一致，搜索范围也为前k层的子堆，k次**弹出栈顶and修复**，代价为<font color="purple">$O(k^2)$ </font>。
3. 虽然第k大的元素只可能存在于前k层，但是出现在第k层的概率很低，故可动态利用堆的性质，维护一个**优先级队列**：每次将堆顶元素入队，队首元素出队，将其在堆中对应的左右子节点入队，重复以上操作k次，则第k次弹出的最大元素即为堆中第k大的元素——由于优先级队列至多k个元素，每次修复代价为$O(logk)$，因此k次总代价为<font color="purple">$O(klogk)$ </font>。

相关的题目：[(sorted)最大的k个元素](search.md)

- （**动态发现中值**）有一组元素，它们动态地加入和删除，但是我们需要随时找出当前所有元素的中位数。为此，请设计一个数据结构，支持<font color="purple">对数时间</font>的插入、删除和<font color="purple">常数时间</font>的找出中位数
> key：利用两个堆构建数据结构

``` py
# 动态发现中值
import heapq
# 定义双堆 double heap
class dHeap:
    def __init__(self, l=[]):
        self.Hmin, self.Hmax = [], []  
        # 最小堆(较大元素)和最大堆(较小元素)
```
返回中位数：
``` py
    def median(self):
        if not self.Hmax:
            return "heap is empty"
        if len(self.Hmin) == len(self.Hmax):
            return (self.Hmin[0]-self.Hmax[0])/2
        else:
            return -self.Hmax[0]
```
插入元素：
``` py
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
```
删除元素：
- 删除中值
``` py
    def del_median(self):
        if len(self.Hmax) == len(self.Hmin): 
            heapq.heappop(self.Hmax)
            HminTop = heapq.heappop(self.Hmin)
            heapq.heappush(self.Hmax, -HminTop)
        else:
            heapq.heappop(self.Hmax)
```

- 删除任意元素

> 由于普通堆并没有删除操作，此处可采用**延迟删除**。<br>
> 记录一个待删除集合*delSet*，将待删元素`x`插入集合，每次当*HmaxTop*或*delSet*更新时，检查`if HmaxTop in delSet`，<br>
> `if True` 执行<font color="purple">删除中值</font>算法，同时`delSet.delete(HmaxTop)`，直到`return False`或堆空或*delSet*空

---

[回到主页🍺](../../index.md)