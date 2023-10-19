# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/21.svg" class="solvedac-tier"> [피보나치 단어](https://www.acmicpc.net/problem/4206) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|68232102|per_ardua_ad_astra|맞았습니다!! |113428KB|280ms|PyPy3|2510B|

## 문제
<p>
	피보나치 단어 수열은 다음과 같이 정의된다.</p>
<p>
	<img alt="" src="https://www.acmicpc.net/upload/images/fibo.png" style="width: 291px; height: 76px;"></p>
<p>
	여기서 +는 두 문자열 이어 붙이는 것을 의미한다.</p>
<table class="table table-bordered table-condensed" style="width: 50%;">
	<thead>
		<tr>
			<td style="width:5%;">
				n</td>
			<td style="width:45%;">
				F(n)</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				0</td>
			<td>
				0</td>
		</tr>
		<tr>
			<td>
				1</td>
			<td>
				1</td>
		</tr>
		<tr>
			<td>
				2</td>
			<td>
				10</td>
		</tr>
		<tr>
			<td>
				3</td>
			<td>
				101</td>
		</tr>
		<tr>
			<td>
				4</td>
			<td>
				10110</td>
		</tr>
		<tr>
			<td>
				5</td>
			<td>
				10110101</td>
		</tr>
		<tr>
			<td>
				6</td>
			<td>
				1011010110110</td>
		</tr>
		<tr>
			<td>
				7</td>
			<td>
				101101011011010110101</td>
		</tr>
		<tr>
			<td>
				8</td>
			<td>
				1011010110110101101011011010110110</td>
		</tr>
		<tr>
			<td>
				9</td>
			<td>
				1011010110110101101011011010110110101101011011010110101</td>
		</tr>
	</tbody>
</table>
<p>
	비트 패턴 p와 정수 n이 주어졌을 때, F(n)에 p가 몇 번 나오는지 구하는 프로그램을 작성하시오.</p>

## 입력
<p>
	테스트 케이스의 첫째 줄에는 n(0 ≤ n ≤ 100)이 주어진다. 둘째 줄에는 비트 패턴 p가 주어진다. p의 길이는 최대 100,000이고 비어있지 않은 문자열이다.</p>

## 출력
<p>
	각각의 테스트 케이스에 대해서, 케이스 번호와 F(n)에서 비트 패턴 p가 몇 번 등장하는지 출력한다. 이런 등장은 겹칠 수 있다. 이 값은 2<sup>63</sup>보다 작다.</p>

