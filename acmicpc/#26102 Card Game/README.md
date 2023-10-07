# <img width="20px"  src="https://d2gd6pc034wcta.cloudfront.net/tier/21.svg" class="solvedac-tier"> [Card Game](https://www.acmicpc.net/problem/26102) 

| 제출 번호 | 닉네임 | 채점 결과 | 메모리 | 시간 | 언어 | 코드 길이 |
|---|---|---|---|---|---|---|
|67607058|per_ardua_ad_astra|맞았습니다!! |155968KB|2304ms|PyPy3|2242B|

## 문제
<p>Alice and Bob play a game of taking turns removing cards from the grid board. At the beginning of the game, there is one card in each cell of the $N \times M$ sized grid board, and each card is painted in one of three colors: red, black, or green. In the grid, the position of the upper-left cell is indicated by $(1,1)$, and the position of the lowerright cell is indicated by $(N, M)$.</p>

<p>Alice and Bob choose one of the cards placed on the grid, and then remove the cards according to the rules below.</p>

<ul>
	<li>If the color of the chosen card is red, all 'connected cards' placed on a diagonal with a slope of $1$ based on it are removed.</li>
	<li>If the color of the chosen card is blue, all 'connected cards' placed on a diagonal with a slope of $-1$ based on it are removed.</li>
	<li>If the color of the chose card is green, all 'connected cards' placed on the diagonal in both directions based on it are removed.</li>
</ul>

<p>'Connected cards' to the chosen card are consecutively adjacent cards along a diagonal with a slope of $1$ or $-1$ including the chosen card.</p>

<p>For example, when the current board situation during the game is as in Figure A.1, let the chosen card be a red card placed at $(4,3)$. As shown in Figure A.1, 'connected cards' placed on the diagonal line with a slope of $1$ refer to the cards placed in the oval circle, which should be removed. That is, cards placed in the cells on the movement path while moving diagonally in both directions from the position $(4,3)$ are 'connected cards'. However, while moving in both directions along the diagonal at the chosen cell $(4,3)$, if it encounters a grid boundary or a blank cell, the movement stops.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e8e7b9d1-16ef-479d-951d-3b5760fc4409/-/preview/" style="width: 291px; height: 180px;"></p>

<p style="text-align: center;">Figure A.1. An example to illustrate connected cards to the red card at $(4, 3)$</p>

<p>Similarly, when the current board situation during the game is as shown in Figure A.2, let the chosen card be the blue card placed at $(3,5)$. As shown in Figure A.2, 'connected cards' placed on the diagonal line with a slope of $-1$ refer to the cards placed in the oval circle, which should be removed.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b45ab339-ec28-42e4-a6e9-409e6a53c5db/-/preview/" style="width: 291px; height: 180px;"></p>

<p style="text-align: center;">Figure A.2. An example to illustrate connected cards to the blue card at $(3, 5)$</p>

<p>Figure A.3 shows the cards to be removed when the chosen card is green card placed at $(4,5)$.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8c759ae4-2c05-40b1-b029-95f3bf06e597/-/preview/" style="width: 291px; height: 179px;"></p>

<p style="text-align: center;">Figure A.3. An example to illustrate connected cards to the green card at $(4, 5)$</p>

<p>Alice and Bob alternately choose a card from the grid, and according to the color of the chosen card, remove the 'connected cards' according to the rules described above. Whoever removes the last card wins the game. That is, the player who cannot remove any card because there are no cards to choose from on the grid loses the game. Both Alice and Bob have a good understanding of the strategy of how to win the game and do their best to win.</p>

<p>Given the size of the grid board and the information on color of the cards placed on the board, write a program to determine whether Alice can win when she starts the game.</p>

## 입력
<p>Your program is to read from standard input. The input starts with a line containing two integers, $N$ and $M$ ($1 ≤ N, M ≤ 25$), where $N$ is the number of rows and $M$ is the number of columns of the grid. In the following $N$ lines, the $i$-th line contains a string of length $M$, which represents the colors of the $M$ cards in the $i$-th row in the grid. Every character in the string is either ‘<code>R</code>’, ‘<code>B</code>’, or ‘<code>G</code>’, which stands for red, blue, or green, respectively.</p>

## 출력
<p>Your program is to write to standard output. Print exactly one line. The line should contain an upper-case letter: either ‘<code>W</code>’ if Alice wins or ‘<code>L</code>’ if Alice loses.</p>

