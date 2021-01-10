// 여러 개의 노드가 존재할 때, 두 개의 노드를 선택해서 현재 이 두 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘
// Kruskal 알고리즘에서 사이클이 존재하는 지 판단할 때 사용됨

// 부모의 값을 찾는 함수
function getParent(parent, x) {
  if (parent[x] === x) return x;
  return (parent[x] = getParent(parent, parent[x]));
}

// 각 부모 노드를 합침 ( 더 작은 값쪽으로 )
function unionParent(parent, a, b) {
  a = getParent(parent, a);
  b = getParent(parent, b);

  if (a < b) parent[b] = a;
  else parent[a] = b;

  return parent;
}

// 같은 부모노드를 가지는지 확인 ( 사이클을 형성하는지 확인 )
function findParent(parent, a, b) {
  a = getParent(parent, a);
  b = getParent(parent, b);

  if (a === b) return true;
  return false;
}
