// var options = {

// 	type : "basic",
// 	 title : "taskc precog", 
// 	 message : "realDonaldTrump just tweeted",
// 	  iconUrl : "icon.png"

// };

 // this api is Asynchronous 

console.log('Popup done?')
function callback () {
	// body...
	console.log('Popup done!')
}

function callback2() {
	chrome.notifications.create(options, callback);
}

// function myfunction(){ 
// 		$.get("http://0.0.0.0:5000/", function ( data, status ){
// 			chrome.notifications.create(options, callback);
// 			});
// 		}


function myfunction() {
 console.log()

 $.getJSON('http://0.0.0.0:5000/', function(result){
  for (var i in result) {
  	if(result[i]['count'] > 0){
  	var options = {

	type : "basic",
	 title : "taskc precog", 
	 message : result[i]['name']+" just tweeted",
	  iconUrl : "icon.png"

};	
  		chrome.notifications.create(options, callback);
  	}

}
});

	// chrome.runtime.sendMessage({
 //        method: 'GET',
 //        action: 'xhttp',
 //        url: 'http://0.0.0.0:5000/',
 //        data: ''
 //    }, function(responseText) {
 //        	console.log(responseText)
 //    		chrome.notifications.create(options, callback);
 //    });

// $.ajax({
//   url: "http://0.0.0.0:5000/"})
//   .done(function( data ) {
//     if ( console && console.log ) {
//       console.log( "Sample of data:", data.slice( 0, 100 ) );
//     }
//   });

}
setInterval( myfunction
	 
			 , 5000);