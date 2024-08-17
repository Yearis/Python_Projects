import Greeting_Message
import requests
print("\nPress:")
print("""1 For General News: General news articles covering a wide range of topics.
2 for Business: News related to business, finance, and the economy.
3 for Entertainment: Articles about movies, television, music, and celebrity news.
4 for Health: Health-related news, including medical research and wellness tips.
5 for Politics: Political news, including local, national, and international politics.
6 for Science: News related to scientific discoveries, research, and technology.
7 for Sports: Coverage of various sports events and updates.
8 for Technology: News about the latest in technology, gadgets, and digital trends.
9 for World: International news covering events and issues from around the globe.\n""")

Topic=int(input("Enter the Number For the News You Want:"))

url=f"https://newsapi.org/v2/everything?q={Topic}&from=2024-07-10&sortBy=publishedAt&apiKey=1e25c62b309a49dda02d9502258ada54"

news=requests.get(url)
print(news.text)