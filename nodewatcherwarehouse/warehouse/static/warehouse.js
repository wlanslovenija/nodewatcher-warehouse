function set_drop_down(id, divs){
    $(id).change(function(){
        var current_id = id+ "_" + $(this).val();
        var all_divs = "div[id^='" + id.replace("#", "") + "_']";
        $(all_divs).not(current_id).hide();
        $(all_divs).not(current_id).find(":input").val("");
        $(current_id).show();
    });
}

function show_message(msg){
    $("#messagebox").html(msg);
    $("#messagebox").dialog({
        resizable: false,
        height:150,
        modal: true,
        buttons: {
            Ok: function() {
                $(this).dialog("close");
            }
        }
    });
}

function show_delete_warning(delete_url){
    $("#dialog:ui-dialog").dialog("destroy");
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

function generate_labels(){
    r = new Array();
    if($("#items_table :checked").length == 0){
        show_message("Please first select the items from the warehouse!");
        return;
    }
    $("#items_table :checked").each(function(i, el){
        r.push(el.value)
    });
    window.open(labels_url.replace("PLACEHOLDER", r.toString()));
    $("#items_table :checked").attr("checked", false);
}