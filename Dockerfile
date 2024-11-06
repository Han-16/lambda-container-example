FROM amazon/aws-lambda-python:3.10
RUN /var/lang/bin/python3.10 -m pip install --upgrade pip
RUN yum install git -y
RUN git clone https://github.com/Han-16/lambda-container-example.git
# RUN /var/lang/bin/python3.10 -m pip install llama-cpp-python==0.3.1 torch==2.1.0
RUN FORCE_CMAKE=1 /var/lang/bin/python3.10 -m pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
RUN /var/lang/bin/python3.10 -m pip install torch==2.1.0
RUN /var/lang/bin/python3.10 -m pip install -r lambda-container-example/requirements.txt
RUN cp lambda_function.py /var/task/
CMD ["lambda_function.lambda_handler"]