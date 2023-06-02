# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/0.svg" class="solvedac-tier"> [Permutation Compression](https://www.acmicpc.net/problem/28177) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|61636655|per_ardua_ad_astra|맞았습니다!! |33236KB|100ms|C++17|1575B|

## 문제
<p>Grammy has a permutation of length $n$. She wants to delete some useless elements in the permutation, so she decided to use some magic tool to delete them. There are $k$ magic tools, the $i$-th of them can delete the maximum element of an interval of length exactly $\ell_i$. Each magic tool can be used at most once.</p>

<p>After each deletion, the length of the array decreases by one, and the neighbors of the deleted element become neighbors themselves.</p>

<p>Before using the tool, Grammy shows you her blueprint of the array after deletion. The new array consists of exactly $m$ distinct elements from $1$ to $n$. Please help Grammy to determine whether it is possible to delete the elements by using the magic tool, so that the result is equal to the blueprint.</p>

## 입력
<p>There are multiple test cases.</p>

<p>The first line contains an integer $T$ ($1 \leq T \leq 10^5$), denoting the number of test cases. </p>

<p>For each test case:</p>

<p>The first line contains three integers $n$, $m$, $k$ ($1 \leq m \leq n \leq 2 \cdot 10^5$, $1\leq k\leq 2\cdot 10^5$), denoting the length of the permutation, the length of the compressed array, and the parameter of the magic tool. </p>

<p>The second line contains $n$ distinct integers $a_i$ ($1 \leq a_i \leq n$), denoting the initial permutation. It is guaranteed that the elements are distinct.</p>

<p>The third line contains $m$ distinct integers $b_i$ ($1 \leq b_i \leq n$), denoting the array after compression. It is guaranteed that the elements are distinct.</p>

<p>The fourth line contains $k$ integers $\ell_i$ ($1 \leq \ell_i \leq n$), denoting the magic tools.</p>

<p>It is guaranteed that $\sum n\leq 2\cdot 10^5$ and $\sum k\leq 2\cdot 10^5$.</p>

## 출력
<p>For each test case, output "<code>YES</code>" or "<code>NO</code>" on a separate line, denoting the answer to the problem. </p>

