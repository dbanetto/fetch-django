ValuesDict = {};

function genJSON(id_json, id_div_inputs) {
	var inputs = $('#' + id_div_inputs + ' input');
	var out = '{';
	for (var i =0; i < inputs.length; i++) {
		out += "\"" + inputs[i].getAttribute('data_name') + "\": \"" + inputs[i].value + "\"";
		if (i != inputs.length - 1) {
			out += ',';
		}
	}
	out += '}';
	$('#' + id_json).val(out);
}

function genOptions(data, id, id_json) {
	obj = $("#" + id);

	// Save settings into dict
	inputs = $("#" + id + " input");
	for (var i = 0; i < inputs.length; i++) {
		ValuesDict[inputs[i].name] = inputs[i].value;
	}

	obj.empty();
	options = data['options'];
	if (options.length > 0) {
		obj.append($('<h3>').text('Additional options for ' + data['name']));
	}

	for (var i = 0; i < options.length; i++) {
		input_id = id + '_' + options[i];
		label = $('<label>').text(options[i]).attr('class', 'form-label').attr('for', input_id);
		input = $('<input>').attr('class', 'form-control')
												.attr('name', input_id)
												.attr('data_name', options[i])
												.attr('required', 'required')
												.attr('placeholder', options[i])
												.attr('value', ValuesDict[input_id]) // apply saved values
												.change(function () {genJSON(id_json, id);});
		obj.append($('<div>').attr('class', 'form-group').append(label).append(input));
	}
}

