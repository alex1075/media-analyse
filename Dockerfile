FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install -y cmake git autoconf libtool pkg-config
RUN apt install -y python3-pip python3-dev build-essential python-is-python3 python3-numpy pybind11-dev libboost-python-dev python3-pybind11 
RUN apt install -y openexr libopenexr-dev 
RUN apt install -y libtiff-dev libtiff-tools libboost-all-dev
RUN apt install -y ffmpeg libopencv-dev libde265-dev aom-tools libaom-dev webp libopencolorio-dev
RUN git clone https://github.com/LibRaw/LibRaw.git
RUN cd LibRaw && autoupdate
RUN cd LibRaw/ &&  autoreconf --install 
RUN cd LibRaw && ./configure
RUN cd LibRaw && make && make install && ldconfig
RUN apt install *openimageio* -y
RUN pip install --upgrade numpy
RUN pip install opencv-python tqdm inquirer pillow shutils rawpy 
WORKDIR /app
COPY . /app
COPY code/ /app/data/
COPY code/helper/ /app/data/helper/
ENTRYPOINT ["./main.py"]
