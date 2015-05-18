app.factory('$storage', ['$window', function($window) {
  return {
    set: function(key, value) {
        $window.localStorage[key] = value;
    },
    get: function(key, defaultValue) {
        return $window.localStorage[key] || defaultValue;
    },
    setObject: function(key, value) {
        $window.localStorage[key] = JSON.stringify(value);
    },
    getObject: function(key) {
        var obj = $window.localStorage[key]
        return obj?JSON.parse(obj || '{}'):false;
    },
    clear: function(){
        $window.localStorage.clear();
    }
  };
}]);