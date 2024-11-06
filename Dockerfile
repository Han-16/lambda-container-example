FROM amazon/aws-lambda-python:3.8

RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
RUN apt-get install git -y
RUN git clone https::/github.com/Han-16/lambda-container.example
RUN pip install -r lambda-container-example/requirements.txt

RUN cp lambda-container-example/lambda_function.py /var/task/
# RUN cp lambda-container-example/imagenet_class_index.json /var/task/

# CMD ["lambda_function.lambda_handler"]