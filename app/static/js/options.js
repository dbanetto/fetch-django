ValuesDict = {};
function change_trigger(listen_id, base_url, id_inputs, id_json) {
	$(listen_id).change(function() {
		var id_base = $(listen_id)[0];
		if (id_base.value === "") {  save_options(id_inputs); $(id_inputs).empty(); return; }
		if (typeof base_url === "string") {
			$.ajax({
				method: 'GET',
				headers: {
					'Content-Type':'application/json'
				},
				dataType: 'json',
				url: base_url + $(listen_id)[0].value,
				success: function(data) {
					genOptions(data['options'], id_inputs, id_json);
				}
			})
		} else if (typeof base_url === "object") {
			genOptions(base_url[$(listen_id)[0].value], id_inputs, id_json);
		}
	});
}

function save_options(id_inputs) {
	var inputs = $(id_inputs + " input");
	for (var i = 0; i < inputs.length; i++) {
		if (ValuesDict[id_inputs] == undefined) {
			ValuesDict[id_inputs] = {};
		}
		ValuesDict[id_inputs][inputs[i].name] = inputs[i].value;
	}
}

function genJSON(id_inputs, id_json) {
	var inputs = $(id_inputs + ' input');
	var out = '{';
	for (var i =0; i < inputs.length; i++) {
		out += JSON.stringify(inputs[i].getAttribute('data_name')) + ": " + JSON.stringify(inputs[i].value);
		if (i != inputs.length - 1) {
			out += ',';
		}
	}
	out += '}';
	$(id_json).val(out);
}

function genOptions(data, id_inputs, id_json) {
	save_options(id_inputs);

	var obj = $(id_inputs);

	var options = data;
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
		.attr('value', value) // apply saved values
		.change(function () {genJSON(id_inputs, id_json);});
		obj.append($('<div>').attr('class', 'form-group').append(label).append(input));
	}
}

