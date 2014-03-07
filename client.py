import urlparse

from libthumbor import CryptoURL

SECRET_KEY = 'MY_SECURE_KEY'
THUMBOR_SERVER = 'http://127.0.0.1:8888'

# upload & get the thumbnail url

crypto = CryptoURL(key=SECRET_KEY)
image_url = crypto.generate(width=150, height=150,
    image_url='29.media.tumblr.com/tumblr_lltzgnHi5F1qzib3wo1_400.jpg')
print urlparse.urljoin(THUMBOR_SERVER, image_url)
