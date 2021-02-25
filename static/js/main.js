/**
 * SERVO / STEERING (PWM)
 */
function updateServoPosition() {
    let sPosition = document.getElementById("sPosition");
    let data = { sPosition: sPosition.value }

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
            console.log(`CODE: ${response.status}`);
            return;
        }
        response.json().then(function(data) {
            console.log('RESPONSE: ', data);
        });
    })
    .catch(function(error) {
        console.log("FETCH RQUEST ERROR: " + error);
    });
}

/**
 * THROTTLE POSITION (PWM)
 */
function updateThrottlePosition() {
    let tPosition = document.getElementById("tPosition");
    let data = { tPosition: tPosition.value }

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
            console.log(`CODE: ${response.status}`);
            return;
        }
        response.json().then(function(data) {
            console.log('RESPONSE: ', data);
        });
    })
    .catch(function(error) {
        console.log("FETCH RQUEST ERROR: " + error);
    });
}