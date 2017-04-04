
$(document).ready(function () {

  $('input.filter').on('keyup', function() {
  var rex = new RegExp($(this).val(), 'i');
  $('.searching').hide();
      $('.searching').filter(function() {
          return rex.test($(this).text());
      }).show();
  });
});
