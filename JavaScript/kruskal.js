function getParent(parent, x) {
  if (parent[x] === x) return x;
  return (parent[x] = getParent(parent, parent[x]));
}

function unionParent(parent, a, b) {
  a = getParent(parent, a);
  b = getParent(parent, b);

  if (a < b) parent[b] = a;
  else parent[a] = b;

  return parent;
}

function findParent(parent, a, b) {
  a = getParent(parent, a);
  b = getParent(parent, b);

  if (a === b) return true;
  return false;
}

// kruskal 알고리즘은 가장 적은 비용으로 모든 노드를 연결하기 위한 알고리즘
// 즉, 최소 신장 트리를 만들기 위한 대표적인 알고리즘
// 알고리즘 동작 과정
// 1. 간선을 비용 기준으로 오름차순 정렬
// 2. 비용이 가장 적은 간선부터 하나씩 추가
// 3. 추가 하기전에 간선이 사이클을 형성하는지 체크 (union-find 알고리즘 이용)
// 4. 사이클을 형성한다면 간선을 포함하지 않는다.
function kruskal(n, costs) {
  let answer = 0;
  let cycle = [];

  for (let i = 0; i < n; i++) {
    cycle.push(i);
  }

  costs = costs.sort((a, b) => a[2] - b[2]);

  costs.forEach((v) => {
    if (!findParent(cycle, v[0], v[1])) {
      cycle = unionParent(cycle, v[0], v[1]);
      answer += v[2];
    }
  });

  return answer;
}
