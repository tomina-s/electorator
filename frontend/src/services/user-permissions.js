export default function getPermissions() {
  let account = JSON.parse(localStorage.getItem('account'))

  if (account && account.permissions) {
    return account.permissions
  }
}