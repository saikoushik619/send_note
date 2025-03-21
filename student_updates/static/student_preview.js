selectedStudent_storage = JSON.parse(localStorage.getItem('selected'));


count = localStorage.getItem('studentCount');
console.log(count);

pName = localStorage.getItem('programName');
console.log(pName);

programName = document.getElementById('Program_name');
programName.innerText =  pName;


studentCount = document.getElementById('selected');
studentCount.innerText = studentCount.innerText + count;
idArray=new Array();
selectedIds=selectedStudent_storage.map((record)=>idArray.push(record.student_id));
console.log(4,idArray);


// Save the inforMATION OF PROGRAM

$('#saveButton').click(function() {
	let formData = new FormData();
	program_message = $('#textarea').val();
	program_document = $('#document').prop("files")[0];


    if(selectedIds.length>0){

            formData.append('program_name', pName);
            formData.append('student_count', count);
            formData.append('program_message', program_message);

            formData.append('selectedIds',idArray)


            formData.append('program_document', program_document);

	}else{
	    console.log('selectedIds length should be greater than zero please select students')
	};

	let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;


	$.ajax({
		type: 'POST',
		url: '/student/selected_rows/',
		data: formData,
		processData: false,
		contentType: false,
		headers: {
			'X-CSRFToken': csrf_token
		},
		success: function(response) {

			alert(' POSTED RESPONSE SUCCESSFULLY');
			console.log(response);


		},
		error: function(error) {
			console.log(error);
		}
	})



})