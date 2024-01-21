# Scrapy settings for pexels project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pexels'

SPIDER_MODULES = ['pexels.spiders']
NEWSPIDER_MODULE = 'pexels.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'pexels (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
'cookie': '_gid=GA1.2.951685644.1658044594; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_171201=eyJpZCI6IjNhYzZiMTQwLTBlMTAtNDU0NC1hYTFjLWZlNTMyODYwNzk2ZCIsImNyZWF0ZWQiOjE2NTgwNDQ1OTQ5MjIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1658044601504.326834959; ab.storage.deviceId.5791d6db-4410-4ace-8814-12c903a548ba=%7B%22g%22%3A%2226cb4845-ab35-ac15-fe35-9ee76cf31473%22%2C%22c%22%3A1658044644203%2C%22l%22%3A1658044644203%7D; locale=en-US; NEXT_LOCALE=en-US; _hjSessionUser_171201=eyJpZCI6ImQ0NGQ4YjkwLTU1OTgtNWFjZS04NGUwLWE4YzU1MjNlNWI2OCIsImNyZWF0ZWQiOjE2NTgwNDQ1OTQ3MjAsImV4aXN0aW5nIjp0cnVlfQ==; ab.storage.sessionId.5791d6db-4410-4ace-8814-12c903a548ba=%7B%22g%22%3A%2286a4b11a-277d-13f8-8352-5645874d2446%22%2C%22e%22%3A1658047528614%2C%22c%22%3A1658044644201%2C%22l%22%3A1658045728614%7D; __cf_bm=KpeO_hHZ44DIY3wiAbEJEGNv2a6XprVdO3rxbLAuqL8-1658050774-0-AQWpyqwN/4NfHIOxzHhN2BKEb6btSzelKx8AZqBpzlqXXsQ2FmrH8Ts6f9d/ttX3Mq8gceNVxlVLw2MIxhchICrv+s635UmaVgf8fIBgIztAETh7wl8//mKxYjDGD+GyWI740AvQly4Trq01oRx0QLa4TtKXyAqdP7WGbScWdn5A; _ga_8JE65Q40S6=GS1.1.1658044593.1.1.1658050777.0; _ga=GA1.1.1728938263.1658044594; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'pexels.middlewares.PexelsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'pexels.middlewares.PexelsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'pexels.pipelines.PexelsPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
IMAGES_STORE = "./img"
HTTPERROR_ALLOWED_CODES = [403]  # 上面报的是403，就把403加入。
FEED_EXPORT_ENCODING = 'utf-8'
