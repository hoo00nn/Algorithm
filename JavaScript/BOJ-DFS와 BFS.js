let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [N, M, V] = input[0].split(" ");
let arr = Array.from(Array(+N), () => Array(+N).fill(0));

input.splice(0, 1);
input.splice(M, 1);

input.forEach((v) => {
  let [L, R] = v.split(" ");

  arr[+L - 1][+R - 1] = 1;
  arr[+R - 1][+L - 1] = 1;
});

const bfs = (v) => {
  let visited = [];
  let Q = [v - 1];

  while (Q.length !== 0) {
    let item = Q.shift();

    if (visited.indexOf(item) !== -1) continue;

    visited.push(item);

    for (let i = 0; i < arr[item].length; i++) {
      if (arr[item][i] === 0) continue;
      if (visited.indexOf(i) !== -1) continue;

      Q.push(i);
    }
  }

  return visited;
};

const dfs = (v) => {
  let visited = [];
  let S = [v - 1];

  while (S.length !== 0) {
    let item = S.pop();

    if (visited.indexOf(item) !== -1) continue;

    visited.push(item);

    for (let i = arr[item].length - 1; i >= 0; i--) {
      if (arr[item][i] === 0) continue;
      if (visited.indexOf(i) !== -1) continue;

      S.push(i);
    }
  }

  return visited;
};

console.log(
  dfs(V)
    .map((v) => v + 1)
    .join(" ")
);
console.log(
  bfs(V)
    .map((v) => v + 1)
    .join(" ")
);
