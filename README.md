# pip 20.2 fails to resolve editable dependencies

## Example with pip==20.2.1

```
$ virtualenv -p python2.7 venv
Running virtualenv with interpreter /usr/bin/python2.7
Already using interpreter /usr/bin/python2.7
New python executable in /home/alanb/tmp/pip-bug/venv/bin/python2.7
Also creating executable in /home/alanb/tmp/pip-bug/venv/bin/python
Installing setuptools, pip, wheel...
done.

$ source venv/bin/activate

(venv) $ pip --version
pip 20.2.1 from /home/alanb/tmp/pip-bug/venv/local/lib/python2.7/site-packages/pip (python 2.7)

(venv) $ pip install -e package_a/
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Obtaining file:///home/alanb/tmp/pip-bug/package_a
Installing collected packages: package-a
  Running setup.py develop for package-a
Successfully installed package-a

(venv) $ pip install -e package_b/
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Obtaining file:///home/alanb/tmp/pip-bug/package_b
ERROR: Could not find a version that satisfies the requirement package-a (from package-b==0.1) (from versions: none)
ERROR: No matching distribution found for package-a (from package-b==0.1)
```

## Example with pip==20.1.1

```
$ virtualenv -p python2.7 venv
Running virtualenv with interpreter /usr/bin/python2.7
Already using interpreter /usr/bin/python2.7
New python executable in /home/alanb/tmp/pip-bug/venv/bin/python2.7
Also creating executable in /home/alanb/tmp/pip-bug/venv/bin/python
Installing setuptools, pip, wheel...
done.

$ source venv/bin/activate

(venv) $ pip install 'pip<20.2'
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting pip<20.2
  Using cached pip-20.1.1-py2.py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.1
    Uninstalling pip-20.2.1:
      Successfully uninstalled pip-20.2.1
Successfully installed pip-20.1.1

(venv) $ pip --version
pip 20.1.1 from /home/alanb/tmp/pip-bug/venv/local/lib/python2.7/site-packages/pip (python 2.7)

(venv) $ pip install -e package_a/
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Obtaining file:///home/alanb/tmp/pip-bug/package_a
Installing collected packages: package-a
  Running setup.py develop for package-a
Successfully installed package-a
WARNING: You are using pip version 20.1.1; however, version 20.2.1 is available.
You should consider upgrading via the '/home/alanb/tmp/pip-bug/venv/bin/python2.7 -m pip install --upgrade pip' command.

(venv) $ pip install -e package_b/
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Obtaining file:///home/alanb/tmp/pip-bug/package_b
Requirement already satisfied: package-a in ./package_a (from package-b==0.1) (0.1)
Installing collected packages: package-b
  Running setup.py develop for package-b
Successfully installed package-b
WARNING: You are using pip version 20.1.1; however, version 20.2.1 is available.
You should consider upgrading via the '/home/alanb/tmp/pip-bug/venv/bin/python2.7 -m pip install --upgrade pip' command.
```