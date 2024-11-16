const op = Array.from(document.getElementsByClassName("flex-item"));
const resetBtn = document.getElementById("reset");
var trials = document.getElementById("trials");
var playerX = document.getElementById("playerX_score");
var playerO = document.getElementById("playerO_score");

var xscore = 0;
var oscore = 0;
var selected = [];
var l;    
winner = false;

function displayLetter(event) {
    var hasBeenclicked = false
    
    //stop accepting inputs when trials == 0 
    if(trials.innerText == 0){
        op.forEach(el =>{
            el.onclick = null;
        })
        return; // Exit the function to prevent further actions
    }
    
    //check is the clicked box has been clicked before
    selected.forEach(el => {
        if(event.target.dataset["number"] == el){
            hasBeenclicked = true;
        }
    })

    if(!hasBeenclicked){
        if(l == "X"){l = "O"} else {l = "X"};
        selected.push(event.target.dataset["number"]);
        event.target.innerText = l;
        winner = (checkWin(op, event.target.dataset["number"],l))    
    }

    if(winner){
        setTimeout(()=>{
            alert("Player " + l + " wins");
            op.forEach(el =>{
                el.innerText = "";
            })
        }, 500)
        //Update the players score
        if(l == "X"){
            xscore++;
            playerX.innerHTML = "PlayerX: " + xscore;
        }else{
            oscore++;
            playerO.innerText = "PlayerO: " + oscore;
        };
        
        selected = [];  //clear selected list
        trials.innerText--; //decrement trial count
        
    };
    

    // check if game is a draw
    let draw = op.every( element => element.innerHTML != "")
    if(draw && !winner && trials.innerText >0){
        setTimeout(()=>{
            alert("draw");
            op.forEach(el =>{
                el.innerText = "";
            })
        }, 500)
        selected=[];
        trials.innerText--;
    }

   
}


checkWin = (arr, spot, letter) =>{
    //wins if it form straight line

    //check rows
    let row_index = Math.floor(spot/3);
    let row = arr.slice(row_index * 3,(row_index + 1) * 3)
    if(row.every(index => index.innerText == letter)){
        return true}


    //check columns
    let col_index = spot % 3;
    let col = [arr[col_index], arr[col_index + 3], arr[col_index + 6]];
    if(col.every(index => index.innerText  === letter)){
        return true}
    
    //diagonals
    //right diagonals
    if(spot % 2 == 0){
        let diagonal1 = [arr[0],arr[4],arr[8]];
        let diagonal2 = [arr[2],arr[4],arr[6]];
        if(diagonal1.every(index => index.innerText == letter)){return true}
        if(diagonal2.every(index => index.innerText == letter)){return true}
    }
    return false;
}


reset = () =>{
   // Reset the game state
   selected = []; // Clear selected list
   xscore = 0; // Reset X score
   oscore = 0; // Reset O score
   playerX.innerHTML = "PlayerX: " + xscore; // Update score display
   playerO.innerText = "PlayerO: " + oscore; // Update score display

   // Prompt for the number of trials
   let a = prompt("Enter no trials: ");
   trials.innerText = a; // Set the trials count

   // Re-enable the click events for the grid items
   op.forEach(el => {
       el.addEventListener('click', displayLetter);
   });

   // Check if trials are 0 on reset
   if (trials.innerText == 0) {
       op.forEach(el => {
            el.onclick = null;
       });
   }
}
