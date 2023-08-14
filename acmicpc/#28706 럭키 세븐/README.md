# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" class="solvedac-tier"> [럭키 세븐](https://www.acmicpc.net/problem/28706) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|65045055|per_ardua_ad_astra|맞았습니다!! |141976KB|344ms|PyPy3|485B|

## 문제
<p>당신은 양의 정수 $K$를 하나 가지고 있습니다. 처음에 $K=1$입니다.</p>

<p>당신에게는 $N$개의 턴이 주어지고, 각 턴에는 $2$개의 선택지 중 하나를 골라야합니다. 각각의 선택지는 “<span style="color:#e74c3c;"><code>+</code> $v$</span>” 혹은 “<span style="color:#e74c3c;"><code>*</code> $v$</span>”와 같은 방식으로 주어집니다. $(1 \le v \le 9)$</p>

<ul>
	<li>“<span style="color:#e74c3c;"><code>+</code> $v$</span>”: $K$를 $K + v$로 바꿉니다.</li>
	<li>“<span style="color:#e74c3c;"><code>*</code> $v$</span>”: $K$를 $K \times v$로 바꿉니다.</li>
</ul>

<p>선택지를 모두 고른 이후 결과로 나온 $K$가 $7$의 배수가 되도록 할 수 있나요?</p>

## 입력
<p>첫 줄에 테스트케이스의 수 $T$가 주어집니다. $(1 \le T \le 10\,000)$</p>

<p>각 테스트케이스의 첫 줄에 턴의 수 $N$이 주어집니다. $(1 \le N \le 200\,000)$</p>

<p>다음 $N$개의 줄의 $i$번째 줄은 “<span style="color:#e74c3c;">$op_1$ $v_1$ $op_2$ $v_2$</span>”와 같은 방식으로 모든 문자를 공백으로 구분하여 주어집니다. $op_1$과 $op_2$는 ‘<span style="color:#e74c3c;"><code>+</code></span>’ 혹은 ‘<span style="color:#e74c3c;"><code>*</code></span>’이며, $v_1$과 $v_2$는 $1$ 이상 $9$ 이하의 정수입니다. 이는 $i$번째 턴의 선택지가 “<span style="color:#e74c3c;">$op_1$ $v_1$</span>”과 “<span style="color:#e74c3c;">$op_2$ $v_2$</span>”라는 것을 의미합니다.</p>

<p>모든 테스트케이스에서 $N$의 합이 $200\,000$을 넘지 않습니다.</p>

## 출력
<p>각 테스트케이스마다 한 줄에 하나씩, $K$를 $7$의 배수로 만들 수 있다면 “<span style="color:#e74c3c;"><code>LUCKY</code></span>”, 불가능하다면 “<span style="color:#e74c3c;"><code>UNLUCKY</code></span>”를 출력하세요.</p>

