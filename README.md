test-thumbor
============

Setup
-----


* Instalar [docker](http://www.docker.io/gettingstarted/)

* Baixar imagem:

$ sudo docker pull georgeyk/thumbor

... wait and...
... wait ...


Uso
---


* Iniciar serviço:

$ sudo docker run -p 8888:8888 -i -t georgeyk/thumbor thumbor -l DEBUG

* Em outro terminal:

$ curl -XPOST -i -H "Slug: foo" http://127.0.0.1:8888/image --data-binary @mu.jpg


HTTP/1.1 100 (Continue)

HTTP/1.1 201 Created

Date: Tue, 03 Dec 2013 16:41:55 GMT

Content-Length: 0

Content-Type: text/html; charset=UTF-8

Location: /image/89f061b9fd20493f85b380a6b5f917cf/foo

Server: TornadoServer/3.1.1

* No browser (note o valor de Location):

http://127.0.0.1:8888/unsafe/100x100/89f061b9fd20493f85b380a6b5f917cf/foo

* Alternativamente, podemos passar apenas a URL da imagem que queremos o thumbnail (client.py):

$ python client.py
http://127.0.0.1:8888/hVwWGACa9JZSHNiFTMKs70NpR1s=/150x150/29.media.tumblr.com/tumblr_lltzgnHi5F1qzib3wo1_400.jpg


Segurança / Acesso por usuário
------------------------------


Não existe um método built-in no thumbor para isso.
Um possível workaround seria verificar, ao renderizar a URL no template, se o usuário possui permissão para ver tal imagem.

O thumbor prevê um mecanismo para evitar abuso do serviço [(here)](https://github.com/globocom/thumbor/wiki/Security)

Além disso é possível usar uma templetag para facilitar o uso nos templates [(here)](http://tech.yipit.com/2013/01/03/how-yipit-scales-thumbnailing-with-thumbor-and-cloudfront/)


Suporte para EXIF orientation
-----------------------------

Possui e é funcional (já está configurado no container de exemplo).

Podem usar essas [imagens](https://github.com/recurser/exif-orientation-examples) para testar


Performance
-----------

Não avaliei outras bibliotecas além da PIL.
Além dela ser a 'default' no thumbor (eg, deve ter um melhor suporte), existe uma nota explicando um bug com imagemagick na documentação do thumbor (usando .gif).
E ambas são wrappers para bibliotecas em C (eg, perfomance similares I guess)

Na utilização, vejo dois cenários:

1) Upload das imagens "internamente", isto é, ao recebermos a imagem, faremos o upload para o thumbor diretamente (similar ao exemplo no início deste arquivo).

Prós: elimina o tempo de espera para subir uma imagem ao thumbor
Contra: o cliente precisa guardar o "location" da imagem que fez o upload

2) Upload da imagem quando o usuário requisitar um thumbnail.

Prós: é mais dinâmico, pode poupar storage
Contra: contabiliza o tempo de upload


Existem opções para se configurar queues/storage/cache: redis, mongodb, memcache
E neste [link](http://tech.yipit.com/2013/01/03/how-yipit-scales-thumbnailing-with-thumbor-and-cloudfront/), o uso do aws cloudfront, embora não tenha testado com nenhuma essas opções.


Thumbnails para outros tipos de arquivos
----------------------------------------

* PDF: a solução mais comum é converter o arquivo para imagem (png/jpg) e então
  gerar o thumbnail.
  Aparentemente, o modo mais comum de se fazer isso é usando ferramentas
  externas como a imagemagick ou ghostscript.

* Vídeos: a solução mais simples seria extrair um frame e então gerar o
  thumbnail. Algumas bibliotecas de referência: PyMedia, ffmpeg.

* MP3 (e outros formatos de áudio): algumas bibliotecas para acessar os
  metadados: mutagen, PyMedia.

* .doc: parece ser possível utilizar o openoffice como "server" e então
  converter o arquivo para pdf (pyuno).
