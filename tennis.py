
def inc_points(pts_p1, pts_p2, winner_id):

	if winner_id == 1:
		pts_winner = pts_p1
		pts_loser = pts_p2
	else:
		pts_winner = pts_p2
		pts_loser = pts_p1

	if pts_winner == 0:
		pts_winner = 15
	elif pts_winner == 15:
		pts_winner = 30
	elif pts_winner == 30:
		pts_winner = 40
	elif pts_winner == 40:
		if pts_loser == 40:
			pts_winner = "Ad."
			pts_loser = " "
		else:
			pts_winner = 0
			pts_loser = 0
	elif pts_winner == "Ad.":
		pts_winner = 0
		pts_loser = 0
	else:
		pts_winner = 40
		pts_loser = 40


	if winner_id == 1:
		return pts_winner, pts_loser
	else:
		return pts_loser, pts_winner