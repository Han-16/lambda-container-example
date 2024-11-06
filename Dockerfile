FROM amazon/aws-lambda-python:3.10
RUN /var/lang/bin/python3.10 -m pip install --upgrade pip
RUN yum install git -y
RUN git clone https://github.com/Han-16/lambda-container-example.git
# RUN CMAKE_ARGS="-DLLAMA_CUDA=on" /var/lang/bin/python3.10 -m pip install llama-cpp-python
RUN /var/lang/bin/python3.10 -m pip install torch==2.1.0
RUN /var/lang/bin/python3.10 -m pip install -r lambda-container-example/requirements.txt
RUN cp lambda_function.py /var/task/
CMD ["lambda_function.lambda_handler"]