# FreeGameAlert  

## What does this do?
It reads the [RSS feed](https://steamcommunity.com/groups/freegamesfinders/rss/) from [this steam group](https://steamcommunity.com/groups/freegamesfinders/announcements), puts all of the games in the RSS feed into a text file called `games`.  

When the `update_games.py` script is run it will check if the newest added game to the feed is different from the newest game in the `games` file. If the games are different, a new game is free! It will then alert you via email.  

With the way I have this set up - you have to send from a gmail account. You then must create an app password to use for this script (see instructions below)  

All of the cool people tell me to use a burner email to send alerts from, so I just did what they said :D  

## Instructions:  
1. `git clone https://github.com/ecmagnuson/FreeGameAlert.git`  
2. change `auth/emailto` to desired email to send to  
3. change `auth/emailfrom` to desired email to send from - must be a gmail  
4. [create an app password](https://support.google.com/accounts/answer/185833?hl=en) with email we made in step 3  
5. change `auth/app_password` to app password  
6. Running the file `update_games.py` should now work  
  
The games file is a representative of `update_games.update_game_list()` and lists all of the games in the RSS feed  

  

When you change the auth/files, .gitignore won't ignore them because they are tracked. You can make git ignore these files like [this](https://stackoverflow.com/questions/1274057/how-do-i-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore/20241145#20241145)  
For example, to ignore auth and all recursive files  
`git update-index --skip-worktree auth/*`
