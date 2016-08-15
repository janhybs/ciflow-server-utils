<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);
// // 
// system("curl ciflow.nti.tul.cz:8080");
// exec("curl -I ciflow.nti.tul.cz:8080", $o, $rc);
// $is_running = $rc == 0;
// // // exec("whoami", $o, $rc);
// print_r($rc);
// print_r($o);


?><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="img/favicon.ico">

    <title>CI Flow123d main page</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="cover.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <!-- <h3 class="masthead-brand">Cover</h3> -->
              <nav>
                <ul class="nav masthead-nav">
                  <!-- <li class="active"><a href="#">Home</a></li>
                  <li><a href="#">Features</a></li>
                  <li><a href="#">Contact</a></li> -->
                </ul>
              </nav>
            </div>
          </div>

          <div class="inner cover">
              <h1 style="font-size: 6em;">Server list</h1>
              
              <div class="colcol col-md-4">
                  <a href="http://ciflow.nti.tul.cz:8080" target="_blank" class="jd">
                      <h3>Flow123d Jenkins</h3>
                      <p>running @ port 8080</p>
                  </a>
              </div>


              <div class="colcol col-md-4">
                  <a href="http://ciflow.nti.tul.cz:8081" target="_blank" class="j">
                      <h3>Libs Jenkins</h3>
                      <p>running @ port 8081</p>
                  </a>
              </div>


              <div class="colcol col-md-4">
                  <a href="http://ciflow.nti.tul.cz/packages" target="_blank"  class="d">
                      <h3>Libs Datastore</h3>
                      <p>running @ port 80</p>
                  </a>
              </div>
              
            <!-- <h1 class="cover-heading">Cover your page.</h1>
            <p class="lead">Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.</p>
            <p class="lead">
              <a href="#" class="btn btn-lg btn-default">Learn more</a>
            </p> -->
          </div>

          <div class="mastfoot">
            <div class="inner">
              <!-- <p>Cover template for <a href="http://getbootstrap.com">Bootstrap</a>, by <a href="https://twitter.com/mdo">@mdo</a>.</p> -->
            </div>
          </div>

        </div>

      </div>

    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery-3.1.0.slim.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
