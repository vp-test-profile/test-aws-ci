import boto3
# CodeBuild
client = boto3.client('codebuild')

# create a build project
response = client.create_project(
    name='test-codebuild',
    description='test ci codeBuild',
    source={
        'type': 'GITHUB',
        'location':"https://github.com/VishnuPrabhas/aws_CB_Demo",
        "gitCloneDepth": 0,        
        "gitSubmodulesConfig": {   
            "fetchSubmodules": True
        },
        "buildspec": "",
        "auth": {
            "type": "OAUTH",       
            "resource": ""
        },
        "reportBuildStatus": True, 
        
        "insecureSsl": True,
        "sourceIdentifier": "NONE"
    },
    
    sourceVersion="main",
   
    artifacts={
        "type": "NO_ARTIFACTS"   
    },
    
    cache={
        "type": "LOCAL",
        "location": "NONE",
        "modes": [
            "LOCAL_CUSTOM_CACHE"
        ]
    },

    environment={
        "type": "LINUX_CONTAINER",
        "image": "aws/codebuild/amazonlinux2-x86_64-standard:4.0",
        "computeType": "BUILD_GENERAL1_SMALL",
        "privilegedMode": False
    },

    serviceRole="arn:aws:iam::269359443853:role/SagemakerDevelopmentRole",
    timeoutInMinutes=60,
    queuedTimeoutInMinutes=60,
    badgeEnabled=True,
    logsConfig={
        "cloudWatchLogs": {
            "status": "DISABLED"    
        }
    },    
    
    concurrentBuildLimit=10
)

# See the list of build project names
buildNames = client.list_projects(
    sortBy='CREATED_TIME',
    sortOrder='DESCENDING'   
) 

# Start Running a build
startBuild = client.start_build(
    projectName='test-codebuild',
     sourceTypeOverride='GITHUB',
    sourceLocationOverride='https://github.com/VishnuPrabhas/aws_CB_Demo',
    sourceAuthOverride={
        'type': 'OAUTH',
        'resource': ''
    },
    gitCloneDepthOverride=0,
    gitSubmodulesConfigOverride={
        'fetchSubmodules': True
    },
    reportBuildStatusOverride=True,
    environmentTypeOverride='LINUX_CONTAINER',
    imageOverride='aws/codebuild/amazonlinux2-x86_64-standard:4.0',
    computeTypeOverride='BUILD_GENERAL1_SMALL',
    cacheOverride={
        'type': 'NO_CACHE',
        'modes': [
            'LOCAL_CUSTOM_CACHE',
        ]
    },
    serviceRoleOverride='arn:aws:iam::269359443853:role/SagemakerDevelopmentRole',
    privilegedModeOverride=False,
    timeoutInMinutesOverride=60,
    queuedTimeoutInMinutesOverride=60,
    logsConfigOverride={
        'cloudWatchLogs': {
            'status': 'DISABLED',
        },    
    },
    imagePullCredentialsTypeOverride='CODEBUILD',
    debugSessionEnabled=True   
)

print(f'Create Build: \n{response}\n')
print('*'*100, '\n')
print(f'Build Project Names: \n{buildNames}\n')
print('*'*100, '\n')
print(f'Start Build: \n{startBuild}\n')
