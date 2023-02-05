# Desktop Notifer 

Here we will created an notifer for our desktop for a specific purpuse.

### Scenario :
Suppose if we are working whole day and don't take any breaks then it will affect our body so much for avoiding that we want something that notify us to take a break with a message why we must take break.

### Required Modules :
1. time : use for time delay of notifications.
2. plyer : from plyer module we want notification class which will help us to give notification to desktop.

### Working :

Working is simple.. 

First we will import both modules using pip command.

After that we will use notification class and at that class we will give parameters like.. 
1. Title : Title of notification
2. Message : What will be the message in notification.
3. App Icon : What will be the icon of our notification.
4. Timeout : When our notication will stop showing.

After this we will set a loop and each loop will continue it's process with delay of 10 Seconds(Which we will do by using time.sleep(10))

For running this in background properly name file like this :
pythonw<file name>.py

### How to stop notification ?
We are using an infinite loop so notification will not stop.. In that scenario go for: 
Task Manager>>Python>>End Task