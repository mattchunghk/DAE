{
    "User": {
        "Path": "/",
        "UserName": "c22-dae",
        "UserId": "AIDATSOD7OL55OWP2NJ5Q",
        "Arn": "arn:aws:iam::245761012475:user/c22-dae",
        "CreateDate": "2022-11-02T04:27:57+00:00"
    }
},
{
    "AccessKey": {
        "UserName": "c22-dae",
        "AccessKeyId": "AKIATSOD7OL5QPLKXRON",
        "Status": "Active",
        "SecretAccessKey": "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",
        "CreateDate": "2022-11-02T04:28:18+00:00"
    }
},
aws s3 mb s3://c22-openrice --region ap-northeast-1
tee -a read_s3.json << EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1546023631000",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:ListBucket",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::c22-openrice",
                "arn:aws:s3:::c22-openrice/*"
            ]
        }
    ]
}
EOF
{
    "PolicyNames": [
        "read_s3_as_datalake"
    ]
}

aws iam put-user-policy --user-name c22-dae --policy-name read_s3_as_datalake --policy-document file://read_s3.json 

aws iam list-user-policies --user-name c22-dae
aws iam get-user-policy --user-name c22-dae  --policy-name read_s3_as_datalake

{
    "UserName": "c22-dae",
    "PolicyName": "read_s3_as_datalake",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt1546023631000",
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:DeleteObject",
                    "s3:ListBucket",
                    "s3:PutObject"
                ],
                "Resource": [
                    "arn:aws:s3:::c22-dae",
                    "arn:aws:s3:::c22-dae/*"
                ]
            }
        ]
    }
}