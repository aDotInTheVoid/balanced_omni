# Local Setup
This only works on macOS. If you need windows, contact me.
## Terminal Usage
The terminal is pretty essential, so you need to know some basic commands.

### Notation
A `$` means the start of a new command.

Eg:
```bash
$ pwd
/Users/nixon/dev/web/fullstack/balanced_omni
```


This means type `pwd` into the terminal, and you will get an output like `/Users/nixon/dev/web/fullstack/balanced_omni`.

A `#` symbol indicates a comment, and these will not need to be typed out, but give additional information about a command.

Additionaly, the `$` (aka the prompt) will look something like `Nixons-MacBook-Pro-2:ballenced_web nixon$`:
- `Nixons-MacBook-Pro-2` is the name of the machine
- `ballenced_web` is the folder you're in
- `nixon` is the user you are

### Basic navigation
The most core commands are `cd`, `pwd`, and `ls`.
- `cd`: Change directory: (directory means folder). It moves where you are in the terminal
- `pwd`: Print working directory`. It prints your locations.
- `ls`: List: It lists directory contents.

#### `pwd`
`pwd` is generally called without arguments (ie you type nothing after the `pwd`).

eg:
```bash
$ pwd
/Users/nixon/dev/web/fullstack/balanced_omni
```

#### `ls`
`ls` has one optional argument you can use: `-A`. This will show hidden files.

eg:
```bash
$ ls
LOCAL_DEPLOY.md  cypress.json  jest.config.js  postcss.config.js     src            venv
README.md        db.sqlite3    manage.py       public                src-cordova    vue.config.js
babel.config.js  dist          node_modules    requirements-dev.txt  tests          yarn.lock
backend          htmlcov       package.json    requirements.txt      tsconfig.json

