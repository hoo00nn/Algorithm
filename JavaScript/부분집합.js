const Subset = (arr) => {
  let result = [];

  for (let i = 1; i < 1 << arr.length; i++) {
    result.push([]);

    for (let j = 0; j < arr.length; j++) {
      if (i & (1 << j)) result[i - 1].push(arr[j]);
    }
  }

  return result;
};

let arr = [1, 2, 3, 4];

console.log(Subset(arr));
