selectedStudent_storage = JSON.parse(localStorage.getItem('selected'));
phoneNumber=selectedStudent_storage.map((record)=>record.student_id)
console.log(3,selectedStudent_storage)
let gridApi;

let columnDefs=[

    {
        headerName : 'student_phone_number',
        field : ''

    },

    {
        headerName : 'messageTime',
        field : ''

    },

    {
        headerName : 'status',
        field : ''

    },

];
const gridOptions={
    columnDefs: columnDefs,
    rowData: null,
    onGridReady : function(){
        gridApi.setGridOption("rowData",null);
    }

}
gridApi = agGrid.createGrid(document.querySelector('#student-grid'), gridOptions);