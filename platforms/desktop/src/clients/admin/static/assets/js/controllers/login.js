app.controller('loginCtrl', function($scope, $mdDialog, Auth, $storage, $timeout){
	
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
	    $mdDialog.show({
			clickOutsideToClose: true,
			escapeToClose: true,
			scope: $scope,
          	preserveScope: true,
			template: '<md-dialog aria-label="Iniciando Sesión">' +
           		'<md-dialog-content layout="row" layout-align="center center">'+
				'<md-progress-circular class="md-accent" md-mode="indeterminate"></md-progress-circular>' +
				'&nbsp;&nbsp;<span>Iniciando Sesión...</span>'+ 
				'</md-dialog-content></md-dialog>',
			controller : function($scope, $mdDialog){
				Auth.login($scope.loginData, function(token){
					$timeout(function() { /// simular carga servidor
						messenger.send('login', token);
						console.log(token);
					}, 500);
				}, function(error){
					$mdDialog.cancel();
					
					$timeout(function() { /// simular carga servidor
						console.log(Object.keys(error));
						messenger.send('login', false);
					
						var alert = $mdDialog.alert({
				        	title: 'Error',
				        	content: 'Los credenciales ingresados son incorrectos.',
				        	ok: 'Cerrar'
				     	});
						 
				     	$mdDialog.show(alert)
				        .finally(function() {
				        	// finally what?
				        });
					}, 500);
				});
			}
	    });
	};
	
});