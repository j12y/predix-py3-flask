
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

---
[signup]: https://www.predix.io/registration
[cf]: https://github.com/cloudfoundry/cli
