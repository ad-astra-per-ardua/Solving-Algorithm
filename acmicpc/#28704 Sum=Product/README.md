# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/17.svg" class="solvedac-tier"> [Sum=Product](https://www.acmicpc.net/problem/28704) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|65047871|per_ardua_ad_astra|맞았습니다!! |195560KB|272ms|PyPy3|675B|

## 문제
<p>길이가 $N$인 수열 $A_1, \cdots, A_N$이 주어집니다. 아래 조건을 모두 만족시키는 $(i, j)$ 정수쌍의 개수를 구하세요.</p>

<ul>
	<li>$1 \le i \le j \le N$</li>
	<li>$A_i + A_{i+1} + \cdots + A_j = A_i \times A_{i+1} \times \cdots \times A_j$</li>
</ul>

## 입력
<p>첫 줄에 수열의 길이 $N$이 주어집니다. $(1 \le N \le 300\,000)$</p>

<p>둘째 줄에 $N$개의 정수 $A_1, \cdots, A_N$ 이 공백으로 구분되어 주어집니다. $(1 \le A_i \le 300\,000)$</p>

## 출력
<p>문제의 조건을 만족시키는 $(i, j)$ 정수쌍의 개수를 출력하세요.</p>

