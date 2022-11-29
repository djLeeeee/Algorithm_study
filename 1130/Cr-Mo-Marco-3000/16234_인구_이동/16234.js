let [order, ...g] = require("fs")
  .readFileSync("input.txt")
  // .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")

const math = Math
const dr = [-1, 0, 1, 0]
const dc = [0, 1, 0, -1]

const [N, L, R] = order.split(" ").map((x) => parseInt(x))

g = g.map((x) => x.split(" ").map((x) => parseInt(x)))

let day = 0

let flag = true

while (flag) {
  flag = false
  day++
  const visited = new Array(N).fill().map(() => new Array(N).fill(0))

  const stack = []

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      let sum = 0
      if (!visited[i][j]) {
        // 셈용 초기화
        stack.push([i, j])

        sum += g[i][j]

        visited[i][j] = 1

        Q = [[i, j]]

        while (Q.length) {
          const [r, c] = Q.shift()
          for (let w = 0; w < 4; w++) {
            const nr = r + dr[w]
            const nc = c + dc[w]
            if (
              0 <= nr &&
              nr < N &&
              0 <= nc &&
              nc < N &&
              !visited[nr][nc] &&
              math.abs(g[r][c] - g[nr][nc]) <= R &&
              math.abs(g[r][c] - g[nr][nc]) >= L
            ) {
              visited[nr][nc] = 1
              stack.push([nr, nc])
              Q.push([nr, nc])
              sum += g[nr][nc]
            }
          }
        }
      }
      if (stack.length >= 2) {
        flag = true
      }
      const population = parseInt(sum / stack.length)
      while (stack.length) {
        const [m, n] = stack.pop()
        g[m][n] = population
      }
    }
  }
}

console.log(day - 1)
