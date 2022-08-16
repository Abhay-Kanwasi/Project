# Typing Speed Calculator

__Objective__

In this project we write a program to calculate our speed word per second when we enter a string.

<br />

__Required Modules__

__(a) time :__  This module required for calculating the word per second.

__(b) random :__  This module required for randomly choose sentences to appear.

<br />

__Working__

__Step 1 :__ Create a variable and store multiple strings in it. Then use random module to choose randomly a string from that variable. Then print that randomly choose one string.

__Step 2 :__ Before taking input write a time function and store it to a variable start_time which will help us to calculate time afterwards. Create a variable testinput and take input form the user. Then again write time function and store it to a variable end_time.Then print there typing speed and how many errors they do.

__Step 3 :__ For calculating the typing speed and errors create two functions.

1. Error function with 2 arguments : string and inputed text from the user. Then create a counter(variable) and set it to zero. Then use a for loop to check each character of string and match it to the user input string. If it doesn't match it will incerase +1 to counter(error+=1).

2. Typing speed with 3 arguments : start_time,end_time and testinput.<br /> 
Here start_time will work like a stopwatch which will start when compiler execute it same goes for end_time as well. Now if we want to calculate this time(time delay) we simply do [end_time-start_time].<br />
Then use time delay and divide it by length of user_input and you get word per second.<br />
<br />
 TIP  : Make sure use roundoff so you don't get error because when we deal with division it is highly possible to get an infinite division.

<br />

__Conclusion__

We use simple approch and minimum to minimum resource to create basic functionality of a typing speed not calculator.


