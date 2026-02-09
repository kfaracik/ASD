/**
 * MinHeap (binary heap)
 *
 * - Complete binary tree stored in an array.
 * - Index math:
 *    parent(i) = floor((i - 1) / 2)
 *    left(i)   = 2*i + 1
 *    right(i)  = 2*i + 2
 * - Min-heap property: each parent <= its children.
 *
 * Operations:
 *  - insert:  O(log n)
 *  - remove:  O(log n)  (removes and returns min)
 *  - peek:    O(1)
 *  - replace: O(log n)  (swap root with new value, return old root)
 */
class MinHeap {
  #heap = [];
  #maxSize;

  /**
   * @param {number} [maxSize] Optional capacity limit.
   */
  constructor(maxSize) {
    this.#maxSize = Number.isFinite(maxSize) ? maxSize : undefined;
  }

  // --- index helpers ---
  #leftChild(index) {
    return 2 * index + 1;
  }

  #rightChild(index) {
    return 2 * index + 2;
  }

  #parent(index) {
    return Math.floor((index - 1) / 2);
  }

  #swap(i, j) {
    [this.#heap[i], this.#heap[j]] = [this.#heap[j], this.#heap[i]];
  }

  // --- public helpers ---
  size() {
    return this.#heap.length;
  }

  isEmpty() {
    return this.#heap.length === 0;
  }

  peek() {
    return this.#heap.length === 0 ? null : this.#heap[0];
  }

  // --- core operations ---
  insert(value) {
    if (this.#maxSize !== undefined && this.#heap.length >= this.#maxSize) {
      throw new Error("MinHeap capacity exceeded");
    }

    this.#heap.push(value);
    this.#bubbleUp(this.#heap.length - 1);
  }

  remove() {
    if (this.#heap.length === 0) return null;
    if (this.#heap.length === 1) return this.#heap.pop();

    const minValue = this.#heap[0];
    this.#heap[0] = this.#heap.pop(); // move last to root
    this.#sinkDown(0);
    return minValue;
  }

  /**
   * Replace the root (min) with a new value in one pass.
   * @returns {number|null} previous min (or null if heap was empty)
   */
  replace(value) {
    if (this.#heap.length === 0) {
      this.#heap.push(value);
      return null;
    }

    const minValue = this.#heap[0];
    this.#heap[0] = value;
    this.#sinkDown(0);
    return minValue;
  }

  // --- internal maintenance ---
  #bubbleUp(index) {
    let current = index;

    while (current > 0) {
      const p = this.#parent(current);
      if (this.#heap[current] >= this.#heap[p]) break; // reversed vs MaxHeap
      this.#swap(current, p);
      current = p;
    }
  }

  #sinkDown(index) {
    let current = index;
    const n = this.#heap.length;

    while (true) {
      const left = this.#leftChild(current);
      const right = this.#rightChild(current);

      let smallest = current;

      if (left < n && this.#heap[left] < this.#heap[smallest]) {
        smallest = left;
      }
      if (right < n && this.#heap[right] < this.#heap[smallest]) {
        smallest = right;
      }

      if (smallest === current) break;
      this.#swap(current, smallest);
      current = smallest;
    }
  }
}
