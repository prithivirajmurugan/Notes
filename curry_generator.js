/* function outer() {
  let counter = 0;
  function inner() {
    counter++;
    console.log(counter)
  }
  return inner;
}
const fn = outer();
 */

/* function sum(a, b, c) {
  return a + b + c
}

console.log(sum(2, 3, 5));

function curry(fn) {
  return function (a) {
    return function (b) {
      return function (c) {
         return fn( ,b,c)
      }
    }
  }
}

const curriedSum = curry(sum)

curriedSum(2)(3)(5) */

function sayMyName(name) {
  console.log(`My name is ${name}`);
}

/* 
implicit binding 
explicit binding
New binding
default binding

*/

const person = {
  name:'prithiviraj',
  sayMyName:function(){
    console.log(`My name is ${this.name}`);
  }
}

person.sayMyName();



const obj = {
  [Symbol.iterator]: function () { 
    let step=0
    const iterator = {
      next: function () {
        step++;
        if (step==1) {
          return {
            value:'Hello',done:false}
        }
        else if(step==2){
           return {
            value:'World',done:false
        }
        }
        return {value:undefined,done:true}
       }
    }
    return iterator
  }
}

for (const word of obj) {
  console.log(word);
}


//Generator 

function* generatorFunction() { 
  yield 'Hello'
  yield 'World'
}

const generatorObject = generatorFunction();

for (const word of generatorObject) {
  
  console.log(word)
}