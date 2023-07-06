FROM python


#python 
RUN apt-get update \
  && apt-get install -y \
  apt-utils \
  python3-pip \
  python3-dev 

RUN pip3 install \
  colorama==0.4.6 \
  dnspython==2.3.0 \
  email-validator==2.0.0.post2 \
  Flask==2.2.3 \
  flask-mongoengine==1.0.0 \
  Flask-PyMongo==2.3.0 \
  Flask-WTF==1.1.1 \
  idna==3.4 \
  itsdangerous==2.1.2 \
  Jinja2==3.1.2 \
  MarkupSafe==2.1.3 \
  mongoengine==0.27.0 \
  pymongo==4.4.0 \
  Werkzeug==2.3.6 \
  WTForms==3.0.1

  EXPOSE 5000