ValuesDict = {};
function change_trigger(id, base_url, id_inputs, id_json) {
  $(id).change(function() {
    id_base = $(id)[0]
    if (id_base.value === "") {  save_options(id_inputs); $(id_inputs).empty(); return; }
    $.ajax({
      type: 'GET',
      url: base_url + $(id)[0].value + '.json',
      success: function(data) {
        genOptions(data, id_inputs, id_json);
      }
    })
  });
}

function save_options(id_inputs) {
	inputs = $(id_inputs + " input");
	for (var i = 0; i < inputs.length; i++) {
		if (ValuesDict[id_inputs] == undefined) {
			ValuesDict[id_inputs] = {};
		}
		ValuesDict[id_inputs][inputs[i].name] = inputs[i].value;
	}
}

function genJSON(id_inputs, id_json) {
	var inputs = $('#' + id_inputs + ' input');
	var out = '{';
	for (var i =0; i < inputs.length; i++) {
		console.log(inputs[i]);
		out += JSON.stringify(inputs[i].getAttribute('data_name')) + ": " + JSON.stringify(inputs[i].value);
		if (i != inputs.length - 1) {
			out += ',';
		}
	}
	out += '}';
	$('#' + id_json).val(out);
}

function genOptions(data, id_inputs, id_json) {
	save_options(id_inputs);

	var obj = $(id_inputs);
	var options = data['options'];
	obj.empty();

	for (var i = 0; i < options.length; i++) {
		var input_id = id_inputs.substr(1) + '_' + options[i];
		var value = "";
		if (ValuesDict[id_inputs] != undefined && ValuesDict[id_inputs][input_id] != undefined) {
			value = ValuesDict[id_inputs][input_id];
		}
		var label = $('<label>').text(options[i]).attr('class', 'form-label').attr('for', input_id);
		var input = $('<input>').attr('class', 'form-control')
												.attr('name', input_id)
												.attr('data_name', options[i])
												.attr('required', 'required')
												.attr('placeholder', options[i])
												.attr('value', value) // apply saved values
												.change(function () {genJSON(id, id_json);});
		obj.append($('<div>').attr('class', 'form-group').append(label).append(input));
	}
}

