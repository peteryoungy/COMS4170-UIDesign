let names = ["Phyllis", "Angela"]
let ppcList = []

function makeNames(names){

    $("#name-box-left").empty()
    $.each(names, function(index, value){
        let nameDiv = $("<div>")
        $(nameDiv).text(value)
        // $(nameDiv).html("<div>" + value + "</div>")

        $(nameDiv).addClass("default-name-style")
        $(nameDiv).attr("data-name", value)

        // reg hover event
        $(nameDiv).hover(
            function(){
                $(this).addClass("name-hover-over")
            },
            function(){
                $(this).removeClass("name-hover-over")
            }
        )
        
        // reg draggable
        $(nameDiv).draggable({
            revert: "invalid",
            // drag must hover over?
            // classes:{
            //     "ui-draggable-dragging": "name-hover-over"
            // },
            zIndex: 100
        })

        $("#name-box-left").append(nameDiv)
    })
}

function makeDroppable(){
    $(".drop-target").droppable({
        // accept: $("#name-box-left > div"),
        drop: function(event, ui){

            ui.draggable.css("left", 0)
            ui.draggable.css("top", 0)

            // console.log(ui.draggable.text())
            console.log(ui.draggable.attr("data-name"))
            // console.log(ui.draggable.data("name"))

            ppcList.push(ui.draggable.text())
            console.log(ppcList)

            $("#name-box-right").append(ui.draggable)
        }
    })
}

$(document).ready(function(){

    makeNames(names)
    makeDroppable()
})