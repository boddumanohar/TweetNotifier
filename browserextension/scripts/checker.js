// var HttpClient = function() {
//     this.get = function(aUrl, aCallback) {
//         var anHttpRequest = new XMLHttpRequest();
//         anHttpRequest.onreadystatechange = function() { 
//             if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
//                 aCallback(anHttpRequest.responseText);
//         }

//         anHttpRequest.open( "GET", 'http://taskc415.heroku.com', true );            
//         anHttpRequest.send( null );
//     }

// }


// aClient = new HttpClient();
// aClient.get('http://taskc415.heroku.com', function(response) {
//     // do something with response
//     alert(response.tweets.counter);
// });

chrome.runtime.sendMessage({
        method: 'GET',
        action: 'xhttp',
        url : 'http://0.0.0.0:5000/'
        // url: 'https://www.facebook.com/v2.8/dialog/oauth?client_id=664416747062739&redirect_uri=http://taskc415.heroku.com'
        
    }, function(responseText) {
        var stringify = JSON.stringify(responseText)
        var resp = JSON.parse(stringify);

         alert(resp.tweets);
    });

//  chrome.runtime.sendMessage({
//         method: 'GET',
//         action: 'xhttp',
//         url: 'http://taskc415.heroku.com'
//     }, function(responseText) {
//     	// var resp = JSON.parse(responseText);
//     	alert(responseText.tweets)

// //     	responseText = responseText.replace(/\\n/g, "\\n")  
// //                .replace(/\\'/g, "\\'")
// //                .replace(/\\"/g, '\\"')
// //                .replace(/\\&/g, "\\&")
// //                .replace(/\\r/g, "\\r")
// //                .replace(/\\t/g, "\\t")
// //                .replace(/\\b/g, "\\b")
// //                .replace(/\\f/g, "\\f");
// // // remove non-printable and other non-valid JsON chars
// // responseText = responseText.replace(/[\u0000-\u0019]+/g,"");
// // chrome.tabs.create({url: 'http://taskc415.heroku.com'});
// // chrome.tabs.create({url: 'http://0.0.0.0:5000/'});

//             });