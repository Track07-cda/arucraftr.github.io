(function($){
  $(function(){

    $('#load_page').css("display","none")
    $('body').css("overflow","auto")

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
  $('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: false, // Does not change width of dropdown to that of the activator
      hover: false, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: false, // Displays dropdown below the button
      alignment: 'left', // Displays dropdown with edge aligned to the left of button
      stoppropagation : true
    }
  );
  $('.collapsible').collapsible();
  $('.tooltipped').tooltip({delay: 100});
  $(this).scroll(function(){
    var scroll_pos = $(this).scrollTop()
    if(scroll_pos > 50){
      $('.navbar-bg').css("opacity","1")
    }else{
      $('.navbar-bg').css("opacity","0")
    }
    })
})(jQuery); // end of jQuery name space

window.onpagehide=function(){initialize()}
window.onbeforeunload=function(){initialize()};

function initialize(){
  $('#load_page').css("display","inline")
  $('body').css("overflow","hidden")
  $('body').removeClass('bg-image')
}