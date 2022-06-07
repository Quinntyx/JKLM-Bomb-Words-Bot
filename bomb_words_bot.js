console.log("Running!");

// Configuration
const targetLength = 10; // the length you want the bot to shoot for
const targetBias = 1.2; // the amount you want the bot to care about the target len. 1 to disable.
const letterWeights = {
    'a': 0.75,
    'b': 1,
    'c': 1,
    'd': 1,
    'e': 0.75,
    'f': 1.3,
    'g': 1,
    'h': 1,
    'i': 0.75,
    'j': 2.3,
    'k': 0,
    'l': 1,
    'm': 1,
    'n': 1,
    'o': 0.8,
    'p': 1,
    'q': 2.5,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1.5,
    'v': 1.8,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
    '-': 0.25,
    "'": 0.1
}, guessedLetters = [], guessedWords = [];

console.log("Registered Configurations!")
console.log("As Follows:")
console.log(`Target Length: ${targetLength}\n Target Bias: ${targetBias}`)


// var wordData = FileReader().readAsText(Blob())
function value(word, weightings) {
    let score = 1
    let wordSet = []
    for (let letter of word) {
        if (!wordSet.includes(letter)) {
            wordSet.push(letter)
            // console.log(wordSet);
        }
    }

    for (let letter of wordSet) {
        if (letter in guessedLetters) {
            continue;
        }
        score += weightings[letter]
    }

    let scoreMultiplier = 1 / (targetBias ** Math.abs(word.length - targetLength));

    console.log(score);
    console.log(scoreMultiplier);

    return score * (1 + scoreMultiplier) / 2;

}

function getBest(data) {
    const letterWeightsForGuessed = {...letterWeights};
    guessedLetters.forEach(l => {letterWeights[l] = 0});

    let out = [];

    for (let word of data) {
        out.push([word, value(word, letterWeightsForGuessed)]);
    }

    out.sort(function(a, b) {
        return a[1] - b[1];
    });

    return out;


}

function guess(word) {
    // Updates the guessed words and guessed letters lists
    // to contain the target word.
    // Will be updated to remove guessedLetters once I implement a getter func.
    for (let letter of word) {
        if (!guessedLetters.contains(letter)) {
            guessedLetters.push(letter);
        }
    }

    if (!guessedWords.contains(word)) {
        guessedWords.push(word)
    }

    console.log(`Guessed ${word}`)
}

function panelPrint(value) {
    let console = document.querySelector("p.cheatOutput")

    let lineCount = console.innerText.split('\n').length
    document.querySelector("p.cheatOutput").innerText += "\n" + value;
}

const sidebar = document.querySelector("div.chat.pane");

if (sidebar) {
    let outPane = document.createElement("div");
    outPane.className = "cheatPane"
    outPane.style.backgroundColor = "var(--accent-2)";

    sidebar.append(outPane);


    let outText = document.createElement("p");
    outText.className = "cheatOutput";
    outText.style.height = "100px";
    outText.innerText = "Testing Testing 123";

    Object.assign(outText.style, {
        margin: "8px",
        borderRadius: "5px",
        backgroundColor: "var(--accent-3)",
        padding: "5px",
        fontFamily: "JetBrainsMono"
    });

    document.querySelector("div.cheatPane").append(outText)

    let cheatInput = document.createElement("textarea")
    cheatInput.className = "cheatInput";
    cheatInput.style.height = "auto";
    cheatInput.placeholder = "Type here to issue commands";

    Object.assign(cheatInput.style, {
        margin: "8px",
        borderRadius: "5px",
        backgroundColor: "var(--accent-3)",
        padding: "5px",
        marginTop: "0px",
        color: "#aaa",
        width: "100%",
        resize: "none",
        outline: "none",
        border: "none",
        lineHeight: "1.25",
        fontSize: "smaller"
    });

    document.querySelector("div.cheatPane").append(cheatInput)
}

let syllable = '';

while (1) {
    if (syllable !== document.querySelector("div.syllable").innerHTML) {
        syllable = document.querySelector("div.syllable").innerHTML
        console.log(`Syllable Changed to ${syllable}`)

    }
}



