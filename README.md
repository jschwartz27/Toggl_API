# Toggl_API

You must install and configure the venmo API:
```shell
$ pip install venmo
$ venmo configure
```

To run the main script, one argument must be provided:
  - the key which you have received
 
 ```shell
$ python main.py -key "example_key"
```
You can also add the function to attach pdfs to the email:
 ```shell
$ python main.py -key "example_key" -pdf True
```
