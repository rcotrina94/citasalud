app.factory('Auth', function($http, $q, $window, $storage){
	var getTokenURL = 'http://localhost:8000/api/auth/token/';
	var accessToken;

	var doLogin = function(loginData){
		var deferred = $q.defer();

		var req = {
			method: 'POST',
			url: getTokenURL,
			data: loginData
		};

		$http(req).then(function(result){
			accessToken = result.data.token;
	      	deferred.resolve(accessToken);

		}, function(error){
			deferred.reject(error);
		});

		return deferred.promise;

	}
	
	var login = function(credentials, success_handler, error_handler){
		doLogin(credentials).then(function (response_token){
			$storage.set('accessToken', response_token);
			return success_handler(response_token);
		}, function (e){
			if (typeof error_handler == 'function'){
				if (e.status == 401 || e.status == 400){
					return error_handler({
						invalid : true
					});
				} else {
					return e;
				}
			}
		});
	};
		
	return {
		login : login,
		getToken : function(){
			return $storage.get('accessToken');
		}
	}

})
