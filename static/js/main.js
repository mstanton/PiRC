function updateServoPosition() {
    let sPosition = document.getElementById("sPosition");

    let data = {
        sPosition: sPosition.value
    }

    console.log(data)

    fetch(`${window.origin}/steering`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
        "content-type": "application/json"
        })
      })
    .then(function(response) {
        if (response.status !== 200) {
        console.log(`Looks like there was a problem. Status code: ${response.status}`);
        return;
        }
        response.json().then(function(data) {
        console.log(data);
        });
    })
    .catch(function(error) {
        console.log("Fetch error: " + error);
    });
}


// $(document).ready(function(){

    
//     // $('#steering').change(function(){
//     //     let data = $(this).val();

//     //     // $.post("", function(data) {
//     //     //     console.log("POSTED:", data);
//     //     // })

//     //     // $.ajax({
//     //     //     url: "http://0.0.0.0:5000/steering",
//     //     //     type: "POST",
//     //     //     data: data,
//     //     //     success: function (response) {
//     //     //         console.log(response)
//     //     //     },
//     //     //     error: function (xhr, status) {
//     //     //         console.log("error", xhr, status);
//     //     //     }
//     //     // });
//     //     // Form-encoded Request, like from Form
//     //     // let fetchFormEncodedRequest = {
//     //     //     cache: "no-cache",
//     //     //     method: "POST",
//     //     //     mode: "same-origin",
//     //     //     headers: {
//     //     //         'Content-Type': 'application/x-www-form-urlencoded',
//     //     //     },
//     //     //     body: { data: data }
//     //     // }

//     //     fetch(`${window.origin}/steering/`, data).then(function(response)
//     //         {
//     //             if(response.status!=200)
//     //             {
//     //                 console.log(response.statusText);
//     //             }
//     //             response.json().then(function(data)
//     //             {
//     //                 console.log(data);
//     //             });
//     //         }).catch(function(error)
//     //         {
//     //             console.log(error);
//     //         });
//     // });

   
// });
