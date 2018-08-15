$('.dataDesc').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-paper-plane').addClass("next");
    } else {
      $('.icon-paper-plane').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.dataDesc').click(
  function(){
    console.log("Something");
    $('.dataDesc-section').addClass("fold-up");
    $('.attribute-section').removeClass("folded");
  }
);

$('.attribute').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-lock').addClass("next");
    } else {
      $('.icon-lock').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.attribute').click(
  function(){
    console.log("Something");
    $('.attribute-section').addClass("fold-up");
    $('.dependentVariable-section').removeClass("folded");
  }
);

$('.dependentVariable').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-repeat-lock').addClass("next");
    } else {
      $('.icon-repeat-lock').removeClass("next");
    }
  }
);

$('.next-button.dependentVariable').click(
  function(){
    console.log("Something");
    $('.dependentVariable-section').addClass("fold-up");
	var dependentVariable=$("#dependentVariable").val();
	var dataDesc=$("#dataDesc").val();
	var attribute=$("#attribute").val();
	var result="The data is about " + dataDesc +" and the important attribute is "+ attribute + " with dependency on "+dependentVariable;
	alert(result);	
    $('.success').css("marginTop", 0);
  }
);