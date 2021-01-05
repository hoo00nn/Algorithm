// const permutation = (input) => {
//   let result = [];

//   const permute = (arr, m = []) => {
//     if (arr.length === 0) result.push(m);
//     else {
//       for (let i = 0; i < arr.length; i++) {
//         let curr = arr.slice();
//         let next = curr.splice(i, 1);
//         permute(curr.slice(), m.concat(next));
//       }
//     }
//   };

//   permute(input);

//   return result;
// };

// console.log(permutation([1, 2, 3, 4]));

// const input = [1, 2, 3, 4, 5];
// const answer = [];

// const permutation = (arr, n, k) => {
//   if (n === arr.length - 1) {
//     const str = arr.slice(0, k).join("");

//     if (!answer.includes(str)) answer.push(str);

//     return;
//   } else {
//     for (let i = n; i < arr.length; i++) {
//       let temp = arr[n];
//       arr[n] = arr[i];
//       arr[i] = temp;

//       permutation(arr, n + 1, k);

//       arr[i] = arr[n];
//       arr[n] = temp;
//     }

//     return answer;
//   }
// };

// console.log(permutation(input, 0, 3));

// const permutation = (arr, n = arr.length) => {
//   if (n === 0) return [[]];
//   if (!(n >= 0)) return [];

//   const output = [];

//   for (let i = 0; i < arr.length; i++) {
//     if (arr.indexOf(arr[i]) < i) continue;

//     const newArr = arr.slice();
//     newArr.splice(i, 1);
//     output.push(...permutation(newArr, n - 1).map((v) => [arr[i], ...v]));
//   }

//   return output;
// };

// const arr = [1, 2, 3, 4, 5];

// console.log(permutation(arr, 3));

const permutation = (arr, num) => {
  let result = [];

  if (num == 1) return arr.map((v) => [v]);

  arr.forEach((v, i, array) => {
    let rest = [...array.slice(0, i), ...array.slice(i + 1)];
    let permutations = permutation(rest, num - 1);
    let permuArr = permutations.map((k) => [v, ...k]);
    result.push(...permuArr);
  });
  return result;
};

console.log(permutation([1, 2, 3, 4, 5], 3));
