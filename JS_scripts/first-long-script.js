// Loops

let arr = [1, 2, 3];
for (let k = 0; k < arr.length; k++) {
    console.log(arr[k]);
}

let obj = {a: 1, b: 2, c: 3};
for (let v in obj) {
    console.log(v);
}

let list = ["x", "y", "z"];
for (let val of list) {
    console.log(val);
}

for (let ch of "Hello") {
    console.log(ch);
}

// Var and Let difference

function varTest() {
    var x = 1;
    if (true) {
        var x = 2;  // same variable
        console.log(x);  // 2
    }
    console.log(x);  // 2
}

function letTest() {
    let x = 1;
    if (true) {
        let x = 2;  // different variable
        console.log(x);  // 2
    }
    console.log(x);  // 1
}

varTest();
letTest();


// Generate Random Color
const generateRandomHexColor = () =>
    `#${Math.floor(Math.random() * 0xffffff).toString(16)}`;

// Scroll To Bottom
const scrollToBottom = (element) =>
    element.scrollIntoView({behavior: "smooth", block: "end"});


// Shuffle Array
const shuffleArray = (arr) => arr.sort(() => Math.random() - 0.5);
// Testing
const arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(shuffleArray(arr1));

// Copy to Clipboard
const copyToClipboard = (text) =>
    navigator.clipboard?.writeText && navigator.clipboard.writeText(text);
// Testing
copyToClipboard("Hello World!");

// Unique Elements
const getUnique = (arr) => [...new Set(arr)];
// Testing
const arr = [1, 1, 2, 3, 3, 4, 4, 4, 5, 5];
console.log(getUnique(arr));

// Detect Dark Mode
const isDarkMode = () =>
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches;
// Testing
console.log(isDarkMode());

// Scroll To Top
const scrollToTop = (element) =>
    element.scrollIntoView({behavior: "smooth", block: "start"});

/*
How to Wait for a Certain Amount of Time
*/
function goToSignupPage() {
    console.log("Sign up page is her!");
}

const wait = async (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
wait(2000).then(() => goToSignupPage());


/*
How to Use the Pluck Property from Array of Objects
*/
const pluck = (objs, key) => objs.map((obj) => obj[key]);
const users = [{name: "Abe", age: 45}, {name: "Jennifer", age: 27}];
pluck(users, 'name'); // ['Abe', 'Jennifer']


/*
How to Insert an Element at a Certain Position
*/
const insert = (arr, index, newItem) => [...arr.slice(0, index), newItem, ...arr.slice(index)];


/*
Positive or negative
*/
const a = 10;
let b = a > 0 ? "positive" : "negative"; // positive
console.log(b)


/*
How to Capitalize Text
*/

const capitalize = (str) => `${str.charAt(0).toUpperCase()}${str.slice(1)}`;
const name = "robert";
capitalize(name) // "Robert";


/*
How to Calculate Percent
*/

const calculatePercent = (value, total) => Math.round((value / total) * 100)
const questionsCorrect = 6;
const questionTotal = 11;
calculatePercent(questionsCorrect, questionTotal); // 55


/*
How to Get a Random Element
*/

const getRandomItem = (items) => items[Math.floor(Math.random() * items.length)];
const items = ["Nicely done!", "Good job!", "Good work!", "Correct!"];
getRandomItem(items); // "Good job!"


/*
How to Remove Duplicate Elements
*/

const removeDuplicates = (arr) => [...new Set(arr)];
const friendList = ["Jeff", "Jane", "Jane", "Rob"];
removeDuplicates(friendList); // ['Jeff', 'Jane', 'Rob']


/*
How to Sort Elements By Certain Property
*/

const sortBy = (arr, key) => arr.sort((a, b) => a[key] > b[key] ? 1 : a[key] < b[key] ? -1 : 0);
const lessons = [{position: 1, name: "Intro"}, {position: 0, name: "Basics"}];
sortBy(lessons, 'position');
// {position: 0, name: 'Basics'},
// {position: 1, name: 'Intro'}


/*
How to Check if Arrays/Objects are Equal
*/

const isEqual = (a, b) => JSON.stringify(a) === JSON.stringify(b);
isEqual([1, '2'], [1, 2]); // false
isEqual([1, 2], [1, 2]); // true


/*
How to Count Number of Occurrences
*/

const countOccurrences = (arr, value) => arr.reduce((a, v) => (v === value ? a + 1 : a), 0);
const pollResponses = ["Yes", "Yes", "No"];
const response = "Yes";
countOccurrences(pollResponses, response); // 2

let x = 'hello'
if (x === 'hello') {
    console.log(x);
}
