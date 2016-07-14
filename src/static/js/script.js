'use strict';

$(document).ready(function(){
     $('.slider').slider({full_width: true});
 });

 $(document).ready(function(){
 // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
     $('.modal-trigger').leanModal();
 });

var userProfile = {};
var userConcentraions = {};

//Change major
$('.majorRadio').change(function(){
    setUserProflie('major',this.id);
    requestConcentrations(userProfile);
});

//Change level
$('.levelRadio').change(function(){
    setUserProflie('level',this.id);
});

function setUserProflie(attr,value){
    userProfile[attr]=value;
}

function requestConcentrations(){
    var major = userProfile['major'];
    var request = $.ajax({
        url: "/tags",
        type: "GET",
        data: {"major":major},
    });

    request.done(function(response){
        $('#tagDiv').html(response);

        //Change concentrations
        userConcentraions = {};
        $('.conCheckbox').change(function(){
            if (this.checked === true){
                userConcentraions[this.id]=true;
            } else {
                userConcentraions[this.id]=false;
            }
            setUserProflie('concentrations',userConcentraions);
        });

        $('#recBtn').on('click',function(){
            requestRecommendations();
        });
    });

    request.fail(function(response){
        alert("Oops, some error happens...Please try again.");
    });
}

function requestRecommendations(){
    var concens = [];
    var concenKeys = Object.keys(userProfile['concentrations']);
    for(var i = 0; i < concenKeys.length;i++){
        var concen = concenKeys[i];
        if (userProfile['concentrations'][concen] === true){
            concens.push(concen);
        }
    }

    var request = $.ajax({
        url: "/recs",
        type: 'GET',
        data: {
            "major":userProfile['major'],
            "level":userProfile['level'],
            "concen": JSON.stringify(concens)
        },
        contentType:'application/json',
    });

    request.done(function(response){
        $('#recDiv').html(response);
    });

    request.fail(function(){
        alert("Oops, some error happens...Please try again.");
    });
}

