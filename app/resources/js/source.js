window.onload = function () {
    var li_ol = document.querySelectorAll(".col_ol li  ol");
    for (var i = 0; i < li_ol.length; i++) {
        li_ol[i].style.display = "none"
    };

    var exp_li = document.querySelectorAll(".col_ol li > span");
    for (var i = 0; i < exp_li.length; i++) {
        exp_li[i].style.cursor = "pointer";
        exp_li[i].onclick = showol;
    };
    function showol() {
        nextol = this.nextElementSibling;
        if (nextol.style.display == "block")
            nextol.style.display = "none";
        else
            nextol.style.display = "block";
    }
}
