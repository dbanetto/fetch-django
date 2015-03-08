ValuesDict = {};

var genOptions = function(data, id) {
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
												.attr('required', 'required')
												.attr('placeholder', options[i])
												.attr('value', ValuesDict[input_id]); // apply saved values
		obj.append($('<div>').attr('class', 'form-group').append(label).append(input));
	}
}
