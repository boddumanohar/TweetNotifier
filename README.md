# This is implimnetation of TASK C.
THE IDEA: notify the user when one handles posts a tweet.

In this task, I am doing Chrome pluggin and Developing REST API in python flask and using postgres as database.

---

#### Instructions for Using chrome.
-   Load the `browserextension` folder into your chorme extensions 
-   Next *login with Your Facebook account* this creates an account for you.
-   By default you will be followed by _@realDonaldTrump_ and _@HillaryClinton_.
-   Later interface will be provided within the application to develop your you
-   Finally, You will be notifed by the pluggin when one of your handles posts on twitter.

#### API in Python flask.
- When the user signs in/up, facebook will verify the user and gives an ID associated with for that user. If such user doesn't exists, then that ID will be stored in a database and handles  _@realDonaldTrump_ and _@HillaryClinton_ shall be added by default.
- The chrome pluggins keeps checking for every 5min for updates.If there is update in any of the handles, the user will be notified of the same.

