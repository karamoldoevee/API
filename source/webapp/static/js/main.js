const indexLink = "https://http://127.0.0.1:8000/";

function renderData(data){
	Object.entries(data).forEach(function ([key, value]) {
		console.log(`${key}: ${value}`);


	});
};

function jqueryParseData(response, status) {
	console.log(response);
	console.log(status);
	renderData(response);
};

function jqueryAjaxError(response, status) {
	console.log(response);
	console.log(status);
	console.log('error');


};

function jqueryLoadIndex(){
	$.ajax({
		url: indexLink,
		method: 'GET',
		success: jqueryParseData,
		error: jqueryAjaxError
	});
};

$(document).ready(function() {
	jqueryLoadIndex();
});