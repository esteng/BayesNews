
function postData(input) {
    $.ajax({
        type: "POST",
        url: "/bayes.py",
        data: { param: input },
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}


window.onload = function(){
  document.getElementById('searchButton').onclick = searchText;
};
function searchText(){
  var search = document.getElementById('searchText').value;
  if(search){
    chrome.tabs.query({active:true,currentWindow:true},function(tabs){
      chrome.tabs.executeScript(tabs[0].id,{file:search.js});
      chrome.tabs.sendMessage(tabs[0].id,{method:'search',searchText:search});
    });
  }
}

postData();