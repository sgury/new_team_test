// App configuration
const config = {
  aws: {
    accessKeyId: "~[AWS_ACCESS_KEY_ID_0]~",
    secretAccessKey: "~[AWS_SECRET_KEY_0]~",
    region: "us-east-1",
    bucket: "~[S3_BUCKET_NAME_0]~"
  },
  twilio: {
    accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    authToken: "your_auth_token_here",
    fromNumber: "~[PHONE_INTL_0]~"
  },
  jwt: {
    secret: "my-super-secret-jwt-key-change-in-production-please",
    expiry: "7d"
  }
};

module.exports = config;
