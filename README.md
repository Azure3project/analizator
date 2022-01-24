https://yourshoppinganalyzer.azurewebsites.net/

# No more food waste!
The project was a part of the course *Introduction to applications and solutions based on Artificial Intelligence and Microsoft Azure* at the Warsaw University of Technology.

## Table of contents
* [Description and the goal of the project](#description)
* [Contributors](#contributors)
* [Functionality description](#functionality)
* [Architecture](#architecture)
* [Tech Stack](#tech-stack)
* [User Guide](#user-guide)
* [Demo](#demo)
* [How to implement this innovation in real life?](#innovation)

<a name="description"/></a>
## Description and the goal of the project
According to the UN report, on average each person throws away 74 kg of food products. This is controversial information to know that approximately 690 million people are malnourished. Food waste and losses are responsible for around 10% of the emissions causing the climate crisis. In Poland, 153 kilograms of food are thrown into the bin every second. Annually, we waste 4.8 million tons of food in Poland. To prevent further food waste, we decided to create a web application that allows us to monitor the contents of our fridge and informs us which products are ending the expiry date so that we can consume the product and not have to throw it away.

<a href="https://klimat.rp.pl/ekotrendy/art17074151-raport-onz-miliard-ton-zywnosci-rocznie-laduje-na-smietniku" target="_blank">Link to data about food waste</a>

<a name="contributors"/></a>
## Contributors
* <a href="https://github.com/gubapatryk" target="_blank">Patryk Guba</a>
* <a href="https://github.com/mjakubowska" target="_blank">Martyna Jakubowska</a>
* <a href="https://github.com/kingakocol" target="_blank">Kinga Kocoł</a>
* <a href="https://github.com/Olakow" target="_blank">Aleksandra Kowalczyk</a>
* <a href="https://github.com/maxxx958" target="_blank">Maxymilian Kowalski</a>
* <a href="https://github.com/AleksanderWodnicki" target="_blank">Aleksander Wodnicki</a>

<a name="functionality"/></a>
## Functionality description
The web application allows you to add and store products in a virtual fridge. In addition to the names of the products, the use-by date of the individual products is also displayed. There are two ways to add ingredients. The first one allows you to add a photo of the sales receipt, then, using OCR, the names of products are extracted from the receipt, appropriate expiration dates are assigned and placed in the fridge. The second way is to manually add products, just enter the product name and the expiration date of the product. The products in the fridge are sorted by their use-by date.

<a name="architecture"/></a>
## Architecture
Tutaj trzeba dodać diagram

<a name="tech-stack"/></a>
## Tech Stack

### Azure App Service Web Apps

 <p align="center">
 <img src="app/materials/appservice.png"/>
 </p>
 
Quickly and easily create enterprise-ready web and mobile apps for any platform or device, and deploy them on a scalable and reliable cloud infrastructure.
 
Documentation: https://azure.microsoft.com/en-us/services/app-service/#documentation
Pricing: https://azure.microsoft.com/en-us/services/app-service/#pricing

### Azure Cognitive Services Computer Vision 

 <p align="center">
 <img src="app/materials/computervision.png"/>
 </p>
 
An AI service that analyzes content in images and video

Documentation: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/
Pricing: https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#pricing
 
### Azure Cognitive Services Computer Vision Optical Character Recognition

The Optical Character Recognition (OCR) service extracts text from images. You can use the new Read API to extract printed and handwritten text from photos and documents. It uses deep-learning-based models and works with text on a variety of surfaces and backgrounds. These include business documents, invoices, receipts, posters, business cards, letters, and whiteboards. 

Quickstart: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio
Language support: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/language-support

### Azure Key Vault

 <p align="center">
 <img src="app/materials/keyvault.png"/>
 </p>
 
Safeguard cryptographic keys and other secrets used by cloud apps and services
 
Documentation: https://azure.microsoft.com/en-us/services/key-vault/#documentation
Pricing: https://azure.microsoft.com/en-us/pricing/details/key-vault/

### Flask

 <p align="center">
 <img src="app/materials/flask.png"/>
 </p>
 
 Flask is a micro web framework written in Python. Flask depends on the Jinja template engine and the Werkzeug WSGI toolkit. 
 
Documentation: https://flask.palletsprojects.com/en/2.0.x/

<a name="user-guide"/></a>
## User Guide

<a name="demo"/></a>
## Demo
 
 <a name="innovation"/></a>
## How to implement this innovation in real life?

We have three solutions:


1. Every shop has the same names for every products. In this case our app could recognize everything and could be use in every shop based  only on one "products dictonary".

2. Many shops have their own app, for example Lidl has app where our receipts are stored. It will be really easy to add our module for their app! Customers could have automatically updated e-fridge in their app.

<p align="center">
 <img src="app/materials/lidl1.png"/>
 </p>

3. We have also one more idea which could help everyone control products' terms of validity even if this person don't have spartphone or computer! During scanning of purchases system could sort them by terms of validity. Then, person at home just takes a look for the top of receipt and will know what to eat first.
