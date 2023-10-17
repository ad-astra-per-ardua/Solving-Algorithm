# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/17.svg" class="solvedac-tier"> [2-SAT - 3](https://www.acmicpc.net/problem/11280) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|68126846|per_ardua_ad_astra|맞았습니다!! |651368KB|1160ms|PyPy3|1681B|

## 문제
<p>2-SAT은 N개의 불리언 변수 \(x_1, x_2, ..., x_n\)가 있을 때, 2-CNF 식을 true로 만들기위해 \(x_i\)를 어떤 값으로 정해야하는지를 구하는 문제이다.</p>

<p>2-CNF식은 \( \left( x \lor y \right) \land \left( \lnot y \lor z \right) \land \left( x \lor \lnot z \right) \land \left( z \lor y \right) \) 와 같은 형태이다. 여기서 괄호로 묶인 식을 절(clause)라고 하는데, 절은 2개의 변수를 \(\lor\)한 것으로 이루어져 있다. \(\lor\)는 OR, \(\land\)는 AND, \(\lnot\)은 NOT을 나타낸다.</p>

<p>변수의 개수 N과 절의 개수 M, 그리고 식 \(f\)가 주어졌을 때, 식 \(f\)를 true로 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.</p>

<p>예를 들어, N = 3, M = 4이고, \(f =  \left( \lnot x_1 \lor x_2 \right) \land \left( \lnot x_2 \lor x_3 \right) \land \left( x_1 \lor x_3 \right) \land \left( x_3 \lor x_2 \right) \) 인 경우에 \(x_1\)을 false, \(x_2\)을 false, \(x_3\)를 true로 정하면 식 \(f\)를 true로 만들 수 있다. 하지만, N = 1, M = 2이고, \(f = \left( x_1 \lor x_1 \right) \land \left( \lnot x_1 \lor \lnot x_1 \right) \)인 경우에는 \(x_1\)에 어떤 값을 넣어도 식 f를 true로 만들 수 없다.</p>

## 입력
<p>첫째 줄에 변수의 개수 N (1 ≤ N ≤ 10,000)과 절의 개수 M (1 ≤ M ≤ 100,000)이 주어진다. 둘째 줄부터 M개의 줄에는 절이 주어진다. 절은 두 정수 i와 j (1 ≤ |i|, |j| ≤ N)로 이루어져 있으며, i와 j가 양수인 경우에는 각각 \(x_i\), \(x_j\)를 나타내고, 음수인 경우에는 \(\lnot x_{-i}\), \(\lnot x_{-j}\)를 나타낸다.</p>

## 출력
<p>첫째 줄에 식 \(f\)를 true로 만들 수 있으면 1을, 없으면 0을 출력한다.</p>

