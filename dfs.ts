/* ================================================================== */
/* ========================= 1) DFS: TREE ============================ */
/* ================================================================== */

export type TreeNode = {
  value: number;
  left: TreeNode | null;
  right: TreeNode | null;
};

/**
 * Depth-First Search (DFS) for a binary tree.
 * Uses a stack to traverse the tree depth-first (preorder).
 *
 * Order: root → left → right
 */
export const dfsTree = (root: TreeNode | null): number[] => {
  if (!root) return [];

  const stack: TreeNode[] = [root];
  const result: number[] = [];

  while (stack.length > 0) {
    const node = stack.pop()!;
    result.push(node.value);

    // Push right first so left is processed first
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }

  return result;
};

/* ================================================================== */
/* ======================== 2) DFS: MATRIX =========================== */
/* ================================================================== */

/**
 * DFS for a matrix (grid).
 * Each cell is treated as a node.
 * Traverses neighbors: up, down, left, right.
 *
 * Starts from (0,0).
 */
export const dfsMatrix = (matrix: number[][]): number[] => {
  const rows = matrix.length;
  if (rows === 0) return [];
  const cols = matrix[0].length;
  if (cols === 0) return [];

  const result: number[] = [];
  const visited: boolean[][] = Array.from(
    { length: rows },
    () => Array(cols).fill(false)
  );

  const dirs: [number, number][] = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  // Stack holds coordinates [row, col]
  const stack: [number, number][] = [[0, 0]];
  visited[0][0] = true;

  while (stack.length > 0) {
    const [r, c] = stack.pop()!;
    result.push(matrix[r][c]);

    // Push neighbors to stack
    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;

      if (
        nr >= 0 &&
        nr < rows &&
        nc >= 0 &&
        nc < cols &&
        !visited[nr][nc]
      ) {
        visited[nr][nc] = true;
        stack.push([nr, nc]);
      }
    }
  }

  return result;
};

/* ================================================================== */
/* ==================== 3) DFS: GRAPH (Adj List) ===================== */
/* ================================================================== */

/**
 * DFS for a graph represented as an adjacency list.
 *
 * graph[v] = list of neighbors of vertex v
 */
export const dfsGraph = (graph: number[][], start: number): number[] => {
  const visited: boolean[] = Array(graph.length).fill(false);
  const result: number[] = [];

  const stack: number[] = [start];

  while (stack.length > 0) {
    const vertex = stack.pop()!;

    if (visited[vertex]) continue;
    visited[vertex] = true;
    result.push(vertex);

    // Push neighbors (reverse order optional, for stable output)
    for (let i = graph[vertex].length - 1; i >= 0; i--) {
      const neighbor = graph[vertex][i];
      if (!visited[neighbor]) {
        stack.push(neighbor);
      }
    }
  }

  return result;
};
