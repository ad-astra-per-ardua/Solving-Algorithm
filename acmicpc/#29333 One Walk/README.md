# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/14.svg" class="solvedac-tier"> [One Walk](https://www.acmicpc.net/problem/29333) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|67678323|per_ardua_ad_astra|맞았습니다!! |210444KB|708ms|PyPy3|1973B|

## 문제
<p><strong>무방향 단순</strong> 그래프 $G$가 주어진다. 이때, 어떤 정점 $S$로부터 다른 정점 $E$까지의 보행이 단 하나가 되도록 $G$의 모든 간선에 방향을 부여하여라. 그래프의 보행이란 같은 정점과 간선을 여러 번 방문할 수 있는 경로를 말한다.</p>

## 입력
<p>첫째 줄에 정점과 간선의 개수 $N$, $M$, 시작점과 도착점의 번호 $S$, $E$가 공백으로 구분되어 주어진다. $(2 \leq N \leq 200\ 000;$ $1 \leq M \leq 300\ 000;$ $1 \leq S, E \leq N;$ $S \neq E)$</p>

<p>둘째 줄부터 $M$개의 줄에 간선으로 연결된 두 정점의 번호 $u$, $v$가 공백으로 구분되어 주어진다. $(1 \leq u, v \leq N)$</p>

## 출력
<p>모든 간선의 방향을 어떻게 정하여도 $S$에서 $E$까지의 보행이 단 하나가 되도록 만들 수 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다. 그렇지 않다면 모든 간선의 방향을 입력된 순서대로 한 줄에 출력한다. $u \rightarrow v$로 방향을 부여했다면 <span style="color:#e74c3c;"><code>0</code></span>, 반대라면 <span style="color:#e74c3c;"><code>1</code></span>을 출력한다.</p>

<p>조건을 만족하는 출력이 여러 가지인 경우 그중 아무거나 출력한다.</p>

