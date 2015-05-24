/// <reference path="../../../../../typings/node/node.d.ts"/>

var app = require('app');  // Módulo para controlar la app.
var ipc = require('ipc');  // Un intercomunicador del proceso principal (app.js) con el renderer
var dialog = require('dialog'); // Mostrar diálogos del Sistema.
var BrowserWindow = require('browser-window'); // Módulo para crear ventanas

var fs = require('fs'); // Módulo de Node para el filesystem 
var path = require('path') // Módulo de Node para paths

var BASE_DIR = __dirname;
var APP_DIR = 'file://' + BASE_DIR; // Ruta base de la app.
var STATIC_DIR = APP_DIR + '/static/'; // Ruta base de archivos estáticos.
var DISK_DIR = path.join(BASE_DIR,'disk.json'); // Archivo para persistencia.

var Cache = (function(){ // Caché para almacenar datos compartidos entre ventanas de la app.
	var data = {};
	return {
		save:  function(key, value){ data[key] = value; }, /// FIXME: Si existe, sobreescribe.
		get: function(key){ return data[key]; }
	};
})();


var validJSON = function(text){
	var valid = false;
	if (/^[\],:{}\s]*$/.test(text.replace(/\\["\\\/bfnrtu]/g, '@').
			replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']').
			replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {
		valid = true;
	}
	return valid;
};

var Disk = (function(){ // Método para almacenar datos en el disco.
	var load = function(key, callback){
		fs.readFile(DISK_DIR, function(error, data){
			if (error){
				/// FIXME: Manejar error de lectura con Diálogos;
				console.error(error);
			}
			var response = data.toString('utf-8');
			if(!validJSON(response) && response){
				console.log('INVALID JSON!');
				return callback('');
			}

			response = JSON.parse(response);
			if (!key){
				return callback(response);
			}
			if (key in response) {
				console.log(response);
				return callback(response[key]);
			} else {
				return callback('');
			}
			
		});
	};
	var save = function(key, value, callback){
		load(null, function(file){
			console.log(file);
			file[key] = value;
			console.log(file);			
			fs.writeFile(DISK_DIR, JSON.stringify(file), 'utf-8', function(error){
				if (error){
					/// FIXME: Manejor error de escritura con Diálogos.
					console.error(error);
				}
				console.log('Saved', key, 'on:', DISK_DIR);
				return callback();
			});
		});
		
	};
	
	var erase = function(key){
		load(null, function(file){
			if (key in file){
				delete file[key];
			} else {
				file = {};
			}			
			fs.writeFileSync(DISK_DIR, JSON.stringify(file), 'utf-8', function(error){
				if (error){
					/// FIXME: Manejor error de escritura con Diálogos.
					console.error(error);
				}
				console.log('Erased', key, 'on:', DISK_DIR);
			});
		});
	};
	
	return {
		save : save,
		load : load,
		erase : erase
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
	
	var w_login_options = {// Opciones para la ventana de login.
		width: 515,        // Ancho
		height: 365,       // Alto
		frame: false,      // Ventana sin borde
		show: false,       // No mostrar ventana al crear.
		resizable: false,  // No se podrá cambiar el tamaño.
		icon:APP_ICON_PATH // Ícono de la ventana.
	};
	// Crear una ventana de navegador con las opciones w_login_options
	mainWindow = new BrowserWindow(w_login_options);
	mainWindow.loadUrl(STATIC_DIR + 'login.html'); // Carga login.html en la ventana.
	function show(mw){
		mw.webContents.on('did-finish-load', function() { 
			mw.show(); // Mostrar la ventana sólamente cuando se haya cargado login.html
			console.log("Mostrando ventana");
		});
	};
	show(mainWindow);

	
	mainWindow.on('closed', function() {
		mainWindow = null; // Al cerrar la ventana, vacía la referencia.
	});
	
	ipc.on('window-evt', function(event, action) { // Intercomunicador 
		mainWindow[action](); // Al cerrar, maximizar o minimzar.
	});
	
	ipc.on('login', function(event, authorized) { // Intercomunicador
		if (authorized){ // Al iniciar sesión, si está autorizado
			Cache.save('access_token', authorized); // Guardar accessToken en caché
			mainWindow.close(); // Cerrar la ventana
			
			var delta = Number.parseInt(SCREEN_SIZE.height*0.2);
			var rec_s = {
				width : SCREEN_SIZE.width - delta,
				height : SCREEN_SIZE.height - delta,
				icon: APP_ICON_PATH,
				show: false
			};
			
			rec_s.title = 'citaSalud - Administración';
			rec_s.fullscreen = false;
			mainWindow = new BrowserWindow(rec_s);
			mainWindow.loadUrl("http://dev:8000/api");
			show(mainWindow);		
			
		} else {
			// Código para manejar cuando las credenciales son incorrectas.
			/// OJO: Ya existe manejo de error en la ventana interna.
			// dialog.showErrorBox('Título', 'Mensaje de error');
		}
	});
	
	ipc.on('disk-save', function(event, key, data){
		Disk.save(key, data, function(){
			// Datos grabados
		});
	});
	
	ipc.on('disk-load', function(event, key){
		Disk.load(key, function(data){
			event.returnValue = data;
		});
	});
	
	ipc.on('disk-erase', function(event, key){
		Disk.erase(key);
	});
	
	
});
