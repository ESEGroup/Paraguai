$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
      isOpen = false;

  trigger.click(function () {
    isOpen = !isOpen;

    $('#wrapper').toggleClass('toggled', isOpen);
    trigger.toggleClass('is-open', isOpen);
    trigger.toggleClass('is-closed', !isOpen);
    overlay.toggle(isOpen);
  })

  $('.datepicker').datetimepicker();
  $('select').select2();
  $('.clickable-row').click(function(){
    window.location = $(this).data('href');
  })
});
