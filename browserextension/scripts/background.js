chrome.runtime.onInstalled.addListener(function(object) {

    if (localStorage.firsttime != 'false' || localStorage.firsttime == 'undefined' || !localStorage.firsttime) {
        var optionsurl = chrome.extension.getURL("options.html");
        chrome.tabs.create({
            url: optionsurl
        }, function(tab) {});

        localStorage.firsttime = false;
    }

    var currentversion = chrome.app.getDetails().version;

    if (!localStorage.version || localStorage.version != currentversion) {
        chrome.browserAction.setBadgeText({
            text: "Login with facebook"
        });
        localStorage.version = currentversion

    }
});

chrome.browserAction.onClicked.addListener(function (tab) { //Fired when User Clicks ICON
     // chrome.tabs.create({url: "https://www.google.co.in/#q=pnr+status"});
     
});