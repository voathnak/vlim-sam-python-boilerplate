FROM lambci/lambda:build-python3.7

RUN pip install -t /opt/python/ requests


COPY pdf_report_test/requirements.txt requirements.txt
RUN pip install -t /opt/python/ -r requirements.txt

RUN rm -rf /opt/include /opt/share
WORKDIR /var/task