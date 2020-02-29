import {
  CognitoUserPool,
  CognitoUserAttribute,
  AuthenticationDetails,
  CognitoUser
} from 'amazon-cognito-identity-js'
import endpoints from '@/cloud.config'

const poolData = {
  UserPoolId: endpoints.UserPoolID,
  ClientId: endpoints.UserPoolClientID
}
const userPool = new CognitoUserPool(poolData)

export default {
  signup(user) {
    const dataEmail = { Name: 'email', Value: user.email }
    const attributeEmail = new CognitoUserAttribute(dataEmail)
    return new Promise((resolve, reject) =>
      userPool.signUp(
        user.username,
        user.password,
        [attributeEmail],
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
