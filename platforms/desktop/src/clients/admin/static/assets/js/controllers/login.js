app.controller('loginCtrl', function($scope, $mdDialog, Auth, $storage, $timeout){
	
	$scope.loginData = {
		'username' : '',
		'password' : ''
	};
	
	var login_data_exists = $storage.get('loginData');

	if (login_data_exists){
		$scope.loginData = login_data_exists;
	}
	
	$scope.remember_pwd = true;
	
	$scope.closeW = function(){
		messenger.send('window-evt', 'close');
	};
	$scope.minW = function(){
		messenger.send('window-evt', 'minimize');
		$scope.hide();
	};
	
	$scope.doLogin = function() {
	    $mdDialog.show({
			clickOutsideToClose: true,
			escapeToClose: true,
			scope: $scope,
          	preserveScope: true,
			template:
				'<md-dialog aria-label="Iniciando Sesión">' +
           		'    <md-dialog-content layout="row" layout-align="center center">' +
				'        <md-progress-circular class="md-accent" md-mode="indeterminate"></md-progress-circular>' +
				'        &nbsp;&nbsp;<span>Iniciando Sesión...</span>' + 
				'    </md-dialog-content>' +
				'</md-dialog>',
			controller : function($scope, $mdDialog){
				Auth.login($scope.loginData, function(token){
					$timeout(function() { /// Simular carga servidor
						if ($scope.remember_pwd){
							$storage.set('loginData', $scope.loginData);
						} else {
							$storage.clear('accessToken');
							$storage.clear('loginData');
						}
						messenger.send('login', token); // Enviar token
					}, 500);
				}, function(error){
					$mdDialog.cancel(); // Hace un reject a la promise que retorna $mdDialog.show()
				
					$timeout(function() { /// Simular carga servidor
						messenger.send('login', false);
						var alert = $mdDialog.alert({ // Opciones de la ventana de alerta
				        	title: 'Error',
				        	content: 'Los credenciales ingresados son incorrectos.',
				        	ok: 'Cerrar'
				     	});
						 
				     	$mdDialog.show(alert) // Muestra la ventana de alerta.
				        .finally(function() {
				        	// finally what?
				        });
					}, 500);
				});
			}
	    });
	};
	
});