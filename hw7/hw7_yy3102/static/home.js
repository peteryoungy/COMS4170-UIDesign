

popular_items = [

    "1", "2","3"
]


function displayBooks(){

    console.log("display books")
    $.each(popular_items, function(index, value){

        // 
        let item = $("<div class=col-md-3>")
        item.addClass("item")
        let imga = $("<a>")
        imga.attr("href", "/view/" + value)
        let img = $("<img>")
        let title = $("<a>")
        title.attr("href", "/view/" + value)
        // let author = $("<a>")

        // let item = $("<a>")
        // item.attr("href", "/view/" + value)
        
        let data_to_send = {"id": value}

        $.ajax({
            type: "POST",
            url: "get_item",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_send),
            success: function(result){
                // item.text(result["item"])
                img.attr("src", result["item"]["volumeInfo"]["imageLinks"]["thumbnail"])
                img.attr("alt", "book-cover")
                title.text(result["item"]["volumeInfo"]["title"])
                // author.text(result["item"]["volumeInfo"])

            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });

        // compose
        imga.append(img)
        item.append(imga)
        item.append(title)

        $("#item-container").append(item)

    })

}


$(document).ready(function(){

    displayBooks()

})