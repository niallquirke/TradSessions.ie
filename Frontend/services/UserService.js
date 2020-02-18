import {
  CognitoUserPool,
  CognitoUserAttribute,
  AuthenticationDetails,
  CognitoUser
} from 'amazon-cognito-identity-js'

const poolData = {
  UserPoolId: 'eu-west-1_qwy9mxF19',
  ClientId: '6g7ob7m7fbl35b5kkletv5iskq'
}
const userPool = new CognitoUserPool(poolData)

export default {
  signup(user) {
    const dataEmail = { Name: 'email', Value: user.email }
    const dataUsername = { Name: 'preferred_username', Value: user.username }
    const attributeEmail = new CognitoUserAttribute(dataEmail)
    const attributeUsername = new CognitoUserAttribute(dataUsername)
    return new Promise((resolve, reject) =>
      userPool.signUp(
        user.email,
        user.password,
        [attributeEmail, attributeUsername],
        null,
        (err, result) => {
          if (err) {
            reject(err)
          } else {
            resolve(result.user)
          }
        }
      )
    )
  },
  login(user) {
    const authenticationDetails = new AuthenticationDetails({
      Username: user.email,
      Password: user.password
    })
    const userData = { Username: user.email, Pool: userPool }
    const cognitoUser = new CognitoUser(userData)
    return new Promise((resolve, reject) =>
      cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: (result) => {
          resolve(result)
        },
        onFailure: (err) => {
          alert(err.message || JSON.stringify(err))
          reject(err)
        }
      })
    )
  },
  logout() {
    return new Promise((resolve, reject) => {
      try {
        userPool.getCurrentUser().signOut()
        resolve()
      } catch (error) {
        reject(error)
      }
    })
  }
}
