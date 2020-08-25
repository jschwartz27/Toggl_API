# Toggl_API

You must install and configure the venmo API:
```shell
$ conda env create -f environment.yml
$ conda activate togglEnv
```

And when you want to exit the environment:
```shell
$ conda deactivate
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