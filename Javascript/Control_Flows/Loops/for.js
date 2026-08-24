// Acutis_Codes/Javascript/Control_Flows/Loops/for.js

// A for loop is a control flow statement that allows you to execute a 
// block of code repeatedly for a specified number of times. It consists of three parts: 
// initialization, condition, and increment/decrement. 
// The loop continues to execute as long as the condition is true.

// Implementation of a for loop in JavaScript
let sum = 0;
for (let i = 1; i <= 10; i++) {
    console.log("Iteration: " + i);
    console.log(i);

    console.log("Sum before adding: " + sum);
    sum += i;
}
console.log("Final sum: " + sum);
