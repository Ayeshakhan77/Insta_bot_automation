from instabot import Bot 
bot = Bot()
bot.login(username="@username", password="1234")
bot.follow('canva')
bot.upload_photo("C:/Users/CSP/Desktop/flowers.jpg",caption="Spring season")
bot.unfollow("canva")
bot.send_message("i love python", ["username1","username2","username3"])
followers=bot.get_user_followers("@username")
for follower in followers:
     print(bot.get_user_info(follower))
following=bot.get_user_following("@username")
for Following in following:
    print(bot.get_user_info(Following))