FROM python:3.9-windowsservercore
WORKDIR /app
COPY . .
RUN Install-PackageProvider -Name Chocolatey -Force
RUN pip install -U selenium
RUN pip install pytest

