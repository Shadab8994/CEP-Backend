const urlParams = new URLSearchParams(
    window.location.search
);



// 🔹 Registration Success Popup

if (urlParams.get('registered') === 'true') {

    Swal.fire({

        title: 'Registered Successfully!',

        text: 'You have registered for the event.',

        icon: 'success',

        confirmButtonColor: '#3085d6'

    }).then(() => {

        window.history.replaceState(
            {},
            document.title,
            window.location.pathname
        );

    });
}



// 🔹 Already Registered Popup

if (
    urlParams.get('already_registered')
    === 'true'
) {

    Swal.fire({

        title: 'Already Registered!',

        text: 'You already registered for this event.',

        icon: 'warning',

        confirmButtonColor: '#f59e0b'

    }).then(() => {

        window.history.replaceState(
            {},
            document.title,
            window.location.pathname
        );

    });
}



// 🔹 Feedback Popup

if (urlParams.get('feedback') === 'success') {

    Swal.fire({

        title: 'Feedback Submitted!',

        text: 'Thank you for your feedback.',

        icon: 'success',

        confirmButtonColor: '#3085d6'

    }).then(() => {

        window.history.replaceState(
            {},
            document.title,
            window.location.pathname
        );

    });
}



// 🔹 Delete Popup

function showDeletePopup(event, url) {

    event.preventDefault();

    Swal.fire({

        title: "Delete Event?",

        text: "This event will be removed permanently!",

        icon: "warning",

        showCancelButton: true,

        confirmButtonColor: "#d33",

        cancelButtonColor: "#3085d6",

        confirmButtonText: "Yes, Delete",

        cancelButtonText: "Cancel"

    }).then((result) => {

        if (result.isConfirmed) {

            window.location.href = url;
        }
    });
}



// 🔹 Cancel Button

const cancelBtn = document.getElementById(
    "cancel-btn"
);

if (cancelBtn) {

    cancelBtn.onclick = function () {

        window.location.href = "/";
    };
}