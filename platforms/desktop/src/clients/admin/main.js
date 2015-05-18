/// <reference path="../../../../../typings/node/node.d.ts"/>

var app = require('app');  // Módulo para controlar la app.
var ipc = require('ipc');  // Un intercomunicador del proceso principal (app.js) con el renderer
// var dialog = require('dialog'); // Mostrar diálogos del Sistema.
var BrowserWindow = require('browser-window'); // Módulo para crear ventanas

var APP_DIR = 'file://' + __dirname; // Ruta base de la app.
var STATIC_DIR = APP_DIR + '/static/'; // Ruta base de archivos estáticos.

var Cache = (function(){ // Caché para almacenar datos compartidos entre ventanas de la app.
	var data = {};
	return {
		save:  function(key, value){ data[key] = value; }, /// FIXME: Si existe, sobreescribe.
		get: function(key){ return data[key]; }
	};
})();

// Un proxy de los errores a Electron
require('crash-reporter').start();

// Referencia global al objeto Window, para evitar que la aplicación
// sea cerrada por el GarbageCollection de Javascript.
var mainWindow = null;

// Cerrar la aplicación cuando todas las ventanas estén cerradas
app.on('window-all-closed', function() {
	if (process.platform != 'darwin'){
		app.quit();
	}
});

// Éste método se llamará cuando Electron acabe su incialización
// y esté listo para crear ventanas.
app.on('ready', function() {
	
	var SCREEN = require('screen');
	var APP_ICON_PATH = '/home/rc/webapps/citasalud/platforms/desktop/src/clients/admin/static/assets/img/icon.png';
	var SCREEN_SIZE = SCREEN.getPrimaryDisplay().workAreaSize;
	
	var w_login_options = { // Opciones para la ventana de login.
		width: 515,        // Ancho
		height: 365,       // Alto
		frame: false,      // Ventana sin borde
		show: false,       // No mostrar ventana al crear.
		resizable: false,  // No se podrá cambiar el tamaño.
		icon:APP_ICON_PATH // Ícono de la ventana.
	}
	// Crear una ventana de navegador con las opciones w_login_options
	mainWindow = new BrowserWindow(w_login_options);
	mainWindow.loadUrl(STATIC_DIR + 'login.html'); // Carga login.html en la ventana.
	mainWindow.webContents.on('did-finish-load', function() { 
		mainWindow.show(); // Mostrar la ventana sólamente cuando se haya cargado login.html
	});
	
	mainWindow.on('closed', function() {
		mainWindow = null; // Al cerrar la ventana, vacía la referencia.
	});
	
	ipc.on('window-evt', function(event, action) { // Intercomunicador 
		mainWindow[action](); // Al cerrar, maximizar o minimzar.
	});
	
	ipc.on('login', function(event, authorized) { // Intercomunicador
		if (authorized){ // Al iniciar sesión, si está autorizado
			Cache.save('access_token', authorized);
			mainWindow.close();
			var delta = Number.parseInt(SCREEN_SIZE.height*0.2);
			
			var rec_s = {
				width : SCREEN_SIZE.width - delta,
				height : SCREEN_SIZE.height - delta
			}
//			rec_s.width = 1600;
//			rec_s.height = 900;
			rec_s.title = 'citaSalud - Administración';
			rec_s.fullscreen = false;
			console.log(SCREEN_SIZE);
			console.log(rec_s);
			mainWindow = new BrowserWindow(rec_s);		
			
		} else {
			// Código para manejar cuando las credenciales son incorrectas.
			/// OJO: Ya existe manejo de error en la ventana interna.
			dialog.showErrorBox('xD', 'WHYYYYY');
		}
	});
		
});