$ ls -A
.browserslistrc  .travis.yml      db.sqlite3      postcss.config.js     tsconfig.json
.coveragerc      .vscode          dist            public                venv
.editorconfig    LOCAL_DEPLOY.md  htmlcov         requirements-dev.txt  vue.config.js
.eslintrc.js     README.md        jest.config.js  requirements.txt      yarn.lock
.git             babel.config.js  manage.py       src
.gitignore       backend          node_modules    src-cordova
.idea            cypress.json     package.json    tests
```
Notice how more stuff (with a name starting with `.` eg `.git` is shown) with `ls -A` than with `ls`.

#### `cd`
`cd` is used to move around the file system. It is always used to with 1 argument, the location you want to go to.

- `cd ~` will take you to `~` which means your home (eg `/Users/nixon`)
- `cd ..` will take you to the parent directory.

eg:
```bash
$ pwd
/Users/nixon/dev/web/fullstack/balanced_omni
$ cd ..
$ pwd
/Users/nixon/dev/web/fullstack
```
Note that cd generally doesn't give output.

- `cd src` will take you to the `src` directory (folder). If `src` isn't a folder in a the folder your in, you'll get an error.

eg:
```bash
$ ls
balanced_omni
$ cd src
bash: cd: src: No such file or directory
```

Multiple paths can be chained with a `/`

eg:
```bash
$ pwd
/Users/nixon/dev/web/fullstack
$ cd balanced_omni/src
$ pwd
/Users/nixon/dev/web/fullstack/balanced_omni/src
$ cd ../..
$ pwd
/Users/nixon/dev/web/fullstack
```

### Other commands
#### `man`
`man` opens a "man" page, which has much more detailed information about a command.

eg: `man ls` will open a page telling you about the many options of the `ls` command. 

This `man` command will open up the `less` command, which will allow you to scroll throught the pages using the arrow keys. To exit press q. More options for using `less`, and therefor `man` can be found with `man less`.

## Installing global software.
### Xcode
Go into the terminal and run `xcode-select --install`. This will open a pop up window that will allow you to both install just the command line tools, or all of xcode.

Either will work, but the command line tools are are quicker to install and take up less space on disk. However a full xcode install now will make it way easier if you ever want to do full swift development, as I've found it a pain to install xcode once I had the command lint tools installed

### Homebrew
Next you need to install homebrew, which is a package manager.

Go to [brew.sh](https://brew.sh/), and copy the command into the terminal. This will take some time, and may require admin rights.
### Brew Packages
We need 3 packages: git, python3 and yarn.

To get them, run `brew install git python3 yarn`

This will take some time.

## Cloning the repo

Now your ready to get the code. We use a system called git, which allows easy
syncing between multiple divices. Git is [highly](https://xkcd.com/1597/)
[complicated](https://twitter.com/agnoster/status/44636629423497217), and their
are [many](https://guides.github.com/) [guides](https://git-scm.com/book/en/v2)
to it's useage. However, if you are just running the code, you shouldn't need to
bother, as long as you don't want to make changes.

To get the code, navigate into the folder you want to put the folder with the code in (ie be in `~/code` before cloning, not `~/code/balanced`).

Then run
```bash
$ git clone https://github.com/aDotInTheVoid/balanced_omni
Cloning into 'balanced_omni'...
remote: Enumerating objects: 88, done.
remote: Counting objects: 100% (88/88), done.
remote: Compressing objects: 100% (68/68), done.
remote: Total 610 (delta 29), reused 66 (delta 18), pack-reused 522
Receiving objects: 100% (610/610), 534.81 KiB | 176.00 KiB/s, done.
Resolving deltas: 100% (293/293), done.
```
To do this, you will need a [github](https://github.com/) [account](https://github.com/join). Once you have one send me you're username so I can give you access to the code.

When you try to clone the code, git may ask you to login to github. This can
rapidly get annoying, so you probably want to set up [password
caching](https://help.github.com/en/github/using-git/caching-your-github-password-in-git)

Git will create a folder for you, and the code will be in the folder. This folder is called the "project root", and most commands need to be run from their

Once you have the code, cd into the folder, and your ready for your next step.


## Python (backend) setup
Because python links it's dependencies to a instance of the interpreter, you need a separate interpreter for the project to make sure nothing interferes with the project.

Therefor you need to install virtualenv, to manage create a "virtual environnement" to isolate the python you use for this, to the python you use for everything else.

Run `pip3 install virtualenv` to install the virtualenv tool.

Next, in the project folder (the one with `src`, `tests` and `backend` folders, as well as this file), Run `virtualenv -p python3 venv`, which creates a virtualenv called venv. It should look something like:

```bash
$ virtualenv -p python3 venv
Running virtualenv with interpreter /usr/local/bin/python3
Already using interpreter /usr/local/opt/python/bin/python3.7
Using base prefix '/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/nixon/dev/rand/balanced_omni/venv/bin/python3.7
Also creating executable in /Users/nixon/dev/rand/balanced_omni/venv/bin/python
Installing setuptools, pip, wheel...
done.
```

Next run `source venv/bin/activate`. This should put the text `venv` before your prompt. Eg (with a full prompt)

```bash
Nixons-MacBook-Pro-2:balanced_omni nixon$ source venv/bin/activate
(venv) Nixons-MacBook-Pro-2:balanced_omni nixon$ deactivate
Nixons-MacBook-Pro-2:balanced_omni nixon$
```
Notice how the deactivate command can be used to exit the virtualenv.

Next you need to install the dependencys. First make sure you are in the virtualenv by runing which:
```bash 
$ which pip3
/usr/local/bin/pip3
$ source venv/bin/activate
$ which pip3
/Users/nixon/dev/rand/balanced_omni/venv/bin/pip3
```
Make sure `pip3` is in `venv`, not something like `/usr`.

Once you have confirmed the correct `pip3`, use it to install the python dependencies
```bash
$ pip3 install -r requirements.txt
Collecting Django==2.2.8
  Using cached Django-2.2.8-py3-none-any.whl (7.5 MB)
Collecting django-cors-middleware==1.4.0
  Using cached django_cors_middleware-1.4.0-py3-none-any.whl (9.1 kB)
Collecting django-extensions==2.2.5
  Using cached django_extensions-2.2.5-py2.py3-none-any.whl (223 kB)
