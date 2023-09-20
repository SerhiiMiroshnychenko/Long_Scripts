// Build-in Methods

let res = [4, 5, 1, 8, 2, 0].filter(function (x) {
  return x > 3;
})[0];
console.log(res);

let res =
[4, 5, 1, 8, 2, 0].find(x => x > 3);
console.log(res);

let res =
[4, 5, 1, 8, 2, 0].findIndex(x => x > 3);
console.log(res);

console.log(Array(3 + 1).join("foo")); //foofoofoo

console.log("foo".repeat(3)); //foofoofoo

console.log("SoloLearn".indexOf("Solo") === 0); // true
console.log("SoloLearn".indexOf("Solo") === (4 - "Solo".length)); // true
console.log("SoloLearn".indexOf("loLe") !== -1); // true
console.log("SoloLearn".indexOf("olo", 1) !== -1); // true
console.log("SoloLearn".indexOf("olo", 2) !== -1); // false

console.log("SoloLearn".startsWith("Solo", 0)); // true
console.log("SoloLearn".endsWith("Solo", 4)); // true
console.log("SoloLearn".includes("loLe")); // true
console.log("SoloLearn".includes("olo", 1)); // true
console.log("SoloLearn".includes("olo", 2)); // false

// Modules

// lib/math.js
export let sum = (x, y) => { return x + y; }
export let pi = 3.14;

// app.js
import * as math from "lib/math"
console.log(`2p = + ${math.sum(math.pi, math.pi)}`)


// Iterators & Generators

let myIterableObj = { 
  [Symbol.iterator] : function* () {
    yield 1; yield 2; yield 3;
  }
};
console.log([...myIterableObj]); // [ 1, 2, 3 ]

function* idMaker() {
  let index = 0;
  while (index < 5)
    yield index++;
}
var gen = idMaker();
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
// Try to add one more console.log, just like the above see what happens.

const arr = ['0', '1', '4', 'a', '9', 'c', '16'];
const my_obj = {
  [Symbol.iterator]: function*() {
    for(let index of arr) {
      yield `${index}`;
    }
  }
};
const all = [...my_obj] /* Here you can replace the '[...my_obj]' with 'arr'. */
  .map(i => parseInt(i, 10))
  .map(Math.sqrt)
  .filter((i) => i < 5) /* try changing the value of 5 to 4 see what happens.*/
  .reduce((i, d) => i + d); /* comment this line while you are changing the value of the line above */
console.log(all);

// Promises

setTimeout(function() {
    console.log("Work 1");
    setTimeout(function() {
        console.log("Work 2");
    }, 1000);
}, 1000);
console.log("End");

new Promise(function(resolve, reject) {
    // Work
    if (success)
        resolve(result);
    else
        reject(Error("failure"));
});

function asyncFunc(work) {
    return new Promise(function(resolve, reject) {
        if (work === "")
            reject(Error("Nothing"));
        setTimeout(function() {
            resolve(work);
        }, 1000);
    });
}
asyncFunc("Work 1") // Task 1
.then(function(result) {
    console.log(result);
    return asyncFunc("Work 2"); // Task 2
}, function(error) {
    console.log(error);
})
.then(function(result) {
    console.log(result);
}, function(error) {
    console.log(error);
});
console.log("End");

// Set Object

let set = new Set([1, 2, 4, 2, 59, 9, 4, 9, 1]);
console.log(set.size); // 5

let set = new Set();
set.add(5).add(9).add(59).add(9);
console.log(set.has(9));
for (let v of set.values())
    console.log(v);

// Map Object

let map = new Map([['k1', 'v1'], ['k2', 'v2']]);
console.log(map.size); // 2

let map = new Map();
map.set('k1', 'v1').set('k2', 'v2');
console.log(map.get('k1')); // v1
console.log(map.has('k2')); // true
for (let kv of map.entries())
    console.log(kv[0] + " : " + kv[1]);

// Inheritance

class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(this.name + ' makes a noise.');
  }
}
class Dog extends Animal {
  speak() {
    console.log(this.name + ' barks.');
  }
}
let dog = new Dog('Rex');
dog.speak(); // Rex barks.

class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(this.name + ' makes a noise.');
  }
}
class Dog extends Animal {
  speak() {
    super.speak(); // Super
    console.log(this.name + ' barks.');
  }
}
let dog = new Dog('Rex');
dog.speak();
// Rex makes a noise.
// Rex barks.

// Class Methods

class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  get area() {
    return this.calcArea();
  }
  calcArea() {
    return this.height * this.width;
  }
}
const square = new Rectangle(5, 5);
console.log(square.area); // 25

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;
    return Math.hypot(dx, dy);
  }
}
const p1 = new Point(7, 2);
const p2 = new Point(3, 8);
console.log(Point.distance(p1, p2));

// Classes

class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
const square = new Rectangle(5, 5);
const poster = new Rectangle(2, 3); 
console.log(square.height); //5

var Square = class Rectangle {
    constructor(height, width) {
        this.height = height;
        this.width = width;
  }
};
const square = new Square(5, 5);
const poster = new Square(2, 3); 
console.log(square.height);

var Square = class {
    constructor(height, width) {
        this.height = height;
        this.width = width;
  }
};
const square = new Square(5, 5);
const poster = new Square(2, 3); 
console.log(square.height);

// The Spread Operator

const myFunction = (w, x, y, z) => {
    console.log(w + x + y + z);
};
let args = [1, 2, 3];
myFunction(...args, 4); //10

var dateFields = [1970, 0, 1];  // 1 Jan 1970
var date = new Date(...dateFields);
console.log(date);

