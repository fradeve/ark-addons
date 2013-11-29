/**
 * Created by fradeve on 22/11/13.
 */

$(document).ready(function(){
    Ladda.bind('.projectbutton-get-str');
    $('.projectbutton-get-str').click(
        function(e){
            activebutton = $(this);
            var l = Ladda.create(this);
            var apiurl = $(this).attr('apiurl');
            $.getJSON(apiurl, function(data){
                    visualize(data);
                    $("#apidatamodal").modal();
                    l.stop()
                },
                "json").fail(function(){
                    activebutton.html('GET failed');
                    activebutton.addClass('btn-danger')
                })
        }
    );
})
