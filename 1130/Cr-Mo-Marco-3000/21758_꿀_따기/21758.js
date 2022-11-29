let [N, input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

N = parseInt(N)

const math = Math

input = input.split(" ").map((x) => parseInt(x))

g = new Array(N).fill().map(() => [0, 0])

let ans = 0

for (let i = 0; i < N; i++) {
  g[i][0] = (g[i - 1]?.[0] || 0) + input[i]
  g[N - i - 1][1] = (g[N - i]?.[1] || 0) + input[N - i - 1]
}

// combination
for (let i = 0; i < N - 2; i++) {
  for (let j = i + 1; j < N - 1; j++) {
    for (let k = j + 1; k < N; k++) {
      // 경우 1 => 맨 왼쪽이 벌통일 경우,
      const left = 2 * (g[i][1] - g[j][1]) + g[j + 1][1] - g[k][1]
      const mid = g[j][0] - g[i][0] + g[j][1] - g[k][1]
      const right = 2 * (g[k][0] - g[j][0]) + g[j - 1][0] - g[i][0]
      const tempMax = math.max(left, mid, right)
      if (tempMax > ans) {
        ans = tempMax
      }
    }
  }
}

console.log(ans)