var arr = ["One", "Two", "Five"];
arr.splice(2, 0, "Three");
arr.splice(3, 0, "Four");
console.log(arr); // One,Two,Three,Four,Five

let newArr = ['Three', 'Four']; 
let arr = ['One', 'Two', ...newArr, 'Five'];
console.log(arr); // One,Two,Three,Four,Five

const obj1 = { foo: 'bar', x: 42 };
const obj2 = { foo: 'baz', y: 5 };
const clonedObj = { ...obj1 }; // { foo: "bar", x: 42 }
const mergedObj = { ...obj1, ...obj2 }; // { foo: "baz", x: 42, y: 5 }

const obj1 = { foo: 'bar', x: 42 };
const obj2 = { foo: 'baz', y: 5 };
const merge = (...objects) => ({ ...objects });
let mergedObj = merge (obj1, obj2);
// { 0: { foo: 'bar', x: 42 }, 1: { foo: 'baz', y: 5 } }
let mergedObj2 = merge ({}, obj1, obj2);
// { 0: {}, 1: { foo: 'bar', x: 42 }, 2: { foo: 'baz', y: 5 } }

// Rest Parameters

function containsAll(arr) {
    for (let k = 1; k < arguments.length; k++) {
        let num = arguments[k];
        if (arr.indexOf(num) === -1) {
            return false;
        }
    }
    return true;
}
let x = [2, 4, 6, 7];
console.log(containsAll(x, 2, 4, 7));
console.log(containsAll(x, 6, 4, 9));

function containsAll(arr, ...nums) {
    for (let num of nums) {
        if (arr.indexOf(num) === -1) {
            return false;
        }
    }
    return true;
}
let x = [2, 4, 6, 7];
console.log(containsAll(x, 2, 4, 7));
console.log(containsAll(x, 6, 4, 9));


// Object Destructuring

let obj = {h:100, s: true};
let {h, s} = obj;
console.log(h);
console.log(s);

let a, b;
({a, b} = {a: 'Hello ', b: 'Jack'});
console.log(a + b);

let {a, b} = {a: 'Hello ', b: 'Jack'};
console.log(a + b);

var o = {h: 42, s: true};
var {h: foo, s: bar} = o;
//console.log(h); // Error
console.log(foo); // 42

var obj = {id: 42, name: "Jack"};
let {id = 10, age = 20} = obj;
console.log(id); // 42
console.log(age); // 20

// Array Destructuring

let arr = ['1', '2', '3'];
let [one, two, three] = arr;
console.log(one); // 1
console.log(two); // 2
console.log(three); // 3

let a = () => {
    return [1, 3, 2];
};
let [one, , two] = a();
console.log(one); // 1
console.log(two); // 2

let a, b, c = 4, d = 8;
[a, b = 6] = [2];
console.log(a); // 2
console.log(b); // 6
[c, d] = [d, c];
console.log(c); // 8
console.log(d); // 4

// Object.assign()

let person = {
    name: 'Jack',
    age: 18,
    sex: 'male'
};
let student = {
    name: 'Bob',
    age: 20,
    xp: '2'
};
let newStudent = Object.assign({}, person, student);
console.log(newStudent.name); // Bob
console.log(newStudent.age); // 20
console.log(newStudent.sex); // male
console.log(newStudent.xp); // 2

let person = {
    name: 'Jack',
    age: 18
};
let newPerson = person;
newPerson.name = 'Bob';
console.log(person.name); // Bob
console.log(newPerson.name); // Bob

let person = {
    name: 'Jack',
    age: 18
};
let newPerson = Object.assign({}, person);
newPerson.name = 'Bob';
console.log(person.name); // Jack
console.log(newPerson.name); // Bob

let person = {
    name: 'Jack',
    age: 18
};
let newPerson = Object.assign({}, person, {name: 'Bob'});
console.log(newPerson.name); // Bob

// Computed Property Names

let prop = 'name';
let id = '1234';
let mobile = '08923';
let user = {
  [prop]: 'Jack',
  [`user_${id}`]: `${mobile}`
};
console.log(user.name); // Jack
console.log(user.user_1234); // 08923

var i = 0;
var a = {
  ['foo' + ++i]: i,
  ['foo' + ++i]: i,
  ['foo' + ++i]: i
};
console.log(a.foo1); // 1
console.log(a.foo2); // 2
console.log(a.foo3); // 3

var param = 'size';
var config = {
    [param]: 12,
    ['mobile' + param.charAt(0).toUpperCase() + param.slice(1)]: 4
};
console.log(config.mobileSize); // 4

// Objects

let tree = {
    height: 10,
    color: 'green',
    grow() { 
        this.height += 2;
    }
};
tree.grow();
console.log(tree.height); // 12

let height = 5;
let health = 100;
let athlete = {
    height, // height: height,
    health // health: health
};
console.log(athlete.height); // 5

var a = {x: 1, x: 2, x: 3, x: 4};
console.log(a.x); // 4 

// Default Parameters

/*
function test(a, b = 3, c = 42) {
  return a + b + c;
}
console.log(test(5));
*/

// Full ES6 equivalent
const test = (a, b = 3, c = 42) => a + b + c;
console.log(test(5));

// Functions

function add(x, y) {
    var sum = x+y;  
    console.log(sum);
}
add(35, 7);

const add = (x, y) => {
    let sum = x + y;  
    console.log(sum);
}
add(35, 7);

const greet = x => "Welcome " + x;
alert(greet("David"));

const x = () => alert("Hi");
x();

var arr = [2, 3, 7, 8];
arr.forEach(function(el) {
    console.log(el * 2);
});

const arr = [2, 3, 7, 8];
arr.forEach(v => {
    console.log(v * 2);
});

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
