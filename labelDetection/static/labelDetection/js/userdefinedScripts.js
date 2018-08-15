$(document).ready(function(){
	
	$("#card1").hide();
	
    $("#imageUpload").on("click",function(){
		$("#card1").show();
		$.ajax({
			url : 'detectLabels/',
			method: 'POST',
			success: function(data){
				$("#placeholder").html(data);
			}
		});
    });
});

