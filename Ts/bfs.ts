/* ================================================================== */
/* ========================= 1) BFS: TREE ============================ */
/* ================================================================== */

export type TreeNode = {
  value: number;
  left: TreeNode | null;
  right: TreeNode | null;
};

/**
 * BFS (Level Order Traversal) for a binary tree.
 * Visits nodes level by level using a queue (FIFO).
 */
export const bfsTree = (root: TreeNode | null): number[] => {
  if (!root) return [];

  const queue: TreeNode[] = [root];  // nodes waiting to be processed
  const result: number[] = [];       // visited values in BFS order

  while (queue.length > 0) {
    const node = queue.shift()!;     // dequeue (FIFO)
    result.push(node.value);         // visit

    // enqueue children (next level)
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }

  return result;
};

/* ================================================================== */
/* ======================== 2) BFS: MATRIX =========================== */
/* ================================================================== */

/**
 * BFS for a matrix (grid).
 * Each cell (r,c) is a node; neighbors are up/down/left/right.
 * Starts from (0,0). Uses `visited` to avoid revisiting cells.
 */
export const bfsMatrix = (matrix: number[][]): number[] => {
  const rows = matrix.length;
  if (rows === 0) return [];
  const cols = matrix[0].length;
  if (cols === 0) return [];

  const result: number[] = [];
  const visited: boolean[][] = Array.from({ length: rows }, () => Array(cols).fill(false));

  const dirs: [number, number][] = [
    [1, 0],  // down
    [-1, 0], // up
    [0, 1],  // right
    [0, -1], // left
  ];

  const queue: [number, number][] = [[0, 0]];
  visited[0][0] = true;

  while (queue.length > 0) {
    const [r, c] = queue.shift()!;
    result.push(matrix[r][c]);

    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;

      // bounds + visited check
      if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
      if (visited[nr][nc]) continue;

      visited[nr][nc] = true;
      queue.push([nr, nc]);
    }
  }

  return result;
};

/* ================================================================== */
/* ==================== 3) BFS: GRAPH (Adj List) ===================== */
/* ================================================================== */

/**
 * BFS for a graph represented as an adjacency list.
 * graph[v] = list of neighbors of vertex v
 */
export const bfsGraph = (graph: number[][], start: number): number[] => {
  const visited: boolean[] = Array(graph.length).fill(false);
  const result: number[] = [];

  const queue: number[] = [start];
  visited[start] = true;

  while (queue.length > 0) {
    const v = queue.shift()!;
    result.push(v);

    for (const neighbor of graph[v]) {
      if (visited[neighbor]) continue;
      visited[neighbor] = true;
      queue.push(neighbor);
    }
  }

  return result;
};
