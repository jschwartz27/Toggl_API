# Toggl Progress API

Create your environment with the following command:
```shell
$ conda env create -f environment.yml
$ conda activate toggl_env
```

And when you want to exit the environment:
```shell
$ conda deactivate
```

To run the main script:
```shell
$ python main.py
```
You can also add the function to attach pdfs to the email:
 ```shell
$ python main.py -pdf True
```

In config.yml, you can adjust settings. E.g., the default transfer amount is $20.00
