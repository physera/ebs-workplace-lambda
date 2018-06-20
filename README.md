# ebs-workplace-lambda
This repo contains some simple lambda functions for creating an AWS-FB Workplace integration. 

## Implementation Notes
* Set up a workplace integration with 'manage group' permissions (for posting to a group) or 
'message any member' and 'allow this integration to work in group chats' (for posting to a chat thread).  
You'll need to be a workplace system administrator to do this, or you'll need to be on good speaking terms with 
someone who is, even if they recently spilled coffee on your shoes. 
* If desired, initialize the chat thread using the ``setup.py`` script in order to get the thread_id your bot will post to.
* Set up an lambda function that is subscribed to the appropriate SNS alerts.  
* Add the access token and group_id/thread_id to the environment variables of your lambda function. 

## Version History
* 2018-06-18 Initial Release

