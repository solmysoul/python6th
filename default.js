
var text = prompt("Enter your name:");
document.write("Your name : " + text + "<br/>");

var len = text.length;
document.write("Number of characters : " + len + "<br/>");

document.write(text.charAt(2) + "<br/>");

document.write(text.toUpperCase() + "<br/>");
document.write(text.toLowerCase() + "<br/>");

var text1 = "hi, ";
var text2 = "bye";
var text3 = text1.concat(text2);
var text4 = text1 + text2;
document.write(text3 + "<br/>");
document.write(text4 + "<br/>");

var text5 = "hello";
var result = text5.slice(3,4);
document.write(result + "<br/>");



//var lastName = "홍"; //4
//var firstName = "길동";
//
//var fullname = lastName + firstName;
//
//console.log(fullname);
//console.log("Today is" + " a " + "beautiful day");
//console.log("My name is " + fullname);
//
//var num1 = 20;
//var num2 = 30;
//var sum = num1 + num2;
//console.log(num1 + " + " + num2 + " = " + sum);
//console.log(num1 + num2);
//console.log("" + num1 + num2);



//var name = "이한솔"; //3
//var age = 26;
//var cgpa = 3.92;
//var lineBreak = "<br/>";
//
//document.write("이름: " + name + lineBreak);
//document.write("나이: " + age + lineBreak);
//document.write("학점: " + cgpa + lineBreak);



//console.log(123, typeof 123); //2
//console.log(123.5, typeof 123.5);
//console.log("123", typeof "123");
//console.log(true, typeof true);
//console.log(false, typeof false); //동적타입
//수
//var car;
//console.log(typeof car);
//var car = "";
//console.log(typeof car);
//
//var person = {firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue"};
//console.log(typeof person, person);
//person = null;
//
//console.log(typeof person, person);



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