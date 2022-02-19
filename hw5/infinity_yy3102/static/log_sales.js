clientWarning = false
reamsWarning = false
numberWarning = false

myName = "Yang Yu"

function display_sales_list(sales){

    // <div class = "row">
    //     <div class="col-md-8">
    //         <div class="row">
    //             <div class="col-md-3"></div>
    //             <div class="col-md-6"></div>
    //             <div class="col-md-3"></div>
    //         </div>
    //     </div>
    //     <div class="col-md-1">
    //         <button>

    //         </button>
    //     </div>
    // </div>

    $("#entry-box").empty()
    $.each(sales, function(index, value){

        console.log(value)


        let entry = $("<div>")
        entry.addClass("row")
        entry.addClass("entry-default")

        let textDiv = $("<div>")
        textDiv.addClass("col-md-8")
        // text.attr("action")
        let textSubDiv = $("<div>")
        textSubDiv.addClass("row")

        let salesperson = $("<div>")
        salesperson.addClass("col-md-3")
        salesperson.text(value.salesperson)
        salesperson.attr("name", "salesperson")

        let client = $("<div>")
        client.addClass("col-md-6")
        client.text(value.client)
        client.attr("name", "client")

        let reams = $("<div>")
        reams.addClass("col-md-3")
        reams.text(value.reams)
        reams.attr("name", "reams")

        let btnDiv = $("<div>")
        btnDiv.addClass("col-md-1")
        let btn = $("<button>")
        btn.addClass("btn btn-warning btn-sm btn-delete")
        btn.attr('data-index', value.id)
        btn.text('X')

        textSubDiv.append(salesperson)
        textSubDiv.append(client)
        textSubDiv.append(reams)

        textDiv.append(textSubDiv)
        btnDiv.append(btn)

        entry.append(textDiv)
        entry.append(btnDiv)

        $("#entry-box").append(entry)
    })
}

function regSubmitEvent(){

    $(".btn-submit").click(function(){

        console.log('click button')
        let data = $('.form-submit').serializeArray()

        // func: check data validity
        if(data[0].value === ""){
            console.log('client is empty')
            if(clientWarning === false){
                clientWarning = true
                let clientAlert = $("<div>")
                clientAlert.addClass("alert alert-danger alert-default")
                clientAlert.attr("role", "alert")
                clientAlert.text("Must enter Client!")

                $("#input-client-div").append(clientAlert)
            }
            // move cursor
            $("#input-client").focus();
            $("#input-client").get(0).setSelectionRange(0, 0);

        } else{
            if(clientWarning === true){
                clientWarning = false
                // $("#input-client-div").(clientAlert)
                $("#input-client-div > div").remove()
            }
        }
        
        
        if(data[1].value === ""){
            console.log('reams is empty')

            // this error has higher priority
            if(numberWarning === true){
                $("#input-reams-div > div").remove()
                numberWarning = false
            }

            if(reamsWarning === false){
                reamsWarning = true
                let reamsAlert = $("<div>")
                reamsAlert.addClass("alert alert-danger alert-default")
                reamsAlert.attr("role", "alert")
                reamsAlert.text("Must enter Reams!")

                $("#input-reams-div").append(reamsAlert)
            }
            // move cursor
            if(clientWarning === false){
                $("#input-reams").focus();
                $("#input-reams").get(0).setSelectionRange(0, 0);
            }
            return
        } else{
            if(reamsWarning === true){
                reamsWarning = false
                $("#input-reams-div > div").remove()
            }
        }

        if(clientWarning === true || reamsWarning === true){
            return
        }

        // func: check if reams is number
        if(isNaN(data[1].value)){
            
            if(numberWarning === false){
                numberWarning = true
                // warning display
                let reamsAlertNumber = $("<div>")
                reamsAlertNumber.addClass("alert alert-danger alert-default")
                reamsAlertNumber.attr("role", "alert")
                reamsAlertNumber.text("Reams must be a number!")

                $("#input-reams-div").append(reamsAlertNumber)
            }
            // cursor go back to reams field
            $("#input-reams").focus()
            let pos = $("#input-reams").val().length
            $("#input-reams").get(0).setSelectionRange(pos, pos)

            return
        } else {
            numberWarning = false
            $("#input-reams-div > div").remove()
        }
            
        // update model and view
        let new_sale = {}
        new_sale.salesperson = myName
        new_sale.client = data[0].value
        new_sale.reams = data[1].value
        console.log(new_sale)

        save_sale(new_sale)

        // clean input box
        $(".input").val("")
        $("#input-client").focus();
        $("#input-client").get(0).setSelectionRange(0, 0);
    })


}

function save_sale(new_sale){

    let data_to_save = {"new_sale": new_sale}         
    $.ajax({
        type: "POST",
        url: "save_sale",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            // func: handle sales
            let all_data_sales = result["sales"]
            sales = all_data_sales
            make()

            // func: handle clients
            let all_data_clients = result["clients"]
            clients = all_data_clients
            regAutocomplete()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


function regClientKeyUp(){

    $("#input-client").keyup(function(e) {

        if (e.keyCode === 13) {
            $("#input-reams").focus();
            pos = $("#input-reams").val().length
            $("#input-reams").get(0).setSelectionRange(pos, pos);
        }

    })

}

function regReamsKeyUp(){
    $("#input-reams").keyup(function(e) {

        if (e.keyCode === 13) {
            $(".btn-submit").click()
        }

    })
}

function regAutocomplete(){
    $("#input-client").autocomplete({
        source: clients
    })
}

function make(){
    display_sales_list(sales)

    $(".btn-delete").click(function(e){
        console.log('delete info')

        let id = $(this).attr("data-index")
        console.log(id)
          
        // update model and view
        delete_sale(id)


        cleanErrorBox()
    })

    console.log('make finished')
}

function delete_sale(id){

    console.log('delete id: ' + id)
    
    let data_to_delete = {"id": id}         
    $.ajax({
        type: "POST",
        url: "delete_sale",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_delete),
        success: function(result){
            // func: handle sales
            let all_data_sales = result["sales"]
            sales = all_data_sales
            make()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}


function cleanErrorBox(){

    if(clientWarning === true){
        $("#input-client-div > div").remove()
        clientWarning = false
    }

    if(reamsWarning === true){
        $("#input-reams-div > div").remove()
        reamsWarning = false
    }

    if(numberWarning === true){
        $("#input-reams-div > div").remove()
        numberWarning = false
    }
}

function reg(){

    regSubmitEvent()

    regClientKeyUp()

    regReamsKeyUp()

    regAutocomplete()

    console.log('reg finished')
}


// $(document).ready(function(){

//     console.log(sales)
//     console.log(clients)

//     reg()

//     make()

//     console.log('finished')
// })
