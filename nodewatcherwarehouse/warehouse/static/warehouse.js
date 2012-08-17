function set_drop_down(id, divs){
    $(id).change(function(){
        var current_id = id+ "_" + $(this).val();
        var all_divs = "div[id^='" + id.replace("#", "") + "_']";
        $(all_divs).not(current_id).hide();
        $(all_divs).not(current_id).find(":input").val("");
        $(current_id).show();
    });
}
