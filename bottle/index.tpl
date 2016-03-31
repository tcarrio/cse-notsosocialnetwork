<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Not-So-Social-Network Index">
    <meta name="author" content="Tom Carrio">
    <!--<link rel="icon" href="../../favicon.ico">-->

    <title>NSSN Home</title>

    <link href="/css/bootstrap.css" rel="stylesheet">

    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

    <!-- Latest compiled JavaScript http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js -->
    <script src="/js/bootstrap.min.js"></script>
      
    <!-- Custom styles for this template -->
    <link href="/css/jumbotron.css" rel="stylesheet">
    <link href="/css/register.css" rel="stylesheet">
    
    </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/index.html">NSSNetwork</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
        <!-- Will need logic to hide this after login 
            Based on server-side logic descerning the user authentication-->
          <form class="navbar-form navbar-right" action="/login" method="post">
            %if status=="bad_login":
            <div class="form-group has-error">
                <input type="text" placeholder="Reenter Email" class="form-control" name="Email">
            %else:
            <div class="form-group">
                <input type="text" placeholder="Email" class="form-control" name="Email">
            %end
            </div>
            %if status=="bad_login":
            <div class="form-group has-error">
                <input type="password" placeholder="Reenter Password" class="form-control" name="Password">
            %else:
            <div class="form-group">
                <input type="password" placeholder="Password" class="form-control" name="Password">
            %end
            </div>  
            <input type="submit" class="btn btn-success" value="Sign in" />
              <a href="/register.html"><p class="btn btn-default">Register</p></a>
          </form>
        </div><!--/.navbar-collapse -->
      </div>
    </nav>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="bg"></div>
    <div class="jumbotron img-header">
      <div class="container">
        <h1>Welcome to the Not-So-Social-Network!</h1>
        <p>This unique social network takes on a new role in the vast pool of sprouting social media services.</p>
        <p><a class="btn btn-primary btn-lg" href="/aboutus.html" role="button">Learn more &raquo;</a></p>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
          <h2>Build</h2>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p><!--
          <p>Show others the kind of work you have accomplished, what you do and what you're interested in. At NSSN you can add information such as a personal introduction, professional history, skills, mentions, and even your social media accounts.</p>-->
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
        </div>
        <div class="col-md-4">
          <h2>Share</h2>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
       </div>
        <div class="col-md-4">
          <h2>Connect</h2>
          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
        </div>
      </div>
      </div>
          
      <nav class="navbar navbar-inverse navbar-fixed-bottom">
          <div class="container">
              <div class="row">
                <div class="col-md-2 col-sm-3 col-xs-6">
                    <a class="navbar-brand" href="/contacts.html">Contacts</a>
                </div>
                <div class="col-md-6 col-sm-3 col-xs-6">
                    <a class="navbar-brand" href="/aboutus.html">About Us</a>
                </div>
            </div>
          </div>
      </nav>

      <script src="/js/parallax.js"></script>
      
  </body>
</html>
