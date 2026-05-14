// 🔹 Registration Popup

const urlParams = new URLSearchParams(window.location.search);

if (urlParams.get('registered') === 'true') {

    Swal.fire({

        title: 'Registered Successfully!',

        text: 'You have registered for the event.',

        icon: 'success',

        confirmButtonColor: '#3085d6'
    });
}


// 🔹 Feedback Popup

if (urlParams.get('feedback') === 'success') {

    Swal.fire({

        title: 'Feedback Submitted!',

        text: 'Thank you for your feedback.',

        icon: 'success',

        confirmButtonColor: '#3085d6'
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