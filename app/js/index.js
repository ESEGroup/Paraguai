/* ---------------------------- */
/* SCRIPT DO TEMPLATE PRINCIPAL */
/* ---------------------------- */
$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
     isClosed = false;

    trigger.click(function () {
      hamburger_cross();      
    });

    function hamburger_cross() {

      if (isClosed == true) {          
        overlay.hide();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        isClosed = false;
      } else {   
        overlay.show();
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }
  }
  
  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });  
});
/*--------------------------------------------------------*/
/*          SCRIPT COPIADO DO DATE PICKER                 */
/*--------------------------------------------------------*/
/* TODO - COLOCAR PARA FUNCIONAR
    https://eonasdan.github.io/bootstrap-datetimepicker/  */
    
/*----------------------------------------------------------------------------------------------------*/
/*          SCRIPT COPIADO DE                                                                         */
/* http://stackoverflow.com/questions/17147821/how-to-make-a-whole-row-in-a-table-clickable-as-a-link */
/*----------------------------------------------------------------------------------------------------*/
jQuery(document).ready(function($) {
    $(".clickable-row tr").click(function() {
        window.location = $(this).data("url");
    });
});