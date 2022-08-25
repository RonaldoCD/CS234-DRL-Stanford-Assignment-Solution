# Installation

* Download and uncompress this repository onto the machine or VM you are planning to use for assignment 3.

* Install Docker by following the [official documentation](https://docs.docker.com/get-docker/). 
> You can skip this step if you are using an Azure VM (e.g. VM used in assignment 2) since Docker has already been installed.

* Make sure your current working directory is the directory containing this README file.
* Build Docker image.

```bash
sudo docker build -t cs234-a3 .
```

* Run Docker image and bind to starter code directory.

```bash
sudo docker run -v PATH/TO/STARTER/CODE/DIR:/home/cs234-a3 -it cs234-a3
```

* Now you are in the `cs234-a3` container and you can edit your solutions directly.
* Submit your solutions to GradeScope. You can generate your submissions using: 

```bash
bash collect_submission.sh
```

## Known Issues
* This image will not work on ARM64 machines such as M1 Macbooks. Please use a x86 machine or VM instead.
* Make sure your machine or VM has 30G+ available disk space.
