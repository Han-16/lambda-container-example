FROM amazon/aws-lambda-python:3.10
RUN /var/lang/bin/python3.10 -m pip install --upgrade pip
ARG ACCESS_KEY
ARG SECRET_KEY
ENV ACCESS_KEY=${ACCESS_KEY}
ENV SECRET_KEY=${SECRET_KEY}
RUN yum install git gcc-c++ cmake make -y
RUN /var/lang/bin/python3.10 -m pip install llama-cpp-python
RUN /var/lang/bin/python3.10 -m pip install torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu
RUN git clone https://github.com/Han-16/lambda-container-example
RUN /var/lang/bin/python3.10 -m pip install -r lambda-container-example/requirements.txt
COPY temp/ /var/task/temp/
COPY lambda_function.py /var/task/
CMD ["lambda_function.handler"]