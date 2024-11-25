FROM ubuntu:22.04

RUN apt-get update && apt-get install -y latexmk python3-pip
RUN mkdir /etc/hw_2
COPY *.py /etc/hw_2/

RUN pip install latex-functions==0.0.1

CMD python3.10 /etc/hw_2/run_modules.py --latex-path /etc/hw_2/artifacts/artifacts.tex && \
latexmk -output-directory=/etc/hw_2/artifacts/ -pdf /etc/hw_2/artifacts/artifacts.tex && \
rm -f /etc/hw_2/artifacts/artifacts.aux /etc/hw_2/artifacts/artifacts.log /etc/hw_2/artifacts/artifacts.fls /etc/hw_2/artifacts/artifacts.fdb_latexmk

