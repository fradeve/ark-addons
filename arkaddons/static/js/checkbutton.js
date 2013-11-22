/**
 * Created by fradeve on 22/11/13.
 */

$(document).ready(function(){
    $('.projectbutton').click(function(e){
        var selectedbutton = $(this)
        var projectcode = $(this).attr('projectcode')
        $.post(
            '../statuscheck/',
            {slug: projectcode}
        ).done(function(data){
                if (data == 'active'){
                    selectedbutton.html('API reachable')
                    selectedbutton.addClass('btn-success', 200)
                }else{
                    selectedbutton.addClass('btn-danger', 200)
                }
            });
    })
})
