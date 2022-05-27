/**
 * Redirects to the home route
 */
function goBack(ev) {
    ev.preventDefault
    var url = "/"
    window.location = url
}

/**
 * creates delete HTML request when deleting entries
 */
function routeToDelete(ev) {
    ev.preventDefault()
    parent = ev.target.parentNode
    keyValue = parent.children[0].value
    const url = `/deleteentry/${keyValue}`
    fetch(url, { method: 'DELETE' }).then(result => {
        var url = "/";
        window.location = url;
    })
}

/**
 * Handles submission of the drop down menu
 */
function submitMediaDropDown(ev) {
    ev.preventDefault()
    myForm = document.getElementById("mediaDropDownForm")
    myFormData = new FormData(document.getElementById("mediaDropDownForm"))
    if (myFormData.get("medias") == "select_media") {
        alert("Select a type")
        return
    } else {
        myForm.submit()
    }
}

/**
 * Handles the submission of the edit form
 * creates a put HTML request
 */
function handleform(ev) {
    ev.preventDefault(); //stop page reloading
    let myform = document.getElementById('editform');
    let fd = new FormData(myform);

    if (fd.get("name") == "" || fd.get("name") == null) {
        alert("Name is required")
        return
    }

    keyValue = document.getElementById('keyValueHidden').value
    let url = `/editentry/${keyValue}`
    let req = new Request(url, {
        body: fd,
        method: 'PUT',
    });
    fetch(req)
        .then(result => {
            var url = "/"
            window.location = url
        })
}

/**
 * Adds event listeners for the required elements
 */
document.addEventListener('DOMContentLoaded', () => {
    let applyButton = document.getElementById('Apply')
    let cancelButton = document.getElementById('Cancel')
    const buttons = document.querySelectorAll('.del-button');
    const mediaForm = document.getElementById("mediaDropDownForm");

    if (applyButton != null) {
        applyButton.addEventListener('click', handleform)
    }
    if (cancelButton != null) {
        cancelButton.addEventListener('click', goBack)
    }
    if (buttons != null) {
        buttons.forEach(button => {
            button.addEventListener('click', routeToDelete);
        });
    }
    if (mediaForm != null) {
        mediaForm.addEventListener('submit', submitMediaDropDown);
    }
    
});
