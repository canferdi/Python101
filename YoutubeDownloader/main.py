from pytube import YouTube

url = input("Enter url: ")
yt = YouTube(url)

select = int(input("Select video quality : \n"
                   "1- Low quailty\n"
                   "2- High quailty\n"))
if(select == 1):
    yt.streams.get_lowest_resolution().download()
elif(select == 2):
    yt.streams.get_highest_resolution().download()
print("Download complete")