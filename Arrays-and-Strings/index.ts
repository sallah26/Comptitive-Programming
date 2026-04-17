const ages:number[] = [12, 42, 32, 46, 51, 7, 15];

console.log("first item is: ", ages[0])
console.log("length of the ages is: ", ages.pop())
console.log("length of the ages is: ", ages.push(100))
console.log("length of the ages is: ", ages.slice(1, 3))
// console.log("length of the ages is: ", ages.concat([1,2,3,4]))
const newArray:number[] = ages.concat([1,2,3,4])
console.log("new array is: ", newArray.every((item) => item < 818))

// 
console.log("length of the ages is: ", ages.fill(2, 3, 5))
console.log("I think we", ages.filter((item) => item < 18))
console.log("I think we", ages.find((item) => item > 50))

console.log("I think we", ages)
console.log("I think we", ages.findIndex((item) => item > 50))
console.log("I think we", ages.forEach((item) => console.log(item)))
console.log("I think we", ages.join(" "))
const neww = ages.join(" ")

console.log("new is", ages)
console.log("new is", typeof(neww))