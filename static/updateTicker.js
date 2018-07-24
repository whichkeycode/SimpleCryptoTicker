$(function(){
	(function updateTicker(){
		/*
			Update the ticker with JSON retrieved from '/data'
		*/
		$.getJSON('/data', function(data) {
			$.each(data,function(i,val){
				$('#'+val['symbol']+'price').text(val['lastPrice'])
				$('#'+val['symbol']+'volume').text(val['quoteVolume'])
				$('#'+val['symbol']+'percent').text(val['priceChangePercent'])
			});
		});
		setTimeout(updateTicker,3000);
	})();
});