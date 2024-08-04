// Install TypeScript (if not already installed):
// bash
// npm install -g typescript

const printArray = <T>(arr: T[]): void => {
arr.forEach( element => console.log(element));
}

// Example usage:
printArray([1, 2, 3]); // Should print each number on a new line
printArray(["a", "b", "c"]); // Should print each string on a new line
printArray([true, false, true]); // Should print each boolean on a new line