# Set the base image
FROM python:3.10

# Creating the virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create the app directory inside the image
WORKDIR /btb_ai

# Copy the necessary files to the app directory
COPY btb_ai/ /btb_ai/btb_ai/
COPY run.py /btb_ai/
COPY dummy_response.json /btb_ai/
COPY requirements.txt /btb_ai/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port on which your Flask app is listening
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "run.py"]
