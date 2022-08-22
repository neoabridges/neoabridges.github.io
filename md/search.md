<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Search Problems
- （**最大的k个元素**），给定有n个数的集合，现要求其中前k大的k个数（要求排好序），请设计多种基于比较的算法，使其最坏情况时间复杂度满足下列要求：<br>(1) $O(nlogn)$ <br> (2) $O(n+klogn)$ <br> (3) $O(n+k^2)$ <br> (4) $O(n+klogk)$ 

> (1) 先对集合*Heap Sort*或*Merge Sort*，然后输出前k个数。<br>
> (2) $O(n)$建立一个最大堆，然后k次pop。<br>
> (3) $O(n)$建立一个最大堆，然后仅在前k层的子堆上调整，弹出k次堆顶；或<font color="purple">$O(n)$线性选出第k大的数</font> [（详细）](#-on线性选出第k大的数-worst-case-on--)，然后$O(k^2)$对前k大的元素进行排序。<br>
> (4) <font color="purple">$O(n)$线性选出第k大的数</font>，然后$O(klogk)$对前k大的元素*Heap Sort*或*Merge Sort*；或$O(n)$建立最大堆，构建<font color="green">优先级队列[（详细）](#优先级队列-)</font>，$O(klogk)$找到前k大元素

---

# Appendix

### <font color="purple"> O(n)线性选出第k大的数 *worst case* O(n)  </font>

期望线性时间实现很简单，但在最坏情况下，随机元素的划分时间复杂度会达到$O(n^2)$。<br>

***SELECT-WLINEAR：*** <br>

> 1.  所有元素5个分为一组，最后不足5个也作为一组<br>
> 2.  找出每组中位数，共$\lceil \frac{n}{5} \rceil$个
> 3.  对这$\lceil \frac{n}{5} \rceil$个中位数递归地使用**SELECT-WLINEAR**找出其中的中位数$m^{*}$ <br>
> 4.  <font color="purple">基于$m^*$ </font>对所有元素进行划分，假设有$x-1$个元素小于$m^{*}$ ，$n-x$ 个元素大于$m^{*}$ <br>
> 5.  *case* $k = x$ : <font color="RoyalBlue">*return* $m^{*}$ </font> <br>
>    *case* $k < x$ : <font color="RoyalBlue">对小于$m^{*}$ 的元素</font> 递归地调用**SELECT-WLINEAR**查找阶为$k$的元素 <br>
>    *case* $k > x$ : <font color="RoyalBlue">对大于$m^{*}$ 的元素</font> 递归地调用**SELECT-WLINEAR**查找阶为$k-x$的元素 <br>      
    
***SELECT-WLINEAR***时间复杂度$W(n)$满足： <br>

$$ 
W(n) \leq \underbrace{W(\lceil \frac{n}{5} \rceil)}_{递归选择中位数的中位数} + \underbrace{W(\frac{7}{10}n + 6)}_{递归地对三部分元素做选择} + O(n) \tag{*}
$$
其中第二项，在所有$\lceil \frac{n}{5} \rceil$组中，至少有一半的小组要贡献<font color="purple">3个</font>比$m^*$大的元素，其中不包括$m^*$所在组以及可能存在的不足5个元素的组，那么至少要淘汰：
$$
3(\frac{1}{2}\lceil \frac{n}{5} \rceil - 2) \geq \frac{3}{10}n - 6
$$
故最坏情况下算法对规模**不超过** <font color="RoyalBlue"> $\frac{7}{10}n + 6$ </font> 的子问题递归地进行选择。 <br>
可以使用**替换法**证明$W(n) = O(n)$。假设对某个常数$c$，有$W(n) \leq cn$带入递归式$(*)$有：
$$ 
\begin{align}
W(n) \leq & c\lceil \frac{n}{5} \rceil + c(\frac{7}{10}n + 6) +an \\
\leq & c\frac{n}{5} + c + \frac{7}{10}cn + 6c + an \\
= &\frac{9}{10}cn + 7c + an \\
= &cn + (-\frac{1}{10}cn + 7c + an) \\
\end{align}
$$
因而，当 $ - \frac{1}{10}cn + 7c + an \leq 0 \Longrightarrow c \geq 10a \frac{n}{n-70}$ 时，假设成立。<br>
当$n \geq 140$，有$\frac{n}{n-70} \leq 2$ 。所以当 $c \geq 20a$ 时，有 $c \geq 10a \frac{n}{n-70}$ ，即假设成立。

### <font color="green">优先级队列 </font>
