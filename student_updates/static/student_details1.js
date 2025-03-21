let gridApi;

function installGrid() {

    let columnDefs = [{

            headerName: 'StudentName',
            field: 'student_name'
        },
        {
            headerName: 'Location',
            field: 'student_location__region'
        },
        {
            headerName: 'phone number',
            field: 'masked_number'
        }
    ];
    const gridOptions = {
        columnDefs: columnDefs,
        rowData: null,
        pagination: true,
        paginationPageSize: 10,

        paginationPageSizeSelector: [10,100,20],
        domLayout: 'autoHeight',
        defaultColDef: {
            editable: true,
            filter: true,
            flex: 1,
            minWidth: 100
        },
        rowSelection: {
            mode: "multiRow",
            groupSelects: 'descendants'
        },
        onGridReady : function(){
            gridApi.setGridOption("rowData",null);
        }



    };
    gridApi = agGrid.createGrid(document.querySelector('#student-grid'), gridOptions);

}

function loadStudentData() {
    $.ajax({

        type: 'GET',
        url: '/student/student_details/',
        success: function(response) {
            console.log(response)
            pageSize = response.page_Size;
            gridApi.setGridOption("pageSize", pageSize);
            gridApi.setGridOption("rowData", response.student_data);

        },
        error: function(error) {
            console.log(error)
        }
    })
}
function loadLocations() {
    dropDownButton = $('#locationDropdown')
    $.ajax({

        type: 'GET',
        url: '/student/locations/',
        success: function(response) {

            optionsHtml = response.available_locations.map((record) => {
                option = document.createElement('option')
                option.textContent = record.name
                return option
            })

            dropDownButton.append(optionsHtml)


        },
        error: function(error) {
            console.log(error);
        }
    })


}



$(document).ready(function() {
    localStorage.clear();
    installGrid();
    loadLocations();
});
loadStudentData()


$('#selectButton').click(function() {
    region = $('#locationDropdown').val();
    $.ajax({
        type: 'GET',
        url: '/student/singleregion/' + region + '/',
        data: {
            'name': region
        },
        success: function(response) {
            console.log(response);
            let pageSize = response.page_size

            gridOptions = {
                paginationPageSize: pageSize,
                rowData: null,


                domLayout: 'autoHeight',
                defaultColDef: {
                    editable: true,
                    filter: true,
                    flex: 1,
                    minWidth: 100,
                },
                rowSelection: {
                    mode: "multiRow",
                    groupSelects: "descendants",
                },
            };


            //gridApi = agGrid.createGrid(document.querySelector('#student-grid'), gridOptions);
            gridApi.setGridOption("rowData", response.student_data);
        },
        error: function(error) {
            console.log(error);
        }
    })
})
let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;


$('#nextPage').click(function() {
    selRows = gridApi.getSelectedRows()
    console.log(144,selRows)
    programName = document.getElementById('program').value
    studentCount = selRows.length
    localStorage.setItem('studentCount', JSON.stringify(studentCount))
    localStorage.setItem('programName', JSON.stringify(programName))

    let selectedStudent_rows = selRows.map((record) => {

        return {
            'student_id':record.id,

        }


    })

    localStorage.setItem('selected', JSON.stringify(selectedStudent_rows));
    selectedStudent_storage = localStorage.getItem('selected');
    //console.log(166,selectedStudent_storage)



    // returning html of next page

    $.ajax({
        type: 'GET',
        url: '/student/selected_students/',
        success: function() {
            console.log('page retrived')
        },
        error: function(error) {
            console.log('error')
        }
    })


});




//dropDownButton=document.getElementById('locationDropdown')
//$.ajax({
//
//    type:'GET',
//    url:'/student/locations/',
//    success : function(response){
//
//        response.available_locations.forEach((record)=>{
//            option=document.createElement('option')
//            option.textContent=record.name
//            dropDownButton.append(option)
//
//
//
//        })
//    } ,
//    error : function(error){
//        console.log(error);
//    }
//})

