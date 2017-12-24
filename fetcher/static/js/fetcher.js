function force(url, from) {
  var from = $(from);
  if (from.attr('disabled') !== undefined) {
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

function refreashLog(url) {
  var from = $('#log-refreash');
  if (from.attr('disabled') !== undefined) {
    return;
  }
  from.attr('disabled', 'disabled');

  var backup_inner = from.html();
  $.ajax({
    type: "GET",
    contentType: "application/json",
    url: url,
    beforeSend: function() {
      from.html("<img src=\"/static/img/activity.gif\"/>");
    },
    success:  function(data) {
      var log = $('#log-box');
      log.text(data.log.reverse().join('\n'));
    },
    complete: function() {
      from.html(backup_inner);
      from.removeAttr('disabled');
    }
  });
}

function status(url) {
  var refreahBtn = $('#fetcherd-refreash');
  refreahBtn.prop("disabled", true);

  $.ajax({
    contentType: "application/json",
    url: url,
    success: function(data) {
      if (data.running) {
        $('#fetcherd-status').text("Is running");
        if (data.fetch_lock) {
          $('#force-fetch').prop("disabled", true);
        } else {
          $('#force-fetch').prop("disabled", false);
        }
        if (data.sort_lock) {
          $('#force-sort').prop("disabled", true);
        } else {
          $('#force-sort').prop("disabled", false);
        }
        $('#log-refreash').prop("disabled", false);
      } else {
        $('#fetcherd-status').text("Is down");
        $('#force-fetch').prop("disabled", true);
        $('#force-sort').prop("disabled", true);
        $('#log-refreash').prop("disabled", true);
      }
    },
    complete: function() {
      refreahBtn.prop("disabled", false);
    }
  });
}
