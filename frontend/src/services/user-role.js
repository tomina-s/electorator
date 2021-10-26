export default function getRole() {
  let account = JSON.parse(localStorage.getItem('account'))

  if (account && account.role) {
    return account.role
  }
}