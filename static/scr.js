window.onload = install;

var saveAnsButton ;

function install(){
    saveAnsButton = document.getElementById('save_ans');
    saveAnsButton.onclick = saves;
}

function saves(){
    var ans  = $("input:radio[name=name]:checked").val();
    //  confirm("submitted");
   
    var req = new XMLHttpRequest();
    // var XMLHttpRequest: new () => XMLHttpRequest
    
     var url = '/saves/?ans='+ans;
    
    req.open("GET",url,true);
    req.send();
    
}



