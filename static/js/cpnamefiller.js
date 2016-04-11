var cpNames = document.getElementById("footer").innerHTML
var footerText = 
  '<nav class="navbar navbar-inverse navbar-fixed-bottom">'+
      '<div class="container">'+
          '<div class="row">'+
            '<div class="col-md-2 col-sm-3 col-xs-6">'+
                '<a class="navbar-brand" href="/contacts">Contacts</a>'+
            '</div>'+
            '<div class="col-md-6 col-sm-3 col-xs-6">'+
                '<a class="navbar-brand" href="/aboutus">About Us</a>'+
            '</div>';
//footerText+=
//    '<div class="col-md-4 col-sm-6 col-xs-12">'+
//                '<strong class="navbar-text">&copy; 2016 '+cpNames+'</strong>'+
//            '</div>';
footerText+=
        '</div>'+
      '</div>'+
    '</nav>';
document.getElementById("footer").innerHTML = footerText;