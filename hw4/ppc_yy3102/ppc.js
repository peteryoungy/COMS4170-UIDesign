
let employees = [
    "Phyllis",
    "Angela",
    "Dwight",
    "Oscar",
    "Creed",
    "Pam",
    "Jim",
    "Stanley",
    "Michael",
    "Kevin",
    "Kelly"
    ]

let ppcList = []

let names = [employees, ppcList]

let targetListMapping = {
    ".drop-target-right": 1,
    ".drop-target-left": 0
}


function makeNames(selector, names){

    $(selector).empty()
    $.each(names, function(index, value){
        let nameDiv = $("<div>")
        $(nameDiv).text(String(index)+ ": " + value)
        // $(nameDiv).html("<div>" + value + "</div>")

        $(nameDiv).addClass("default-name-style")
        $(nameDiv).attr("data-name", value)

        // func: reg hover event
        $(nameDiv).hover(
            function(){
                $(this).addClass("name-hover-over")
            },
            function(){
                $(this).removeClass("name-hover-over")
            }
        )
        
        // func: reg draggable
        $(nameDiv).draggable({
            revert: "invalid",
            // drag must hover over?
            // classes:{
            //     "ui-draggable-dragging": "name-hover-over"
            // },   
            zIndex: 100
        })

        $(selector).append(nameDiv)
    })
}

function makeDroppable(source, target){

    $(target).droppable({
        accept: source,
        drop: function(event, ui){
            
            // TODO: ui.draggable[0]


            // func: remove backgroud color
            $(this).removeClass("start-dragging")
            $(this).removeClass("drop-over")
            
            ui.draggable.css("left", 0)
            ui.draggable.css("top", 0)

            person = ui.draggable.attr("data-name")
            // console.log(ui.draggable.text())
            console.log(person)
            // console.log(ui.draggable.data("name"))

            // func: update model
            // ppcList.push(person)
            // employees = employees.filter(function(e) { return e !== person})

            pushIndex = targetListMapping[target]
            console.log(pushIndex)

            names[pushIndex].push(person)
            names[pushIndex ^ 1] = names[pushIndex ^ 1].filter(function(e) { return e !== person})

            // func: update view
            makeNames("#name-box-left", names[0])
            makeNames('#name-box-right', names[1])
            console.log(2)
        },

        activate: function(event, ui){
            console.log("activate")
            $(this).addClass("start-dragging")
        },

        deactivate: function(event, ui){
            console.log("deactivate")
            $(this).removeClass("start-dragging")
            // $(this).removeClass('drop-over')
        },

        over: function(event, ui){
            console.log("over")
            $(this).addClass('drop-over')
        },

        out: function(event, ui){
            console.log("out")
            $(this).removeClass('drop-over')
        }
    })
}

$(document).ready(function(){

    makeNames("#name-box-left",names[0])
    makeNames('#name-box-right', names[1])
    makeDroppable("#name-box-left > div", ".drop-target-right")
    makeDroppable("#name-box-right > div", ".drop-target-left")
})