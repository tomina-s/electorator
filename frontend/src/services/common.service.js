function getRole() {
  let account = JSON.parse(localStorage.getItem('account'))

  if (account && account.role) {
    return account.role
  }
}

function getPermissions() {
  let account = JSON.parse(localStorage.getItem('account'))

  if (account && account.permissions) {
    return account.permissions
  }
}

function getUIKPermission() {
  const perm = getPermissions()
  const role = getRole()

  if (role === "УИК" && perm.length !== 0) {
    return perm[0]
  }
}

export {getPermissions, getUIKPermission, getRole}