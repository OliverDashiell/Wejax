$(function(){
	var timestamp = new Date();
	var protocol = document.location.protocol == "https:"? "wss://" : "ws://";
	var ws = new WebSocket(protocol + document.domain + ":" + document.location.port + "/websocket");

	function output(msg){
		$('#output').append(msg).append(" [" + (new Date()-timestamp) + "ms]").append("<br/>");
	}
	
	ws.onopen = function() {
		output("connected...");
	};

	ws.onmessage = function (evt) {
		output(evt.data);
	};
	
	$('#ajax_btn').click(function(){
		timestamp = new Date();
		
		$.get("/ajax", function(result){
			output(result);
		});
	});
	
	$('#ws_btn').click(function(){
		timestamp = new Date();
		
		ws.send("Hello, websocket");
	});
});