
console.log(123, typeof 123);
console.log(123.5, typeof 123.5);
console.log("123", typeof "123");
console.log(true, typeof true);
console.log(false, typeof false); //동적타입

var car;
console.log(typeof car);
var car = "";
console.log(typeof car);

var person = {firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue"};
console.log(typeof person, person);
person = null;

console.log(typeof person, person);



//document.write("Hello World"); //1
//document.write("<h1>Welcome to JS Program</h1>")
//document.write("<h2>Welcome to JS program</h2>")
//
//console.log('Welcome JS program');
//console.info('Welcome JS program');
//console.warn('Welcome JS program');
//console.error('Welcome JS program');
//
//alert('Welcome JS Program');
//var a = prompt('Welcome JS Program');
//console.log(a);