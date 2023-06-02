# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" class="solvedac-tier"> [TreeScript](https://www.acmicpc.net/problem/28166) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|61636704|per_ardua_ad_astra|맞았습니다!! |100080KB|712ms|Python 3|635B|

## 문제
<p>TreeScript is a programming language developed for maintaining tree structures. In this problem, we will learn how to create rooted trees in TreeScript.</p>

<p>In TreeScript, all tree nodes are stored in memory. Each tree node has a number and the address of its parent node, and both are immutable, so they have to be determined when creating the node. In particular, the address of the root node's parent node is empty.</p>

<p>In order to access these nodes, the address of a node can be stored in a register. If there are $m$ registers, the registers can be written as $r[0],r[1],\ldots ,r[m-1]$. </p>

<p>Now let's learn the node creation statement: $$r[i]=\mathrm{create}(r[j], k);$$ where $k$ is the node number, $i$ and $j$ are the indices of the registers, where $0\le i,j< m$ and $i=j$ is possible. The effect of this statement is that a node numbered $k$ is created, whose parent address is stored in $r[j]$, and then the new node's address is stored in $r[i]$. Once each node has been created correctly, you do not need to store the address of any more nodes; they will automatically execute the pre-defined instructions. For reasons of space, we will learn about them later.</p>

<p>To check your learning, you need to create a rooted tree of size $n$. At first, the system will automatically create the root node for you and store it in $r[0]$. So you only need to execute $n-1$ additional creation instructions to create the tree.</p>

<p>As you know, registers are very expensive, so you need to find the minimum amount $m$ of the registers you need.</p>

## 입력
<p>There are multiple test cases.</p>

<p>The first line of the input contains one integer $T$ ($1\le T\le 10^5$) --- the number of test cases.</p>

<p>For each test case:</p>

<p>The first line contains one integer $n$ ($2\le n\le 2\cdot 10^5$) --- the size of the tree.</p>

<p>The second line contains $n$ integers $p_1,p_2,\ldots,p_n$, where node $p_i$ is the parent node of node $i$ and $1\le p_i<i$. Specially, $p_1=0$ and it means $1$ is the root of the tree.</p>

<p>The sum of $n$ over all test cases does not exceed $2\times 10^5$.</p>

## 출력
<p>For each test case, output the answer in one line.</p>

