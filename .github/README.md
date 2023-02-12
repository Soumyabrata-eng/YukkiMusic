<img src="https://telegra.ph/file/c0e014ff34f34d1056627.png" align="right" width="200" height="200"/>

# Yukki Music Bot

[Yukki Music Bot](https://github.com/TeamYukki/YukkiMusicBot) is a Powerful Telegram Music+Video Bot written in Python using Pyrogram and Py-Tgcalls by which you can stream songs, video and even live streams in your group calls via various sources.

* Youtube, Soundcloud, Apple Music, Spotify, Resso and Telegram Audios & Videos support.
* Written from scratch, making it stable and less crashes.
* Attractive thumbnails, fonts and images,  making experience more user-friendly and interactive.
* Loop, Seek, Shuffle, Specific Skip, Playlists etc support
* Global, Users, Chats Top 10 played tracks stats
* Multi-Language support

# 🔗 An Overview

Here's a brief high-level overview of the Yukki Music Bot:

This project is based on [Pyrogram](https://github.com/pyrogram) and [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls) . Pyrogram is a modern, elegant and asynchronous MTProto API framework.

* For database, Yukki uses the MongoDB to store data and keys. [MongoDB](https://www.mongodb.com/) is a document database with the scalability and flexibility that you want with the querying and indexing that you need.
* Project uses the bs4 web scrapping for getting many platform details. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files.
* The project uses the font [`Raleway`](../assets/font2.ttf) as its main font for the thumbnails.
* The projects uses attractive images and icons which you can get in [assets](../assets/) directory.

# ⚡️ Getting Started

### Before deploying Yukki Music Bot , please have a look towards [all available config vars](../config/README.md) , also please check [all available commands](../strings/command.yml) of the project.

> If you want to start working with Yukki Music Bot you can either fork or import repo .
> The official [documentation site](https://notreallyshikhar.gitbook.io/yukkimusicbot/) contains a lot of information. The best place to start is from the deployment section.
> If you'd like to talk to us, join us on our [Telegram Group](https://t.me/YukkiSupport)

## 🖇 Prerequisites

> In order to avoid conflicts in your project, you must have/installed
- [Python3.9](https://www.python.org/downloads/release/python-390/)
- [Telegram API Key](https://docs.pyrogram.org/intro/setup#api-keys)
- [Telegram Bot Token](https://t.me/botfather)

## 🚀 Heroku Deployment

<h4>Click the button below to deploy Yukki on Heroku!</h4>    
<a href="https://yukki.tech/deploy/"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a>

## 🖇 VPS Deployment

```console
$Soumyabrata/Yukki~ $ sudo apt-get update && sudo apt-get upgrade -y
$Soumyabrata/Yukki~ $ sudo apt-get install python3-pip ffmpeg -y
$Soumyabrata/Yukki~ $ sudo pip3 install -U pip
$Soumyabrata/Yukki~ $ curl -fssL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install nodejs -y && npm i -g npm
$Soumyabrata/Yukki~ $ sudo apt install git
$Soumyabrata/Yukki~ $ git clone https://github.com/Soumyabrata-eng/YukkiMusic && cd YukkiMusic
$Soumyabrata/Yukki~ $ pip3 install -U -r requirements.txt

Edit the variables by <code>vi sample.env</code> and then click <code>CTRL+C</code> and :wq to save env.

$Soumyabrata/Yukki~ $ cp sample.env .env
$Soumyabrata/Yukki~ $ sudo apt install tmux && pkill -9 tmux && pkill -9 python3 && tmux
$Soumyabrata/Yukki~ $ bash start
```
## 🏷 Support

Reach out to the maintainer at one of the following places:

- [GitHub Issues](https://github.com/TeamYukki/yukkimusicbot/issues/new?assignees=&labels=question&template=SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/TeamYukki)
- [Telegram Support](https://t.me/YukkiSupport)

## 🎗 Project assistance

If you want to say **thank you** or/and support active development of YukkiMusicBot:

- Add a [GitHub Star](https://github.com/TeamYukki/YukkiMusicBot) to the project.
- Fork the Repo :)
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

## ✍🏻 Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](CONTRIBUTING.md), and thank you for being involved!

## 👨🏻‍💻 Authors & contributors

The original setup of this repository is by [Team Yukki](https://github.com/TeamYukki).

For a full list of all authors and contributors, see [the contributors page](https://github.com/TeamYukki/YukkiMusicBot/contributors).
