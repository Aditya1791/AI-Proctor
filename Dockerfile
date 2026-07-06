FROM python:3.8-slim-bullseye

WORKDIR /app

# Pre-download DeepFace weights from alternate mirror to bypass Google Drive limits
RUN mkdir -p /root/.deepface/weights \
    && python -c "import urllib.request; urllib.request.urlretrieve('https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5', '/root/.deepface/weights/vgg_face_weights.h5')"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install them
COPY requirements.txt .

# Set CMake environment variable to compile dlib in parallel (e.g., using 4 cores)
ENV CMAKE_BUILD_PARALLEL_LEVEL=4
ENV DLIB_NO_GUI_SUPPORT=1

# Upgrade pip and install requirements
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir "protobuf<=3.20.1" Flask-Session==0.3.2 dlib
RUN pip install --no-cache-dir --upgrade gdown

# Download Natural Language Processing Models (NLTK)
RUN python -m nltk.downloader punkt wordnet averaged_perceptron_tagger

# Copy all the project files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
