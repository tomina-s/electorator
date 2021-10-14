export default function authHeader() {
  let account = JSON.parse(localStorage.getItem('account'))

  if (account && account.jwt) {
    return { Authorization: 'Token ' + account.jwt }
  } else {
    return {}
  }
}