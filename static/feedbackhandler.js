$(document).ready(function() {

    $("#messageform").on("submit", function() {
        $("input[name='stars']").val($('.fa-star.checked').length)
        newMessage($(this));
        return false;
    });
    $("#messageform").on("keypress", function(e) {
        if (e.keyCode == 13) {
            $("input[name='stars']").val($('.fa-star.checked').length)
            newMessage($(this));
            return false;
        }
        return true;
    });
    $("#message").select();
    $('.fa-star').click(function (){
        updateStars($(this));
    })
});

function updateStars(star) {
    star.toggleClass('checked');
    const numberOfStars = $('.fa-star.checked').length
    const starContainer = star.parent();
    starContainer.empty();
    let checkedStars = 0
    for(let i = 0; i < 5; i++ ){
        if (checkedStars < numberOfStars) {
            starContainer.append("<span class='fa fa-star checked'></span>");
            ++checkedStars;
        } else {
            starContainer.append("<span class='fa fa-star'></span>");
        }
    }
    $('.fa-star').click(function (){
        updateStars($(this));
    })
}

function newMessage(form) {
    const message = form.formToDict();
    console.log(message)
    $.postJSON("/feedbacks/", message, function(response) {
        updater.showMessage(response);
        if (message.id) {
            form.parent().remove();
        } else {
            form.find("input[type=text]").val("").select();
        }
    });
}

jQuery.postJSON = function(url, args, callback) {
    $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
            success:
                function(response) {
                    if (callback) callback(eval("(" + response + ")"));
                },
            error: function(response) {
                    console.error("ERROR:", response);
                }
    });
};

jQuery.fn.formToDict = function() {
    const fields = this.serializeArray();
    const json = {};
    for (let i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

const updater = {
    showMessage: function(message) {
        const existing = $("#m" + message.id);
        if (existing.length > 0) return;
        const node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};