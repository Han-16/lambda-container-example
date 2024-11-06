FROM amazon/aws-lambda-python:3.10
RUN /var/lang/bin/python3.10 -m pip install --upgrade pip
RUN yum install git -y
RUN git clone https://github.com/Han-16/lambda-container-example.git
# RUN /var/lang/bin/python3.10 -m pip install torch==2.1.0+cu121 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 huggingface-hub==0.26.2 llama-cpp-python langchain-core tensorflow pymc
RUN /var/lang/bin/python3.10 -m pip install -r lambda-container-example/requirements.txt
RUN cp lambda_function.py /var/task/
CMD ["lambda_function.lambda_handler"]