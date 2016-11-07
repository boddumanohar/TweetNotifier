# This is implimnetation of TASK C.
THE IDEA: notify the user when one handles posts a tweet.

In this task, I am doing Chrome pluggin and Developing REST API in python flask and using postgres as database.

---
The URL for API is taskc415.heroku.com


#### Instructions for Using chrome.
-   Load the `browserextension` folder into your chorme extensions 
-   By default you will be followed by _@realDonaldTrump_ and _@HillaryClinton_.
-   To add new handle, go to task415.heroku.com/addhandle 
-   Finally, You will be notifed by the pluggin when one of your handles posts on twitter.

#### API in Python flask.
- The chrome pluggins keeps checking for every 5 secconds for updates.If there is update in any of the handles, the user will be notified of the same.
- The logic of the api is provided in RestAPI folder.

#### ToDo
1. Facebook login
    - problems:
        1. `FB.getLoginStatus()` doesn't fire up. Even if, domain name( taskc415.heroku.com ) domain name and redirectURL are set correctly.
 
    
#### To setup Manually 
1. Go to RestAPI folder
2. create your database and update your environment variable accordingly
3. run setup.py
4. no go to the route /addhandle and add your handle
5. update the permissions in the menifest.json file and add your domain 
6. Now load the chrome extension package and you will be notified when one of the handles posts a tweets 