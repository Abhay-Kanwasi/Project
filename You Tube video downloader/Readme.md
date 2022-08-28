# Youtube Video downloder

__Objective__

Download the youtube video and explore the Youtube library.

<br />

__Requirements__
<br />
1. from pytube library import YouTube.
2. link of a Youtube video.

<br />

__Procedure__

First we create a variable name link = "provide the link of Youtube video" then make a youtube_1 object for YouTube class and pass link variable to the Youtube classs.
Now we explore the YouTube library diffrent methods like title,publish_date,author,age_restricted,thumbnail_url.

We just simply say youtube_1.give the method name.(i.e Title : youtube_1.title)

<br />

Then we print all the availabe strems of video with the help of streams.all() and store it into a variable name videos and because we want it in a list format we use list casting and also want numbers in first for counting we use enumerate and pass videos to it.

<br />

__download youtube video__
first we ask for stream which stream we want to download our video then then we say "videos[stream].download" it will download the video. Then we write a message when our youtube video successfully downloaded.

