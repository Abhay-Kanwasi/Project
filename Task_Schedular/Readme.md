# Task Scedular

> The Task Scheduler enables you to automatically perform routine tasks on a chosen computer. Task Scheduler does this by monitoring whatever criteria you choose (referred to as triggers) and then executing the tasks when those criteria are met.Scheduling is important art of planning your activities so that you can achieve your goals and priorities in the time you have available. When it's done effectively, it helps you: Understand what you can realistically achieve with your time. Make sure you have enough time for essential tasks.

We are creating a task scedular for a desktop notification that will be take input parameters from the user about how many days of scheduling and what is the time for that.


## Module Required
* `datetime`
* `time`
* `schedule`


## Methadology 

The basic idea is that we have python script running all the time and then we have certain tasks or functions we want to execute on a regular basis it can be everyday,everyminute,everysecond,everyday at a certain time. All of this is easy using `schedule` module. All of this is related to time so we use one more module `datetime`