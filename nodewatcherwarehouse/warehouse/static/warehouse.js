function set_drop_down(id, divs){
    $(id).change(function(){
        var current_id = id+ "_" + $(this).val();
        var all_divs = "div[id^='" + id.replace("#", "") + "_']";
        $(all_divs).not(current_id).hide();
        $(all_divs).not(current_id).find(":input").val("");
        $(current_id).show();
    });
}

function show_delete_warning(delete_url){
    $( "#delete-confirm" ).dialog({
            resizable: false,
            height:150,
            modal: true,
            buttons: {
                "Delete": function() {
                    $.get(delete_url, function(data) {
                        document.location.reload();
                    });
                },
                Cancel: function() {
                    $(this).dialog("close");
                }
            }
        });
}
