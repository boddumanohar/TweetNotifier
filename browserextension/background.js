<script src=/script/jquery.min.js></script>

var options = {

	type : "basic",
	 title : "taskc precog", 
	 message : "realDonaldTrump just tweeted",
	  iconUrl : "icon.png"

};

 // this api is Asynchronous 

console.log('Popup done?')
function callback () {
	// body...
	console.log('Popup done!')
}


setInterval(function(){
    $.ajax({ url: "http://0.0.0.0:5000/", success: function(data){
        //Update your dashboard gauge
        // salesGauge.setValue(data.value);

chrome.notifications.create(options, callback);


    }, dataType: "json"});
}, 30000);