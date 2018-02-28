
# ToDo: Finish this according to the guide
# https://docs.docker.com/get-started/part2/#tag-the-image
# and to check if scrapy needs an additional settings:
# https://github.com/scrapy-plugins/scrapy-splash

# Use an Floydhub deeplearning docker as a parent image
# https://github.com/floydhub/dl-docker
FROM floydhub/dl-docker:cpu

# Set the working directory to /keep-current
WORKDIR /keep-current

# Copy the current directory contents into the container at /keep-current
ADD . /keep-current

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "setup.py"]