//region=document.getElementById('locationDropdown').value;
//
//
//
//let gridApi;
//let pageSize
//// DISPLAYING ALL AVAILABLE DATA
//$.ajax({
//    type:'GET',
//    url:'/student/singleregion/'+region+'/',
//    data:{
//        'region':region
//    },
//    success : function(response){
////        console.log(20,response);
//        pageSize = response.page_size
//        let rowData=response.student_data;
//        let columnDefs=[
//            {
//                headerName: "StudentName",
//                field: 'student_name'
//
//            },
//            {
//                headerName: "Location",
//                field :'student_location'
//
//            },
//            {
//                headerName : 'Phone Number',
//                field: "student_phone_number"
//
//            }
//        ];
//        const gridOptions = {
//        columnDefs: columnDefs,
//        rowData: rowData,
//        pagination: true,
//        paginationPageSize: pageSize,
//        paginationPageSizeSelector: [10, 20,100],
//        domLayout: 'autoHeight',
//        defaultColDef: {
//            editable: true,
//            filter: true,
//            flex: 1,
//            minWidth: 100,
//        },
//        rowSelection: {
//            mode: "multiRow",
//            groupSelects: "descendants",
//        },
//       onGridReady: function(params) {
//       const gridApi = params.api;
//       const gridColumnApi = params.columnApi;
//
//           // Log gridApi to ensure it's properly initialized
//        loadStudentData();
//      }
//    };
//
//    // Initialize the grid immediately when the document is ready
//    gridApi = agGrid.createGrid(document.querySelector('#student-grid'), gridOptions);
//    gridApi.setGridOption("rowData",rowData);
//    gridApi.setGridOption("pageSize",pageSize);
//    },
//    error : function(error){
//        console.log(23,error)
//    }
//})

//$('#selectButton').click(function(){
//    region=document.getElementById('locationDropdown').value;
//    $.ajax({
//        type :'GET',
//        url:'/student/singleregion/'+region+'/',
//        data : {
//            'name':region
//        },
//        success : function(response){
//            console.log(response);
//            let pageSize = response.page_size
//            if (typeof gridApi !== 'undefined'){
//                gridApi.destroy()
//            }
//
//            let rowData=response.student_data;
//            let columnDefs=[
//                {
//                headerName: "StudentName",
//                field: 'student_name'
//
//            },
//            {
//                headerName: "Location",
//                field :'student_location'
//
//            },
//            {
//                headerName : 'Phone Number',
//                field: "student_phone_number"
//
//            }
//
//            ];
//            const gridOptions = {
//            columnDefs: columnDefs,
//            rowData: rowData,
//            pagination: true,
//            paginationPageSize: pageSize,
//            paginationPageSizeSelector: [10, 20,100],
//            domLayout: 'autoHeight',
//            defaultColDef: {
//            editable: true,
//            filter: true,
//            flex: 1,
//            minWidth: 100,
//        },
//        rowSelection: {
//            mode: "multiRow",
//            groupSelects: "descendants",
//        },
//        };
//
//
//        gridApi = agGrid.createGrid(document.querySelector('#student-grid'), gridOptions);
//        gridApi = agGrid.createGrid("rowData", gridOptions);
//        },
//        error : function(error){
//            console.log(error);
//        }
//    })
//    })
//let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
//
//
//$('#nextPage').click(function(){
//    selRows=gridApi.getSelectedRows()
//    programName=document.getElementById('program').value
//    studentCount=selRows.length
//    localStorage.setItem('studentCount', JSON.stringify(studentCount))
//    localStorage.setItem('programName', JSON.stringify(programName))
//
//    let selectedStudent_rows=selRows.map((record)=>{
//
//            return{
//            'student_id':record.student_id,
//            'student_name':record.student_name,
//            'student_location': record.student_location,
//            'student_phone_number': record.student_phone_number,
//            'student_count':studentCount
//            }
//
//
//    })
//    console.log(localStorage.getItem("student_name"))
//
//
//
//    localStorage.setItem('selected', JSON.stringify(selectedStudent_rows));
//    selectedStudent_storage=localStorage.getItem('selected');
//    console.log(178,selectedStudent_storage[0].student_id)
//
//
//
//    //let selectedStudent_details=JSON.parse({'s':selectedStudent_rows})
//    console.log(185,selectedStudent_storage)
//
//
//    // returning html
//
//    $.ajax({
//        type:'GET',
//        url:'/student/selected_students/',
//        success : function (){
//            console.log('page retrived')
//        },
//        error : function(error){
//            console.log('error')
//        }
//    })
//
//
//});