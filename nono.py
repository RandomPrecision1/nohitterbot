import mlbgame
import praw
import pprint
import time
import sys
from datetime import datetime

home_nonos = []
away_nonos = []

def submit(reddit, player, player_team, other_team, link):
	word = 'have' if player.find('/') > -1 else 'has'
	text = player + ", of the " + player_team + ", " + word + " pitched five hitless innings vs the " + other_team + ".\n\nGameday link: " + link
	print(text)
	reddit.submit("No-H****r Alert: " + player, text)

def isHomeNoHitter(overview, game):
	if game_id in home_nonos:
		return False
		
	if int(overview.inning) >= 6 and game.away_team_hits <= 0:
		return True
	if int(overview.inning) == 5 and overview.inning_state == 'Bottom' and game.away_team_hits <= 0:
		return True
		
	return False

def isAwayNoHitter(overview, game):
	if game_id in away_nonos:
		return False
		
	if int(overview.inning) >= 6 and game.home_team_hits <= 0:
		return True
		
	return False
	
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
			
			if isHomeNoHitter(overview, game):
				pitcher = ' / '.join(map(lambda x: x.name_display_first_last, playerstats.home_pitching))
				submit(sub, pitcher, home, away, gameday)
				home_nonos.append(game_id)
			if isAwayNoHitter(overview, game):
				pitcher = ' / '.join(map(lambda x: x.name_display_first_last, playerstats.away_pitching))
				submit(sub, pitcher, away, home, gameday)
				away_nonos.append(game_id)
		except KeyboardInterrupt:
			break
		except:
			pass

	print("Sleeping...")
	time.sleep(5 * 60)