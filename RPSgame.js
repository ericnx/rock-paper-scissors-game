const playerScoreDisplay = document.getElementById("you-score");
const computerScoreDisplay = document.getElementById("computer-score");
const message = document.getElementById("message");
const blueDisplay = document.getElementById("blue-display");
const redDisplay = document.getElementById("red-display");
let playerScore = 0;
let computerScore = 0;

// Runs when the player clicks one of the choice buttons
function playGame(playerPick){
    let computerPick = getComputerPick();
    let winner = determineWinner(playerPick, computerPick);
    displayPicks(playerPick, computerPick);
    displayResult(winner, playerPick, computerPick);
    updateScore(winner);
}

// Get the computer's random pick from the 3 possible choices
function getComputerPick(){
    const picks = ['Rock', 'Paper', 'Scissors'];
    return picks[Math.floor(Math.random() * picks.length)]
}

// Determine who wins the round
function determineWinner(playerPick, computerPick){
    if (playerPick === computerPick){
        return 'Tie';
    }
    else {
        switch (playerPick) {
            case 'Rock':               
                return (computerPick === 'Scissors') ? 'You' : 'Computer'
            case 'Paper':
                return (computerPick === 'Rock') ? 'You' : 'Computer'
            case 'Scissors':
                return (computerPick === 'Paper') ? 'You' : 'Computer'
        }
    }
}

// Adds 1 to the respective winner's score
function updateScore(winner){
    if (winner === 'You'){
        playerScore++;
        playerScoreDisplay.textContent = playerScore;
    }
    else if (winner === 'Computer') {
        computerScore++;
        computerScoreDisplay.textContent = computerScore;
    }
}

// Displays the result of the round below the scoreboard
function displayResult(winner, playerPick, computerPick){
    if (winner === 'Tie'){
        message.textContent = "It's a tie! Go again!";
    }
    else if (winner === 'You'){
        message.textContent = `You win! ${playerPick} beats ${computerPick}.`;
    }
    else {
        message.textContent = `Computer wins! ${computerPick} beats ${playerPick}.`;
    }
}

// Displays the picks' images inside the red and blue boxes
function displayPicks(playerPick, computerPick){
    blueDisplay.innerHTML = `<img src="images/${playerPick.toLowerCase()}.png" class="pick-display">`;
    redDisplay.innerHTML = `<img src="images/${computerPick.toLowerCase()}.png" class="pick-display">`;
}