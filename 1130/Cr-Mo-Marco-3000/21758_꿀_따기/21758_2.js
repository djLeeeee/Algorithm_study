let [N, input] = require("fs")
  // .readFileSync("/dev/stdin")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")

N = parseInt(N)

input = input.split(" ").map((x) => parseInt(x))

g = new Array(N).fill().map(() => [0, 0])

let ans = 0

for (let i = 0; i < N; i++) {
  g[i][0] = (g[i - 1]?.[0] || 0) + input[i]
  g[N - i - 1][1] = (g[N - i]?.[1] || 0) + input[N - i - 1]
}

// 그리디 풀이법
// 벌통이 중간에 있을 때, 무조건 벌이 양 끝단에 있어야 최대
for (let mid = 1; mid < N - 1; mid++) {
  const honey = g[mid][0] - g[0][0] + g[mid][1] - g[N - 1][1]
  if (honey > ans) {
    ans = honey
  }
}

// 벌통이 한쪽으로 몰려 있다면, 벌통과 다른 벌들 중 하나가 각각 끝에 몰려 있어야 최대
// 각각 좌과 우측으로 나눈다
for (let bee = 1; bee < N - 1; bee++) {
  const honey = g[0][1] - g[N - 1][1] - input[bee] + g[0][1] - g[bee][1]
  if (honey > ans) {
    ans = honey
  }
}
for (let bee = 1; bee < N - 1; bee++) {
  const honey = g[N - 1][0] - g[0][0] - input[bee] + g[N - 1][0] - g[bee][0]
  if (honey > ans) {
    ans = honey
  }
}

console.log(ans)
