(function()
{
  var app = angular.module("Colorize!",['hmTouchEvents','ngclipboard']);

  var MainController = function($scope, $http, $log,$interval)
  {

    var onConnection = function(response){
      $scope.color = response.data.color;
      $scope.complement = response.data.complemento;
    };

    var onError = function(){
      $log.info("Error al conectar");
    };

    $scope.change = function(){
      if($scope.name !=""){
        checkBlank = false;
        $http.get("https://colorize.com.ar/gc/"+$scope.name).then(onConnection, onError);
      }
      else {
        checkBlank = true;
      }
    };

    $scope.style = function(color) {
      return { "background-color":color}
    };

    $scope.blank = function(){
      if (checkBlank == true) {
        return {"border": 'solid 2px red'}
      }
    };

    var checkBlank = false;
    $scope.color = "#000000";
    $scope.complement = "";
    $scope.name = "";


  };
  app.controller("MainController",["$scope","$http","$log","$interval",'hmTouchEvents',MainController]);
}());
