app.factory('$db', function($http, $q, Auth){
	var baseURL = 'http://localhost:8000/api/';
	
	var token_header = function(){
		return { 'Authorization' : 'Token ' + Auth.getToken() };
	};
	var Request = {
		get : function(url, params){
			var userInfo;
	
			var deferred = $q.defer();
	
			var req = {
				method: 'GET',
				headers : token_header,
				url: baseURL + url
			}
			if (params){
				req['params'] = params
			}
	
			$http(req).then(function(result){
				userInfo = result.data;
			  	deferred.resolve(userInfo);
	
			}, function(error){
				console.log(error)
				deferred.reject(error);
			});
	
			return deferred.promise;
		}
	};
	
	var userProfile = function(user_id){
		r = Request.get('user/')
	}
	
	return {
		profile : userProfile
	}
});