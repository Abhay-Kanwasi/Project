from pytube import YouTube

link = "https://www.youtube.com/watch?v=4Rl8S7stN5A"

youtube_1 = YouTube(link)


print("Title of video : ",youtube_1.title)
print("Publish date of video : ",youtube_1.publish_date)
print("Creator of video : ",youtube_1.author)
print("Age restricted or not : ",youtube_1.age_restricted)
print("Thumnail url of video : ",youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
streaming = list(enumerate(videos))
for i in streaming:
    print(i)
print()

strm = int(input("Enter : "))
videos[strm].download()
print("Succesfully downloded video.")