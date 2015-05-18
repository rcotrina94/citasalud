app.factory('$storage', ['$window', function($window) {
  return {
    set: function(name, value) {
        messenger.send('disk-save', name, value);
    },
    get: function(name) {
        return messenger.sendSync('disk-load', name);
    },
    clear: function(key){
        return messenger.send('disk-erase', key)
    }
    
  };
}]);