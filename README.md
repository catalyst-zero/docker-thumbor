# docker-thumbor

[Thumbor](https://github.com/globocom/thumbor) image server in a
[docker](https://www.docker.io/) container, deployed with
[dokku](https://github.com/progrium/dokku), inspired by
https://github.com/georgeyk/test-thumbor.

## deployment

Setup ssh key.
```bash
cat ~/.ssh/id_rsa.pub | ssh root@thumbor.your-domain.com "sudo sshcommand acl-add dokku $USER"
```

Setup git remote (assuming `$DOKKU_ROOT/VHOST` contains your-domain.com).
```bash
git remote add thumbor.your-domain.com dokku@thumbor.your-domain.com:thumbor
```

Push your code.
```bash
git push thumbor.your-domain.com master
```

Set the thumbor security key as ENV var in your dokku application. After
setting the key you need to redeploy your app (check
https://github.com/scottatron/dokku-rebuild). For testing use the script below,
to get a secured url.
```bash
echo "export THUMBOR_SECURITY_KEY=yourkey" >> $DOKKU_ROOT/$YOUR_APP/ENV
```

## testing
Install `libthumbor` and execute the script below.
```bash
pip install libthumbor
```
Script to generate a url.
```python
import urlparse

from libthumbor import CryptoURL

SECRET_KEY = 'yourkey'
THUMBOR_SERVER = 'http://127.0.0.1:8888'

# get the thumbnail url
crypto = CryptoURL(key=SECRET_KEY)
image_url = crypto.generate(width=150, height=150, image_url='yoururl')
print urlparse.urljoin(THUMBOR_SERVER, image_url)
```
