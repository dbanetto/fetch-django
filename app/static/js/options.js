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

function genOptions(data, id_inputs, id_json) {
	save_options(id_inputs);

	var obj = $(id_inputs);

	var options = data['properties'];
	obj.empty();
	var vals = ValuesDict[id_inputs];
	console.log(vals);
	console.log(ValuesDict);

	// Make form
	obj.jsonForm({
		schema: options,
		params: {
			fieldHtmlClass: "form-control"
		},
		value: vals,
		"displayErrors": function (errors, formElt) {
		// FIXME: Try to display errors
		for (var i=0; i<errors.length; i++) {
			errors[i].message = "Avast! Ye best be fixin' that field!";
		}
			$(formElt).jsonFormErrors(errors, formObject);
		}
	});
  $(id_inputs + " .form-actions").remove();

	// Add change event to genJSON
	var inputs = $(id_inputs + ' input');
	inputs.change(function () {
		var values = obj.jsonFormValue();
		var errors = obj.jsonFormErrors(); // FIXME: try to display errors
		$(id_json).val(JSON.stringify(values));
	});
}
