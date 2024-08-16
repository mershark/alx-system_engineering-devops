*POSTMORTEM* 


Start : 1/08/2024, 4:AM end : 14/08/2024, 4:PM

 *IMPACT:* 

What service was down/slow? The whole application running on PHP 7 crashed during this time lapse. What were users experiencing? Users were unable to connect into their accounts , those who were already connected were unable to send any requests (messages) How many % of the users were affected? Almost 100% of the users have been affected by this downtime error. what was the root cause The root cause of the error is an update made into production environment while some methods were still dependent to previous development stack (PHP 7, apache 5)

 *TIMELINE:* 

When was the issue detected The issue has been detected the 10/07/2023 at 2:0pAM How was the issue detected The issue was detected via the application deployment log which was displaying dependencies alert.

 *ACTIONS TAKEN:* 

In order to solve the issue, we proceeded to a rollback of the application development state.

 *Misleading investigation/debugging paths that were taken;* 

We first tried to convert methods and variables concerned to the new version which
has led to complications.

 *Which team/individuals;* 

The incident escalated to developers team.

 *How the incident was resolved;* 

Incident was resolved via rollback on the server to the previous application state. It made new users lose their accounts but it was the best solution.

 *Root cause and resolution;* 

What was causing the issue was because Someone tried to upgrade his local development stack onto the next version but unfortunately he turned up to be upgrading the overall production environment . His error passed without devOps noticing it then the clients started facing errors to connect or send requests using the methods concerned by the upgrade. 

 *How the issue was fixed;* 

As explained earlier, the issue has been fixed via a complete rollback of the application including data to the previous state.
To be more accurate, we have automated a backup for the application each day at 23:59 PM.

 *Corrective and preventative measures:* 

We have Set developers' local environment with docker containers so they can do whatever they want without affecting the global system.

 *Ways to address the issue;* 

Read log files Fix logs where error has been shown Locate concerned files Identify the current error (“deprecated and unused methods”) message Tried to update the methods whereas users were deferred on the backup server from the app file of 01:02 reset the whole app state to 01/02￼Enter
