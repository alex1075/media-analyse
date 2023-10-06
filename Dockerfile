FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install -y cmake git autoconf libtool pkg-config
RUN apt install -y python3-pip python3-dev build-essential python-is-python3
RUN git clone https://github.com/LibRaw/LibRaw.git
RUN cd LibRaw && git checkout 0.16.1
RUN cd LibRaw && autoupdate
RUN cd LibRaw/ &&  autoreconf --install 
RUN cd LibRaw && ./configure && mkdir build && cd build && cmake .. && make && make install && ldconfig
RUN pip install opencv-python numpy tqdm inquirer pillow shutils rawpy rawkit
WORKDIR /app
COPY . /app
COPY code/ /app/data/
COPY code/helper/ /app/data/helper/
ENTRYPOINT ["/bin/python", "main.py"]
