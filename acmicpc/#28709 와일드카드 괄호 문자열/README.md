# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/15.svg" class="solvedac-tier"> [와일드카드 괄호 문자열](https://www.acmicpc.net/problem/28709) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|65046966|per_ardua_ad_astra|맞았습니다!! |143176KB|244ms|PyPy3|1165B|

## 문제
<p>‘<span style="color:#e74c3c;"><code>(</code></span>’, ‘<span style="color:#e74c3c;"><code>)</code></span>’로 이루어진 문자열이 올바른 괄호 문자열이라는 것은 다음을 의미합니다.</p>

<ul>
	<li>$S$가 빈 문자열이면, $S$는 올바른 괄호 문자열입니다.</li>
	<li>$S$가 올바른 괄호 문자열이면, $S$의 앞뒤에 각각 ‘<span style="color:#e74c3c;"><code>(</code></span>’와 ‘<span style="color:#e74c3c;"><code>)</code></span>’를 붙여 만든 문자열 “<span style="color:#e74c3c;"><code>(</code></span>$S$<span style="color:#e74c3c;"><code>)</code></span>” 는 올바른 괄호 문자열입니다.</li>
	<li>$S$와 $T$가 올바른 괄호 문자열이면, $S$와 $T$를 붙여 만든 문자열 “$ST$”는 올바른 괄호 문자열입니다.</li>
	<li>위 세 규칙을 통해 만들 수 없는 문자열은 올바른 괄호 문자열이 아닙니다.</li>
</ul>

<p>예를 들어, “<span style="color:#e74c3c;"><code>(())()</code></span>”, “<span style="color:#e74c3c;"><code>()()</code></span>”은 올바른 괄호 문자열이고 “<span style="color:#e74c3c;"><code>)(</code></span>”, “<span style="color:#e74c3c;"><code>())(</code></span>”는 올바른 괄호문자열이 아닙니다.</p>

<p>문자열 $S$가 주어집니다. $S$는 ‘<span style="color:#e74c3c;"><code>(</code></span>’, ‘<span style="color:#e74c3c;"><code>)</code></span>’, ‘<span style="color:#e74c3c;"><code>?</code></span>’, ‘<span style="color:#e74c3c;"><code>*</code></span>’로 이루어진 문자열입니다. ‘<span style="color:#e74c3c;"><code>?</code></span>’ 문자를 ‘<span style="color:#e74c3c;"><code>(</code></span>’이나 ‘<span style="color:#e74c3c;"><code>)</code></span>’로, ‘<span style="color:#e74c3c;"><code>*</code></span>’ 문자를 ‘<span style="color:#e74c3c;"><code>(</code></span>’와 ‘<span style="color:#e74c3c;"><code>)</code></span>’로 이루어진 길이가 $0$ 이상인 원하는 문자열로 대체하여 $S$를 올바른 괄호 문자열로 만들 수 있나요?</p>

## 입력
<p>첫 줄에 테스트케이스의 수 $T$가 주어집니다. $(1 \le T \le 10\,000)$</p>

<p>각 테스트케이스의 첫 줄에는 ‘<span style="color:#e74c3c;"><code>(</code></span>’, ‘<span style="color:#e74c3c;"><code>)</code></span>’, ‘<span style="color:#e74c3c;"><code>?</code></span>’, ‘<span style="color:#e74c3c;"><code>*</code></span>’로 이루어진 길이가 $1$ 이상 $500\,000$ 이하인 문자열 $S$가 주어집니다.</p>

<p>입력에서 주어진 문자열 $S$의 길이 합은 $500\,000$을 넘지 않습니다.</p>

## 출력
<p>각 테스트케이스마다 한 줄에 하나씩, ‘<span style="color:#e74c3c;"><code>?</code></span>’ 문자를 ‘<span style="color:#e74c3c;"><code>(</code></span>’이나 ‘<span style="color:#e74c3c;"><code>)</code></span>’로, ‘<span style="color:#e74c3c;"><code>*</code></span>’ 문자를 ‘<span style="color:#e74c3c;"><code>(</code></span>’, ‘<span style="color:#e74c3c;"><code>)</code></span>’로 이루어진 길이가 $0$ 이상인 원하는 문자열로 대체하여 $S$를 올바른 괄호 문자열로 만들 수 있다면 “<span style="color:#e74c3c;"><code>YES</code></span>”, 불가능하면 “<span style="color:#e74c3c;"><code>NO</code></span>”를 출력하세요.</p>

