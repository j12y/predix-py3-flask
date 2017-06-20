
# Overview

This is a simple demo of using Cloud Foundry, Flask, and Python 3.

## Requirements

- [ ] You must have at minimum a [Predix Free Tier](signup) account.
- [ ] You must have the [Cloud Foundry CLI](cf) and can run `cf login`

# Setup

```
git clone https://github.com/j12y/predix-py3-flask.git
cd predix-py3-flask
```

You'll want to change the application name to something unique just for you.

```
cf push
```
# Results

With a successful push you should be able to go to a URL such as:

https://py3-cf-demo.run.aws-usw02-pr.ice.predix.io/

Which will just print some text in your browser

> 3.5.3 (default, Jan 20 2017, 17:01:29) [GCC 4.8.4]

# Description

## **Procfile**

The **Procfile** informs Cloud Foundry what service to run when invoked.  In this
sample, it is simply `python app.py` which will run our code.  This is suitable
for demo purposes, but you may want to substitute a production web server such
as gunicorn for final applications.

## **app.py**

The **app.py** is a simple Flask demo.  With Cloud Foundry the PORT you should
use is exposed as an environment variable.  You can also run your flask app
without pushing to Predix by running `python app.py` where it will look for a
PORT environment variable or default to something such as
http://localhost:8080/.

If you are unfamiliar with Flask there are many great resources if you search.

## **manifest.yml**

The **manifest.yml** is used by Cloud Foundry to identify some details of how
your application should be `cf push`ed.  This example is pretty simple but
there are many other settings you can specify.  The **name** must be unique
across a Predix Availability Zone, so you may see an error:

```
Binding py3-cf-demo.run.aws-usw02-pr.ice.predix.io to py3-cf-demo...
FAILED
The route py3-cf-demo.run.aws-usw02-pr.ice.predix.io is already in use.
```

This simply means you need to give your app a unique name because the name is
part of the URL used in the resulting app.

The [python buildpack][buildpack] is optional to specify, in this example we are pulling the
latest version from github instead of using what the default would be in
Predix.

## **requirements.txt**

The python buildpack for Cloud Foundry will make sure to `pip install` anything
found in the requirements.txt and is needed for your application to run.  If
you have your own libraries not available on PyPI you may need to "vendor"
those dependencies.

## **runtime.txt**

The python buildpack for Cloud Foundry will look for this file and if found
will use a python version that corresponds.  Not every version of Python is
supported, so check the buildpack documentation for additional details.

If this file is absent you will default to a py2.x version.

---
[signup]: https://www.predix.io/registration
[cf]: https://github.com/cloudfoundry/cli
[buildpack]: http://docs.cloudfoundry.org/buildpacks/python/
