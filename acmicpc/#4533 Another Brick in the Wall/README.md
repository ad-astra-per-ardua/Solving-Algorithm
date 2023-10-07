# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/17.svg" class="solvedac-tier"> [Another Brick in the Wall](https://www.acmicpc.net/problem/4533) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|66902638|per_ardua_ad_astra|맞았습니다!! |116624KB|176ms|PyPy3|2438B|

## 문제
<p>After years as a brick-layer, you've been called upon to analyze the structural integrity of various brick walls built by the Tetrad Corporation. Instead of using regular-sized bricks, the Tetrad Corporation seems overly fond of bricks made out of strange shapes. The structural integrity of a wall can be approximated by the fewest number of bricks that could be removed to create a gap from the top to the bottom. Can you determine that number for various odd walls created by Tetrad?</p>

## 입력
<p>Input to this problem will begin with a line containing a single integer X (1 ≤ X ≤ 100) indicating the number of data sets. Each data set consists of two components:</p>

<ul>
	<li>A single line, "M N" (1 ≤ M,N ≤ 20) where M and N indicate the height and width (in units), respectively, of a brick wall;</li>
	<li>A series of M lines, each N alphabetic characters in length. Each character will indicate to which brick that unit of the wall belongs to. Note that bricks will be contiguous; each unit of a brick will be adjacent (diagonals do not count as adjacent) to another unit of that brick. Multiple bricks may use the same characters for their representation, but any bricks that use identical characters will not be adjacent to each other. All letters will be uppercase.</li>
</ul>

## 출력
<p>For each data set, output the fewest number of bricks to remove to create a gap that leads from some point at the top of the wall, to some point at the bottom of the wall. Assume that bricks are in fixed locations and do not "fall" if bricks are removed from beneath them. A gap consists of contiguous units of removed bricks; each unit of a gap must be adjacent (diagonals do not count) to another unit of the gap. </p>

