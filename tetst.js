// function initialize() {
//     const buttons = document.querySelectorAll('button');
  
//     buttons.forEach(button => {
//       button.addEventListener('click', event => {
//         // Write your code here
//         const direction = button.textContent.trim(); // Get the text content of the button (either '↓' or '↑')
//       const parentDiv = button.parentNode; // Get the parent div of the button

//       if (direction === '↓') {
//         // Move the span and button down
//         const nextSibling = parentDiv.nextElementSibling;
//         if (nextSibling) {
//           parentDiv.parentNode.insertBefore(nextSibling, parentDiv);
//         }
//       } else if (direction === '↑') {
//         // Move the span and button up
//         const previousSibling = parentDiv.previousElementSibling;
//         if (previousSibling) {
//           parentDiv.parentNode.insertBefore(parentDiv, previousSibling);
//         }
//       }
    
//       });
//     });
//   }
  
//   document.body.innerHTML = `
//   <div>
//       <span>Prepare presentation</span>
//       <button class="downButton" type="button">↓</button>
//   </div>
//   <div>
//       <span>Read emails</span>
//       <button class="downButton" type="button">↓</button>
//       <button class="upButton" type="button">↑</button></div>
//   <div>
//       <span>Monthly report</span>
//       <button class="upButton" type="button">↑</button>
//   </div>`;
  
//   initialize();
  
//   document.querySelectorAll("button")[0].click();
//   document.querySelectorAll("button")[3].click();
//   document.querySelectorAll("button")[1].click();
  
//   console.log(document.body.innerHTML);
// function academicNotes(notes) {
//   if (typeof notes !== 'object' || Array.isArray(notes)) {
//       throw new Error('Not an object');
//   }
  
//   const keys = Object.keys(notes);
//   if (keys.length === 0) {
//       throw new Error('Object is empty');
//   }
  
//   let accumulatedPercentage = 0;
//   let accumulatedNote = 0.0;
  
//   for (const key of keys) {
//       const value = notes[key];
//       const keyNumber = parseFloat(key);

//       // Validate keys
//       if (isNaN(keyNumber) || keyNumber === null || key === '') {
//           throw new Error('Some key is not a number');
//       }
//       if (keyNumber < 0 || keyNumber > 5) {
//           throw new Error('Some key is out of range');
//       }
      
//       // Validate values
//       if (value === null || value === undefined || typeof value !== 'number' || !Number.isInteger(value)) {
//           throw new Error('Some value is not an integer');
//       }
//       if (value <= 0 || value > 100) {
//           throw new Error('Some value is out of range');
//       }
      
//       accumulatedPercentage += value;
//       accumulatedNote += keyNumber * value;
//   }
  
//   if (accumulatedPercentage > 100) {
//       throw new Error('Total sum of percentage values exceeds the maximum');
//   }
  
//   return {
//       accumulatedPercentage: accumulatedPercentage,
//       accumulatedNote: accumulatedPercentage > 0 ? accumulatedNote / accumulatedPercentage : 0
//   };
// }

// // Example test cases
// console.log(academicNotes({ 2.9: 40, 3.1: 30 }));  // Expected Output: { accumulatedPercentage: 70, accumulatedNote: 3.0 }
// console.log(academicNotes({ 4: 50, 3.5: 50 }));    // Expected Output: { accumulatedPercentage: 100, accumulatedNote: 3.75 }

// Error cases
// console.log(academicNotes([{ 2.9: 40 }]));        // Expected Output: throws an error with message 'Not an object'
// console.log(academicNotes({}));                   // Expected Output: throws an error with message 'Object is empty'
// console.log(academicNotes({ 2.9: 40, null: 30 })); // Expected Output: throws an error with message 'Some key is not a number'
// console.log(academicNotes({ 2.9: 40, 6: 30 }));    // Expected Output: throws an error with message 'Some key is out of range'
// console.log(academicNotes({ 2.9: null, 3.1: 30 })); // Expected Output: throws an error with message 'Some value is not an integer'
// console.log(academicNotes({ 2.9: 40, 3.1: -30 })); // Expected Output: throws an error with message 'Some value is out of range'
// console.log(academicNotes({ 2.9: 71, 3.1: 30 }));  // Expected Output: throws an error with message 'Total sum of percentage values exceeds the maximum'

function sort(initialArray, sortingArray) {
    let paired = sortingArray.map((value, index) => [value, initialArray[index]]);
    paired.sort((a, b) => a[0] - b[0]);
    return paired.map(pair => pair[1]);
}

console.log(sort(['x', 'y', 'z'], [1, 2, 0]))