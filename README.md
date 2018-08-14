# reddit no-hitter bot

Current details:

* Username and password are provided via praw.ini (currently authorized for /u/nohitterbot2)
* Checks MLB Gameday info via the [mlbgame library](http://panz.io/mlbgame/)
* Checks are done every 5 minutes
* If a game is in the 7th inning or later and one team has no hits, a post will be made
* Posting is done via the [praw library](https://praw.readthedocs.io/en/latest/)
* When a post is made, that game ID is added to an array in memory - one for home no-hitters, one for away. Potential no-hitters in these arrays are no longer considered (though a game could have an entry in both)
* The post will have a title of "No-H\*\*\*\*r Alert: <name>", with text of "<name> of the <team> has pitched six hitless innings vs the <other team>. Gameday link: <link>"

Planned updates:

* More error-handling in the event that something doesn't work
* Perfect game alerts?
* Possibly improving the conditions from "7th inning or later". If a home team pitcher pitches 6 hitless innings, the alert currently won't appear until the top 7th, but we could actually display it at the bottom 6th. This is just a little more complicated condition to check
* Extra game viewing/watching info? The old no-hitter bot had radio and TV data, but I didn't see a quick way to access that through the mlbgame api
* Updating bot posts? Like indicating if the bid was successful or broken-up
* Persistent data storage - currently if the bot is reset during a no-hitter bid, it would repost the game