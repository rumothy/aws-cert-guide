// set the AWS variable for the SDK
var AWS = require('aws-sdk');
console.log('hello from ex2');

// define the AWS region as us-east-2
AWS.config.update({region:'us-east-2'});

// source the credentials from the .aws/credentials file in your home directory
var credentials = AWS.SharedIniFileCredentials({profile: 'default'});
AWS.config.credentials = credentials;

// Create the EC2 definition
var ec2 = new AWS.EC2({apiVersion: '2016-11-15'});
var instanceParams = {
    ImageId: 'ami-0d8f6eb4f641ef691',
    InstanceType: 't3.small',
    KeyName: 'mykeypair',
    MinCount: 1, 
    MaxCount: 1
};

// define a promise for the EC2 instance
var instancePromise = new AWS.EC2({apiVersion: '2016-11-15'}).runInstances(instanceParams).promise();

// define the error handling for the EC2 promise
instancePromise.then(
    function(data) {
        console.log(data);
        var instanceId = data.Instances[0].InstanceId;
        console.log("Created instance", instanceId);
    });