Collecting djangorestframework==3.10.3
  Using cached djangorestframework-3.10.3-py3-none-any.whl (909 kB)
Collecting PyJWT==1.7.1
  Using cached PyJWT-1.7.1-py2.py3-none-any.whl (18 kB)
Collecting sqlparse
  Using cached sqlparse-0.3.0-py2.py3-none-any.whl (39 kB)
Collecting pytz
  Using cached pytz-2019.3-py2.py3-none-any.whl (509 kB)
Collecting six>=1.2
  Downloading six-1.14.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: sqlparse, pytz, Django, django-cors-middleware, six, django-extensions, djangorestframework, PyJWT
Successfully installed Django-2.2.8 PyJWT-1.7.1 django-cors-middleware-1.4.0 django-extensions-2.2.5 djangorestframework-3.10.3 pytz-2019.3 six-1.14.0 sqlparse-0.3.0
```

Note that you probably wont use cached versions, but that's fine.

Now you can run the system check. In the root code directory (the one that conains a file `manage.py`) run

```bash
./manage.py check
System check identified no issues (0 silenced).
```

If you get errors, that's bad, [open an issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue) [on the code](https://github.com/aDotInTheVoid/balanced_omni/issues/new).

The `./` syntax tells the terminal that the program in in the current directory, rather than somewhere else.

If the system check is sucessfull, it's time to format the database. Run

```bash
$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, corsheaders, jwt_auth, profiles, sessions, tasks
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying jwt_auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying corsheaders.0001_initial... OK
  Applying profiles.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying tasks.0001_initial... OK
```

The output may be different, depending on the state of the code, but as long as their no errors you're fine.

Next create a superuser.

```bash
$ ./manage.py createsuperuser
Email: x@x.co
Username: x
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: Y
Superuser created successfully.
```
You will need to enter an email, username and password. Note that when entering a passowrd, it will not appear as you type, but their may be a key icon.

Django may warn you if you're chosen password is insecure, but as long as it's local, you'll be fine.

Now you can start the backend server.
```bash
$ ./manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
January 31, 2020 - 10:33:19
Django version 2.2.8, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
Note that the command will not stop running, so you'll need to open a new tab in the terminal to do more stuff while the server in running.

If you open the given url [(probably http://127.0.0.1:8000/)](http://127.0.0.1:8000/), you'll get an error 404 (unless I change this). Additionaly, it the output of the `./manage.py runserver` command, you should see `[31/Jan/2020 10:34:23] "GET / HTTP/1.1" 404 2361` albeit with a different date. 

However if you go to (`/admin`)[http://127.0.0.1:8000/admin] you'll see a login screen. Note that this is not the user-facing app, but an auto generated admin page that you'll want to use to edit the database (eg creating users).

## Node/yarn/vue (frontend)

To build the user facing site, you'll first need to install the frontend requirements

To do this, in the project root directory run
```bash
$ yarn install
yarn install v1.21.1
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
warning "@vue/eslint-config-airbnb > eslint-import-resolver-webpack@0.11.1" has unmet peer dependency "webpack@>=1.11.0".
warning " > sass-loader@8.0.0" has unmet peer dependency "webpack@^4.36.0".
warning " > vuetify-loader@1.3.1" has unmet peer dependency "webpack@^4.0.0".
[4/4] 🔨  Building fresh packages...
✨  Done in 38.25s.
```
Ignore the warnings they don't matter.

Finaly to run the local server, do:
```bash
$ yarn run serve
yarn run v1.21.1
$ vue-cli-service serve
 INFO  Starting development server...
Starting type checking service...
Using 1 worker with 2048MB memory limit
98% after emitting CopyPlugin

 DONE  Compiled successfully in 29047ms                                                                                13:27:41

No type errors found
Version: typescript 3.5.3
Time: 5050ms

  App running at:
  - Local:   http://localhost:8080
  - Network: http://10.7.5.170:8080

  Note that the development build is not optimized.
  To create a production build, run yarn build.
```
Right now, the frontend and backend don't talk to each other, so you don't need to run both at the same time, but this will change.