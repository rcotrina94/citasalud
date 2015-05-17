var app = require('app');  // Module to control application life.
var ipc = require('ipc');

var BrowserWindow = require('browser-window');  // Module to create native browser window.
var APP_DIR = 'file://' + __dirname;
var STATIC_DIR = APP_DIR + '/static/';

// Report crashes to our server.
require('crash-reporter').start();

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the javascript object is GCed.
var mainWindow = null;

// Quit when all windows are closed.
app.on('window-all-closed', function() {
	if (process.platform != 'darwin'){
		app.quit();
	}
});

// This method will be called when Electron has done everything
// initialization and ready for creating browser windows.
app.on('ready', function() {
	// Create the browser window.
	mainWindow = new BrowserWindow({width: 640, height: 380, frame:false, show:false});
	
	// and load the index.html of the app.
	mainWindow.loadUrl(STATIC_DIR + 'login.html');
	
	mainWindow.webContents.on('did-finish-load', function() {
		mainWindow.show();
		mainWindow.webContents.send('ping', 'whoooooooh!');
	});
	
	mainWindow.openDevTools();
	
	// Emitted when the window is closed.
	mainWindow.on('closed', function() {
		// Dereference the window object, usually you would store windows
		// in an array if your app supports multi windows, this is the time
		// when you should delete the corresponding element.
		mainWindow = null;
	});
	
	ipc.on('window-evt', function(event, action) {
		mainWindow[action]();
	});
		
});
