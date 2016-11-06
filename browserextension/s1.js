var options = {

	type : "basic",
	 title : "taskc precog", 
	 message : "new notification",
	  iconUrl : "icon.png"

};

chrome.notifications.create(options, callback); // this api is Asynchronous 

console.log('Popup done?')
function callback () {
	// body...
	console.log('Popup done!')
}