aws iam create-user --user-name Developer01

aws iam create-group --group-name Developers

aws iam add-user-to-group --user-name Developer01 --group-name Developers

aws iam get-group --group-name Developers

vim iam.json
{
	"Statement": 
	{
		"Effect": "Allow",
		"Principal": {"Service": "ec2.amazonaws.com"},
		"Action": "sts:AssumeRole"
	} 
}

aws iam create-role --role-name iamrole --assume-role-policy-document file://iam.json

aws iam get-role --role-name iamrole

vim s3readonly.json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect":"Allow",
			"Action": [
				"s3:Get*",
				"s3:List*"
			],
			"Resource": "arn:aws:s3:::12291034-random-bucket",
			"Condition": {
				"IpAddress": {
					"aws:SourceIp": "10.0.0.0/16"
				}
			}
		}
	]
}

aws iam create-policy --policy-name s3readonly --policy-document file://s3readonly.json
