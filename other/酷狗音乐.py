import urllib.request
import re
import requests

from lxml import etree


def get_song_url_list(rank_url):
    response = requests.get(rank_url)
    tree = etree.HTML(response.text)
    return tree.xpath('//div[@id="rankWrap"]//ul//a[@data-active="playDwn"]/@href')


def get_hash_and_id(song_url):
    response = requests.get(url=song_url)
    text = response.text
    hash_list = re.findall('"hash":"(.*?)"', text)
    id_list = re.findall('"album_id":(\d+)', text)
    return hash_list[0], id_list[0]


def get_download_url_and_name(hash_and_id):
    url = f"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hash_and_id[0]}&dfid=4FIHWS4Dn3X02ZlVgd1EDsFC&appid=1014&mid=7722cc659527b0e54d4993ec8ec2587b&platid=4&album_id={hash_and_id[1]}"
    response = requests.get(url)
    json = response.json()
    return json["data"]["play_backup_url"], json["data"]["song_name"]


def save_song(download_url_and_name):
    urllib.request.urlretrieve(download_url_and_name[0],
                               f"D:/MyPython/MyProject_1/music/{download_url_and_name[1]}.mp3")
    print(download_url_and_name[1] + "       下载好了")


def main():
    rank_url = "https://www.kugou.com/yy/rank/home/1-33163.html"
    song_url_list = get_song_url_list(rank_url)

    for song_url in song_url_list:
        hash_and_id = get_hash_and_id(song_url)
        download_url_and_name = get_download_url_and_name(hash_and_id)
        save_song(download_url_and_name)


main()



















