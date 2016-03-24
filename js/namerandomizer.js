var names = [
    "Tom! Tom Carrio!",
    "Michael! Michael Atang!",
    "Jon! Jon Calvert!",
    "Wesley! Wesley Austin!"
];

//This function randomizes the names for randomized access later
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

return array;
}

//Shuffle the array
names = shuffle(names);

//Create IDs for each element of the array to be called by
document.getElementById("name1").innerHTML = names.pop();
document.getElementById("name2").innerHTML = names.pop();
document.getElementById("name3").innerHTML = names.pop();
document.getElementById("name4").innerHTML = names.pop();

//Popping conserves space as the elements are removed 