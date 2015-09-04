function force(url, from) {
  var from = $(from);
  if (from.attr('disabled') != undefined) {
    return;
  }
  from.attr('disabled', 'disabled');

  var backup_inner = from.html();
  $.ajax({
      type: "POST",
      contentType: "application/json",
      url: url,
      beforeSend: function() {
        from.html("<img src=\"/static/img/activity.gif\"/>");
      },
      complete: function() {
        from.html(backup_inner);
        from.removeAttr('disabled');
      }
  });
}
