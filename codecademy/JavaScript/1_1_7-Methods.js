// Codecademy JavaScript Course
// Feb 16. 2022 - Day 2

// Chap 1 Introduction
// 1. Introduction to JavaScript
// 7. Methods

/*
Does the syntax look familiar? When we use console.log() we're calling the .log() method on the console object.
Let's see console.og() and some real string methods in action!

console.log('hello'.toUpperCase()); --> Prints 'HELLO'
console.log('Hey'.startsWith('H'); --> Prints true

Look at each of the lines above:
* On the first line, the .toUpperCase() method is called on the string instance 'hello'. The result is logged
	to the console. This method returns a string in all capital letters: 'HELLO'.
* On the second line, the .startsWith() method is called on the string instance 'Hey'. This method also accepts the
	character 'H' as an input, or argument, between the parantheses. Since the string 'Hey' starts with the letter 
	'H', the mothod returns the boolean true.

You can find a list of built-in string methods in the JavaScript documentation. Developers use documentation as
a reference tool. It describes JavaScript's keywords, methods and syntax. 
*/

/*
Tasks:
1. Use the .toUpperCase() method to log the string 'Codecademy' to the console in all capital letters.

2. In the second console.log statement, we have a string ' Remove whitespace ' which has spaces before and
	 after the words 'Remove whitespace'.
	 
	 If we browse the JavaScript string documentation, we find several built-in string methods that each
	 accomplish a different goal. The one method that seems ideal for us is .trim()
	 
	 Use the method to remove the whitespace at the beginning and the end of the string in the second 
	 console.log() statement.
*/

console.log('Codecademy'.toUpperCase());

console.log('   Remove whitespaces   '.trim());

