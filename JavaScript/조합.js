const combination = (arr, num) => {
  let result = [];

  if (num == 1) return arr.map((e) => [e]);

  arr.forEach((v, i, array) => {
    let rest = array.slice(i + 1);
    let combinations = combination(rest, num - 1);
    let combiArr = combinations.map((k) => [v, ...k]);
    result.push(...combiArr);
  });

  return result;
};

console.log(combination([1, 2, 3, 4, 5], 3));
