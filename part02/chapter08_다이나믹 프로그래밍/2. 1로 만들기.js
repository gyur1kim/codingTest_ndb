/*
 * 연산 4개를 적절히 사용해서 1을 만드는데,,, 연산을 최소로 하세요.
 *
 * 1. X가 5로 나누어떨어지면, 5로 나눈다.
 * 2. X가 3으로 나누어떨어지면, 3으로 나눈다.
 * 3. X가 2로 나누어떨어지면, 2로 나눈다.
 * 4. X에서 1을 뺀다.
 *
 * 아 헐 DP맞네...
 *
 */

function solution(x) {
  // 각 숫자의 최소 연산 횟수를 저장해두는 배열입니다.
  const dp = [0, 0];

  for (let i=2; i<=x; i++) {
    // case1. 이전 값에서 1을 더하는 게 가장 연산 횟수가 적다고 정해둡니다.
    dp.push(dp[i-1] + 1)
    // case2. 이전 값에서 1을 더하는 게 적을까요! 아니면 2배 한 게 적을까요! 연산 횟수를 비교합니다.
    if (i%2 === 0) {
      dp[i] = Math.min(dp[i], dp[i/2] + 1)
    }
    // case3. 현재 dp[i]에 있는 연산횟수가 적을까요! 아니면 3배 한 게 적을까요! 연산 횟수를 비교합니다.
    if (i%3 === 0) {
      dp[i] = Math.min(dp[i], dp[i/3] + 1)
    }
    // case4. 현재 dp[i]에 있는 연산횟수가 적을까요! 아니면 5배 한 게 적을까요! 연산 횟수를 비교합니다.
    if (i%5 === 0) {
      dp[i] = Math.min(dp[i], dp[i/5] + 1)
    }
  }

  return dp[x]
}

console.log(solution(26))