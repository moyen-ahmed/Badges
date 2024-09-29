let e=4;
let f=5;
console.log("e= ",3,"& f", f);
console.log("e+b =",e+f);
console.log("e-b =",e-f);
console.log("e*b =",e*f);
//Unary Operators
console.log("Unary Operators")
let m=4;
let n=5;
console.log("m= ",m,"& n =", n); 
m++;
n++;
console.log(m,n)
//a++(post increment)
//++a(post incerement)
//same way for (--)
// Equall to ==
// not queal to != (ony valu check)
//  Equall to & data type ===
//  not queueMicrotask. !== (also check data type)
// and && 
// or ||
// logical not !
// Post-increment (a++)
let a = 5;
console.log("Before post-increment: ", a); // 5
console.log("Post-increment a++: ", a++);  // 5 (returns the value first, then increments)
console.log("After post-increment: ", a);  // 6

// Pre-increment (++a)
let b = 5;
console.log("Before pre-increment: ", b); // 5
console.log("Pre-increment ++a: ", ++b);  // 6 (increments first, then returns the value)
console.log("After pre-increment: ", b);  // 6

// Post-decrement (a--)
let c = 5;
console.log("Before post-decrement: ", c); // 5
console.log("Post-decrement a--: ", c--);  // 5 (returns the value first, then decrements)
console.log("After post-decrement: ", c);  // 4

// Pre-decrement (--a)
let d = 5;
console.log("Before pre-decrement: ", d); // 5
console.log("Pre-decrement --a: ", --d);  // 4 (decrements first, then returns the value)
console.log("After pre-decrement: ", d);  // 4

// Equal to (==) (only checks value)
let x = '5';
let y = 5;
console.log("Is x == y?: ", x == y);  // true (checks value only, type is ignored)

// Not equal to (!=) (only checks value)
console.log("Is x != y?: ", x != y);  // false (checks value only, type is ignored)

// Strictly equal to (===) (checks value and type)
console.log("Is x === y?: ", x === y);  // false (checks value and type, different types)

// Strictly not equal to (!==) (checks value and type)
console.log("Is x !== y?: ", x !== y);  // true (different value types)

// Logical AND (&&)
let p = true;
let q = false;
console.log("p && q: ", p && q);  // false (both must be true for && to return true)

// Logical OR (||)
console.log("p || q: ", p || q);  // true (only one needs to be true for || to return true)

// Logical NOT (!)
let r = true;
console.log("!r: ", !r);  // false (negates the value of r)



//Coditional statement
console.log("Coditional statement")
//if 
let age = 20;

if (age >= 18) {
  console.log("You are eligible to vote."); // This will run if the condition is true
}

// else if
let score = 85;

if (score >= 90) {
  console.log("You got an A.");
} else if (score >= 80) {
  console.log("You got a B.");
} else if (score >= 70) {
  console.log("You got a C.");
} else if (score >= 60) {
  console.log("You got a D.");
} else {
  console.log("You got an F.");
}
// 
//Ternary Operator
console.log("Ternary Operator");
//    a?b:c>> Condition? truth Output : false output
let year= 20;
let message = year >= 18 ? "You are an adult." : "You are a minor.";
console.log(message); 


//pop Up ..give me pop up message in Disply
  
alert("Hello boss");//one time 

//promt also pop up type but it gives also data input
let name=prompt("What is your name ?");
console.log(name)

//Example >>>>>>>>>>>>>
// Get user input (prompt returns a string, so we convert it to a number)
let number = parseInt(prompt("Enter a number:"));

// Check if the number is odd or even
if (number % 2 === 0) {
  console.log("It's a 'Kharap' number.");  // If the number is even
} else {
  console.log("It's a 'Good' number.");    // If the number is odd
}
    //Thats all//
    //Ishtiak Ahmed Moyen