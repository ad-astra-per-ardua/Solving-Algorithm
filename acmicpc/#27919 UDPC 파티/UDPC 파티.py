votes = input()
yun_votes = votes.count("U") + votes.count("C")
dp_votes = votes.count("D") + votes.count("P")

if (dp_votes + 1) / 2 < yun_votes:
    print("U", end="")
if dp_votes:
    print("DP")
