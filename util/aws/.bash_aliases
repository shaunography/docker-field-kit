### aws ###
aws-role-assumer() {
    # get role information
    read -p 'enter role arn: ' role_arn
    read -p 'enter role session name: ' role_session_name
    read -p 'enter profile to use: ' profile_name

    # call role assumption
    temp_role=$(aws sts assume-role --role-arn $role_arn --role-session-name $role_session_name --profile $profile_name)

    # update aws configuration
    # export variables
    export AWS_ACCESS_KEY_ID=$(echo $temp_role | jq -r .Credentials.AccessKeyId)
    export AWS_SECRET_ACCESS_KEY=$(echo $temp_role | jq -r .Credentials.SecretAccessKey)
    export AWS_SESSION_TOKEN=$(echo $temp_role | jq -r .Credentials.SessionToken)

    # create new profile in config
    aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID --profile $role_session_name
    aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY --profile $role_session_name
    aws configure set aws_session_token $AWS_SESSION_TOKEN --profile $role_session_name
}

aws-mfa-session() {
    # get role information
    read -p 'Enter MFA ARN: ' mfa_arn
    read -p 'Enter MFA Token: ' token
    read -p 'Enter Profile to use: ' profile_name

    # call role assumption
    session=$(aws sts get-session-token --serial-number $mfa_arn --token-code $token --profile $profile_name)

    # update aws configuration
    # export variables
    export AWS_ACCESS_KEY_ID=$(echo $session | jq -r .Credentials.AccessKeyId)
    export AWS_SECRET_ACCESS_KEY=$(echo $session | jq -r .Credentials.SecretAccessKey)
    export AWS_SESSION_TOKEN=$(echo $session | jq -r .Credentials.SessionToken)

    # create new profile in config
    aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID --profile mfa
    aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY --profile mfa
    aws configure set aws_session_token $AWS_SESSION_TOKEN --profile mfa
}

