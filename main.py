import random

import instaloader
import time
import datetime


il = instaloader.Instaloader()
username = 'bakirov.s'

profile = instaloader.Profile.from_username(il.context, username=username)
posts = profile.get_posts()

print(f'[+] Profile info: {username}\n{profile.biography}'
      f'\nPosts count: {profile.mediacount}'
      f'\nFollowers: {profile.followers}\n\n'
      )

# print(posts, type(posts))

count = 0
for post in posts:
    count += 1
    print(f'[+] step {count}: downloading ... ', end='')
    il.download_post(post, target=f'{username}_all_posts')
    time.sleep(random.randrange(4, 9)) #увеличиваем время между загрузками, чтобы нас не забанила система инсты

print(f'[+] Done!', datetime.datetime.now())
