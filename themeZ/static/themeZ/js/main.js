function setBodyBelowHeaderMenu() {
    // get the height of the bootstrap menu and set this height to the padding-top of the body
    var menuHeight = $('.navbar').outerHeight();
    $("body").css("padding-top", menuHeight);
}

// run @ page load

setBodyBelowHeaderMenu();
