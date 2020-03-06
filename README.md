# TradSessions.ie

**Non-tech: A platform for finding, sharing and reviewing Irish traditional music sessions.**

**Tech: A completely serverless, infrastructure-as-code, web application with enterprise standard infrastructure, management and deployment capable of scaling to millions of users and hundreds of developers while maintaining exceptional cost effectiveness and security.**

## Frontend

<img src="Readme/TradSessions.ie - Home.jpg" width="210" style="margin-right:5px"> <img src="Readme/TradSessions.ie - Login.jpg" width="210"> <img src="Readme/TradSessions.ie - Profile.jpg" width="210"> <img src="Readme/TradSessions.ie - Create.jpg" width="210">

The frontend is a mobile-first single page application built using Vue.js. It uses Vuex to manage state, Axios to to call API's and Nuxt.js to pre-render pages server-side to improve SEO and initial load time.


## Backend

### Infrastructure

<img src="Readme/TradSessions.ie - Infrastructure.png">

* The backend is an all AWS, serverless, infrastructure-as-code architecture. The static frontend content is stored in S3 and distributed through Cloudfront which increases speed but also handles the SSL certificate provided Amazon Certificate manager. 
* The static javascript then calls API's from the users browser to fill any dynamic content. 
* API Gateway exposes a public API that triggers a lambda funtion that processes the request and returns content from the DynamoDB NoSQL Database. 
* When the user wants to access private data they are asked to sign in which is done using Amazon Cognito. 
* Once signed up and logged in Amazon Cognito returns a JWT Token that can be used to access the private API and in turn the Lambda function and DynamoDB database behind it.

### Management

<img src="Readme/TradSessions.ie - Management.png">

* The main architecture is completely deployed through CloudFormation. This helps to make infrastructure changes in a structured and consistent way and provides a strategy for a Disaster Recovery Situation where the template could immediately be deployed in another availability zon or region.
* CloudWatch Events are configured on all frontend facing services monitoring error numbers and alerting me via email using Amazon SNS if the number of errors breaks a certain threshold.
* AWS Backup is used to schedule regular backups of the Prod environment DynamoDB data.
* GuardDuty is enabled to provide intelligent threat analysis on everything happening in the account and notify me if anything looks suspicious.
* The CloudWatch alarms, the DynamoDB Backup plan and the GuardDuty Threat Detection were implemented manually in the console and are not included in the Cloudformation template. This is because I was only concerned about configuing these 3 for the Prod environment and not for Dev and Test.

### Deployment

<img src="Readme/TradSessions.ie - Deployment.png">

* For the packaging and Dev environment deployment of the app I'm using AWS Severless Application Model (SAM). SAM makes the CloudFormation template much simpler and makes the deployement of your code and resources to your AWS account only 2 commands away: "sam build && sam deploy". This command returns the API URLs and resource IDs necessary to plug it into your localhost frontend for testing as you develop.
* For the Test and Prod environments I built a fully automated CI/CD Pipeline.
    * Whenever code is pushed to this Github Repo AWS CodePipeline automatically pulls it from here and triggers a pipeline release with the package.
    * It is first sent to AWS CodeBuild to be compiled and checked for any errors.
    * It's then sent to AWS CodeDeploy which creates a CloudFormation Change Set and deploys the code and infrastructure changes to the Test environment
    * After the code as been tested in the Test environment I can then hit Approve in CodePipline and it will release the package to Prod.
* The Pipeline is itself deployed through CloudFormation aswell so changes can be done in a strutured, consistent way and it is easily replicated.

Drawing kudos to the amazing https://cloudcraft.co
