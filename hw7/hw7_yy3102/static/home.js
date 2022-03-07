

popular_items = [

    "1", "2","3"
]


function displayBooks(){

    console.log("display books")
    $.each(popular_items, function(index, value){


        let item = $("<a>")
        item.attr("href", "/view/" + value)
        
        let data_to_send = {"id": value}

        $.ajax({
            type: "POST",
            url: "get_title",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_send),
            success: function(result){
                item.text(result["title"])
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });


        $("#item-container").append(item)

    })

}


$(document).ready(function(){

    displayBooks()

})