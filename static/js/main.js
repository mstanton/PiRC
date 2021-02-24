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

function updateThrottlePosition() {
    let tPosition = document.getElementById("tPosition");

    let data = {
        tPosition: tPosition.value
    }

    console.log('tPosition', data)

    fetch(`${window.origin}/forward`, {
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