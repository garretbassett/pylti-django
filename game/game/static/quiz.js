document.addEventListener("DOMContentLoaded", function () {
    var launchId = document.getElementById("launchId").value;
    var selectedAnswer;  // Global variable to store the selected answer

    // var radioButtons = document.querySelectorAll('input[name="answer"]');
    // radioButtons.forEach(function (radio) {
    //     radio.addEventListener("change", function (event) {
    //         selectedAnswer = event.target.value;  // Update the selected answer
    //     });
    // });
    
    quizForm.addEventListener("submit", function (event) {
        event.preventDefault();
        
        var selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (!selectedAnswer) {
            alert("Please select an answer.");
            return;
        }

        var answerValue = selectedAnswer.value;
        var earnedScore = calculateEarnedScore(answerValue);

        submitScore(earnedScore);
    });

    function calculateEarnedScore(answer) {
        if (answer === "A") {
            return 10;
        } else if (answer === "B") {
            return 8;
        } else if (answer === "C") {
            return 7;
        } else if (answer === "D") {
            return 6;
        }
    }

    var submitScore = function (score) {
        console.log("\n\nScore: " + score);
        var xhttp = new XMLHttpRequest();
        // xhttp.addEventListener("load", getScoreBoard);
        xhttp.open("POST", "/api/quiz_score/" + launchId + "/" + score + "/", false);
        xhttp.send();
    };

    // function submitScore(earnedScore) {
    //     var xhttp = new XMLHttpRequest();
    //     xhttp.addEventListener("load", function() {
    //         if (xhttp.status === 200) {
    //             // Score submitted successfully
    //             console.log("Score submitted successfully");
    //         } else {
    //             // Error submitting score
    //             console.error("Error submitting score:", xhttp.responseText);
    //         }
    //     });
    //     xhttp.open("POST", "/api/score/" + launchId + "/" + earnedScore + "/", true);
    //     xhttp.send();
    // }

});



// add endGame()

// var endGame = function () {
//     pause = true;
//     gameover = true;
//     submitScore();
// };

// var submitScore = function () {
//     var time_taken = Math.floor(Date.now() / 1000) - startTime;
//     var xhttp = new XMLHttpRequest();
//     // xhttp.addEventListener("load", getScoreBoard);
//     xhttp.open("POST", "/api/score/" + launchId + "/" + score + "/" + time_taken + "/", false);
//     xhttp.send();
// };

// var getScoreBoard = function () {
//     var xhttp = new XMLHttpRequest();
//     xhttp.addEventListener("load", refreshScoreBoard);
//     xhttp.open("GET", "/api/scoreboard/" + launchId + "/", true);
//     xhttp.send();
// };

// document.getElementById("refresh-btn").addEventListener("click", function() {
//     getScoreBoard();
// });

// getScoreBoard();

// document.addEventListener("DOMContentLoaded", mainGame);
