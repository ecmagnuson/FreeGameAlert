# FreeGameAlert  

how to use:  
1. `git clone https://github.com/ecmagnuson/FreeGameAlert.git`  
2. change `auth/email` to desired email to send to  
3. [create an app password](https://support.google.com/accounts/answer/185833?hl=en) with desire google account  
4. change `auth/app_password` to app password  
5. Running the file `update_games.py` should now work  
  
  

When you change the auth/ files .gitignore won't ignore them because they are tracked. You can make git ignore these files like [this](https://stackoverflow.com/questions/1274057/how-do-i-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore/20241145#20241145)  

`git update-index --skip-worktree auth/*`
