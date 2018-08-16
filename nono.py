import mlbgame
import praw
import pprint
import time
import sys
from datetime import datetime

home_nonos = []
away_nonos = []

while True:
	print("Checking at {0}".format(str(datetime.now())))
	r = praw.Reddit('nonobot', user_agent='Mike Trout')
	
	sub = r.subreddit('randomnono')
	
	now = datetime.now()
	
	games = mlbgame.day(now.year,now.month,now.day)
	for game in games:
		try:
			game_id = game.game_id
			overview = mlbgame.overview(game_id)
			playerstats = mlbgame.player_stats(game_id)
			
			home = game.home_team
			away = game.away_team
			gameday = "http://mlb.mlb.com/mlb/gameday/index.jsp?gid=" + overview.gameday_link
			
			if overview.inning >= 6 and game.away_team_hits <= 0 and game_id not in home_nonos:
				pitcher = playerstats.home_pitching[0].name_display_first_last
				text = pitcher + ", of the " + home + " has pitched five hitless innings vs the " + away + ".\n\nGameday link: " + gameday
				sub.submit("No-H****r Alert: " + pitcher, text)
				home_nonos.append(game_id)
			if overview.inning >= 6 and game.home_team_hits <= 0 and game_id not in away_nonos:
				pitcher = playerstats.away_pitching[0].name_display_first_last
				text = pitcher + ", of the " + away + " has pitched five hitless innings vs the " + home + ".\n\nGameday link: " + gameday
				sub.submit("No-H****r Alert: " + pitcher, text)
				away_nonos.append(game_id)
		except KeyboardInterrupt:
			break
		except:
			pass

	print("Sleeping...")
	time.sleep(5 * 60)