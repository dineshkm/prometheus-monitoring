FROM python:3.6

ADD http-monitor /http-monitor
RUN pip install -r /http-monitor/pip-requirements.txt

WORKDIR /http-monitor
ENV PYTHONPATH '/http-monitor/'
EXPOSE 8080

CMD ["python" , "/http-monitor/monitor.py"]