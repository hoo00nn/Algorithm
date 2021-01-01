let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

input.splice(input.length - 1, 1);

const [N, M] = input[0].split(" ");
let x = [-1, 1, 0, 0];
let y = [0, 0, -1, 1];
let checked = Array.from(Array(+N), () => Array(+M).fill(false));

input.splice(0, 1);
let arr = input.map((v) => v.split(""));

const bfs = (start, end) => {
  let Q = [{ x: start, y: end, count: 1 }];
  checked[start][end] = true;

  while (Q.length !== 0) {
    let item = Q.shift();

    for (let i = 0; i < x.length; i++) {
      let S = item.x + x[i];
      let E = item.y + y[i];

      if (S > +N - 1 || S < 0) continue;
      if (E > +M - 1 || E < 0) continue;
      if (checked[S][E]) continue;
      if (arr[S][E] === "0") continue;
      if (S === +N - 1 && E === +M - 1) return item.count + 1;

      Q.push({ x: S, y: E, count: item.count + 1 });
      checked[S][E] = true;
    }
  }
};

console.log(bfs(0, 0));
