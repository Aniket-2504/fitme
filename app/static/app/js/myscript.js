$('.remove-cart').click(function() {
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})