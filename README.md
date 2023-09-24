# machine_learning_project
Industry Standard Way Of Writing Projects

Requirements

1. [Github Account] (https://github.com)
2. [Heroku Account] (https://dashboard.heroku.com/login)
3. [VS CODE SOFTWARE] (https://code.visualstudio.com/download)
4. [GIT CLI] (https://git-scm.com/downloads) 
5. [GIT Documentation] (https://git-scm.com/docs/gittutorial)

Creating conda environment
```
conda create -p venv python==3.7 -y
```

Activate conda virtual environment
```
conda activate env/
```

```
pip install -r requirements.txt
```

To add file in git
```
for all files and folder
    git add .
```

```
for a specific file
    git add <file_name>
```

To ignore files while pushing files to github, you should add the name of the files in .gitignore file

To check git status

```
git status
```

To check all versions maintained by git

```
git log
```

To create a version or commit all changes

```
git commit -m "message"
```
To check origin or project url
```
git remote -v
``

To setup CI/CD pipeline in Heroku, we need 3 information

1. HEROKU EMAIL = victoropeyemi97@outlook.com
2. HEROKU API_KEY = <>
3. HEROKU APP_NAME = ml-regression-app-2


Build Docker Image

```
docker build -t <image_name>:<tag_name> .
```
>Note: docker image name should always be lowercase letter


To list docker images

```
dpcker images
```

To run docker image

```
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID>
```

To check running container in docker
```
docker ps
```

To stop docker container

```
docker stop <Container ID>
```