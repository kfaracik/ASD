/**
 * Merge two sorted arrays into a single sorted array.
 */
function merge(left: number[], right: number[]): number[] {
  const combined: number[] = [];
  let i = 0;
  let j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      combined.push(left[i]);
      i++;
    } else {
      combined.push(right[j]);
      j++;
    }
  }

  while (i < left.length) {
    combined.push(left[i]);
    i++;
  }

  while (j < right.length) {
    combined.push(right[j]);
    j++;
  }

  return combined;
}

/**
 * Returns a new sorted array (ascending) using merge sort.
 * Does not mutate the input.
 */
export function mergeSort(array: number[]): number[] {
  if (array.length <= 1) return array.slice();

  const mid = Math.floor(array.length / 2);
  const left = mergeSort(array.slice(0, mid));
  const right = mergeSort(array.slice(mid));

  return merge(left, right);
}
