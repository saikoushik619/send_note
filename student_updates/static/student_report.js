$.ajax({
    type:'GET',
    url: '/student/student_report_send/',
    success : function (response){
            console.log(response)
            let gridApi;


			columnDefs = [

				{
					headerName: "ProgramName",
					field: 'program_name'
				},

				{
				    headerName : 'ProgramMessage',
				    field : 'program_message'
				},
				{
					headerName: "student_count",
					field: 'student_count'

				},



			];

			const gridOptions = {
				columnDefs: columnDefs,
				rowData: null,
				domLayout: 'autoHeight',
				onGridReady : function(){

				    gridApi.applyTransaction({add: response.data});
				}

			}


			gridApi = agGrid.createGrid(document.querySelector('#student-grid'), gridOptions);



    },

    error : function(error){
        console.log(error)
    }


})
