$(function () {
    $(".skill-prog span").each(function(){

        $(this).animate({
             'width': $(this).data("width")   
        },1000)
    })
})