 var app = angular.module('citaSalud', ['ngMaterial', 'users'])
 .config(function($mdThemingProvider, $mdIconProvider){
	$mdIconProvider
		.iconSet("action", "assets/components/svg-material-icons/svg-sprite-action.svg", 24)
		.iconSet("alert", "assets/components/svg-material-icons/svg-sprite-alert.svg", 24)
		.iconSet("av", "assets/components/svg-material-icons/svg-sprite-av.svg", 24)
		.iconSet("communication", "assets/components/svg-material-icons/svg-sprite-communication", 24)
		.iconSet("content", "assets/components/svg-material-icons/svg-sprite-content.svg", 24)
		.iconSet("device", "assets/components/svg-material-icons/svg-sprite-device.svg", 24)
		.iconSet("editor", "assets/components/svg-material-icons/svg-sprite-editor.svg", 24)
		.iconSet("file", "assets/components/svg-material-icons/svg-sprite-file.svg", 24)
		.iconSet("hardware", "assets/components/svg-material-icons/svg-sprite-hardware.svg", 24)
		.iconSet("image", "assets/components/svg-material-icons/svg-sprite-image.svg", 24)
		.iconSet("maps", "assets/components/svg-material-icons/svg-sprite-maps.svg", 24)
		.iconSet("navigation", "assets/components/svg-material-icons/svg-sprite-navigation.svg", 24)
		.iconSet("notification", "assets/components/svg-material-icons/svg-sprite-notification.svg", 24)
		.iconSet("social", "assets/components/svg-material-icons/svg-sprite-social", 24)
		.iconSet("toggle", "assets/components/svg-material-icons/svg-sprite-toggle.svg", 24);
	
	$mdThemingProvider.theme('default')
		.primaryPalette('blue')
    	.accentPalette('blue-grey');
});

app.controller('mainCtrl', function($scope, $mdDialog){
	
	var ipc = require('ipc');
	var messenger = {
		send : function(event, action) {
			ipc.send(event, action);
		}
	};
	
	$scope.loginData = {
		'username' : 'admin',
		'password' : 'admin',
		'remember_pwd' : true
	};
	
	$scope.closeW = function(){
		messenger.send('window-evt', 'close');
	};
	$scope.minW = function(){
		messenger.send('window-evt', 'minimize');
		$scope.hide();
	};
	
	$scope.doLogin = function(){
		$scope.loading();
	};
	
	$scope.loading = function() {
		var parentEl = angular.element(document.querySelector('#internalw'));
	    $mdDialog.show({
		  parent : parentEl,
	      controller: DialogController,
	      template: '<md-progress-circular class="md-accent" md-mode="indeterminate"></md-progress-circular>',
	    })
	    .then(function(answer) {
	      $scope.alert = 'You said the information was "' + answer + '".';
	    }, function() {
	      $scope.alert = 'You cancelled the dialog.';
	    });
		
	};
	
	function DialogController(scope, $mdDialog) {
	    scope.closeDialog = function() {
	      $mdDialog.hide();
	    }
	  }
		  
	$scope.hide = function(){
		$mdDialog.cancel();
	}
});