$(window).on('resize', function() {
  $('.poster-full').css('max-height', $(this).height() - $('.navbar').height() - 10);
});
$(window).resize();

$('#series-plus').on('click', function() {
  console.log("clicked");
  var plus1 = parseInt($('#series-current').text()) + 1;
  console.log(plus1);

  $.ajax('count/', {
    contentType: 'application/json',
    dataType: 'json',
    method: 'POST',
    data: JSON.stringify({
      current_count: plus1
    }),
    success: function(data) {
      console.log(data);
      if (data['success']) {
        $('#series-current').text(data.current_count);
      }
    }
  });
});
