English

<h1>📚 Degirum ORCA on Amber OS </h1>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Amber OS User Guide](#-amberos-guide)
	- [Amber OS finder](#-amberos-finder)
	- [PRO Tools installation](#-protools-installaiton)
	- [DeGirum Client installation](#-dgclient-installaiton)
	- [Download user manuals](#-user_manuals)
- [Getting Started](#-getting-started)
- [Run DeGirum Notebooks](#-run-degirum-notebooks)
	- [To Launch a Single Notebook with Cloud Key](#to-launch-degirum_cloud)
	- [To Launch a Single Notebook with Local IP](#to-launch-degirum_ip)
- [FAQ](#-faq)


<div id='-amberos-guide'/>

## Amber OS User Guide

<div id='-amberos-finder'/>

## Amber OS finder
1. Open a web browser on the same network as Amber OS.
2. Type "latticenode.local" in the address bar.
3. Click your Amber OS and use the default account(admin) to log in.
4. The default account/password is admin/admin1234. 

<img src="./images/amberos_finder.gif" height="600">


<div id='-protools-installaiton'/>

## PRO Tools installation
1. Login Amber OS.
2. Click "Control Pannel" -> "Pro Tools" -> "Install Now" -> "Apply".

<img src="./images/protools_install.gif" height="600">

<div id='-dgclient-installaiton'/>

## Degirum Client installation
1. Login Amber OS.
2. Click "Pro Tools" -> "App Store"
3. Input "degirum" -> click search. 
4. Click "Install" -> "OK".

<img src="./images/degirum_client_install.gif" height="600">

<div id='-user_manuals'/>

## Download user manuals
1. [Amber OS](https://myamber.cloud/life/v1/file?query=%7B%22token%22%3A%22dc86bf44980a529fa3b0fce6a6e2d08e%22%2C%22root%22%3A%22cloud%22%2C%22path%22%3A%22%2Fshared-to%2Fffa377c3-a8c6f35d%2FAmberPRO%2FAmberPRO+OS+User+Manual%2FAmber+OS+-+User+Manual.pdf%22%2C%22download%22%3A%22true%22%7D)
2. [PRO Tools](https://myamber.cloud/life/v1/file?query=%7B%22token%22%3A%22dc86bf44980a529fa3b0fce6a6e2d08e%22%2C%22root%22%3A%22cloud%22%2C%22path%22%3A%22%2Fshared-to%2Fffa377c3-a8c6f35d%2FAmberPRO%2FPRO+Tools+%28beta%29%2FPRO+Tools+1.19.1+User+Manual.pdf%22%2C%22download%22%3A%22true%22%7D)


<div id='-getting-started'/>

## Getting Started

1. Use [Amber OS Finder](#amber-os-finder) to find your Amber OS.
2. Sign up for an AmberCloud account(https://myamber.cloud/#ln/signup).
3. Install [Pro Tools](#-protools-installaiton).  
4. Install [DeGirum Client](#-dgclient-installaiton) 
5. Sign up for an account on DeGirum Cloud Portal and Log in. (https://cs.degirum.com)
6. Study the DeGirum Development Tools(inclued pySDK,AI Models and on-line documents) are available on the Cloud Platform(https://docs.degirum.com/content/).
7. Explore Degirum Jupyter notebooks using github URL (https://github.com/DeGirum/PySDKExamples), select one related to your needs or give them all a try. Good Luck!

To install to the new release version, please run `python -m pip install degirum --extra-index-url https://degirum.github.io/simple` in degirum client container. 

If you run into issues, please check the [troubleshooting section](#-troubleshooting), [FAQs](#-faq)
If you need help on pySDK and AI models convert issues, please start a GitHub discussions.(https://github.com/DeGirum/PySDKExamples/discussions).  


<div id='-run-degirum-notebooks'/>

## Run DeGirum Notebooks
```
git clone https://github.com/DeGirum/PySDKExamples.git
cd PySDKExamples
pip install -r ./requirements.txt
```

<img src="./images/degirum_example_localip.gif" height="600">

<div id='to-launch-degirum_cloud'/>

## To Launch a Single Notebook with Cloud Key

Create cloud API access token on Tokens page of DeGirum Cloud Portal(https://cs.degirum.com/profile#profile-tab-tokens).

```
import degirum as dg         # import DeGirum PySDK package
# connect to DeGirum cloud platform and use DeGirum public model zoo
zoo = dg.connect(dg.CLOUD, "https://cs.degirum.com", "<my cloud API access token>")
print(zoo.list_models())     # print all available models in the model zoo

# load mobilenet_ssd model for CPU; model_name should be one returned by zoo.list_models()
model_name = "mobilenet_v2_ssd_coco--300x300_quant_n2x_cpu_1"     
model = zoo.load_model(model_name, image_backend='pil')

# perform AI inference of an image specified by URL
image_url = "https://raw.githubusercontent.com/DeGirum/PySDKExamples/main/images/TwoCats.jpg"
result = model(image_url)

print(result)                # print numeric results
result.image_overlay.show()  # show graphical results
```


<div id='to-launch-degirum_ip'/>

## To Launch a Single Notebook with Local IP
```
import degirum as dg         # import DeGirum PySDK package
# connect to Local Degirum Server
AmberOS_docker_host_IP = '172.17.0.1' 
zoo = dg.connect(AmberOS_docker_host_IP)
print(zoo.list_models())     # print all available models in the model zoo

# load mobilenet_ssd model for CPU; model_name should be one returned by zoo.list_models()
model_name = "mobilenet_v2_ssd_coco--300x300_quant_n2x_orca1_1"     
model = zoo.load_model(model_name, image_backend='pil')

# perform AI inference of an image specified by URL
image_url = "https://raw.githubusercontent.com/DeGirum/PySDKExamples/main/images/TwoCats.jpg"
result = model(image_url)

print(result)                # print numeric results
result.image_overlay.show()  # show graphical results
```


<div id='-faq'/>

## FAQ
- [Latticework Support](https://support.myamberlife.com/hc/en-us)
- [DeGirum Support](https://degirum.ai/)

