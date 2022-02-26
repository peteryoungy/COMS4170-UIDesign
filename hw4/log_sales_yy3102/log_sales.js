
let sales = [
	{
		"salesperson": "James D. Halpert",
		"client": "Shake Shack",
		"reams": 100
	},
	{
		"salesperson": "Stanley Hudson",
		"client": "Toast",
		"reams": 400
	},
	{
		"salesperson": "Michael G. Scott",
		"client": "Computer Science Department",
		"reams": 1000
	},
]

let clientWarning = false
let reamsWarning = false
let numberWarning = false

const myName = "Yang Yu"

clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
]



function makeEntries(){

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
        btn.attr('data-index', index)
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

        // todo: didn't use form ?
        


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

        // update model
        let newSale = {}
        newSale.salesperson = myName
        newSale.client = data[0].value
        newSale.reams = data[1].value
        console.log(newSale)

        sales.unshift(newSale)

        // update autocomplete
        if(!clients.includes(newSale.client)){
            clients.push(newSale.client)
        }

        // update view
        make()

        // clean input box
        $(".input").val("")
        $("#input-client").focus();
        $("#input-client").get(0).setSelectionRange(0, 0);
    })


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
    makeEntries()

    $(".btn-delete").click(function(e){
        console.log('delete info')

        let index = $(this).attr("data-index")
        // console.log(index)
        
        // console.log(e)
        
        // update model
        sales.splice(index, 1)

        // update view
        make()
        cleanErrorBox()
    })

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
}


$(document).ready(function(){

    reg()

    make()

    console.log('finished')
})
