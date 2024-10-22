# Life_Hack, Data Hack and Best Sustainability Hack 2022
HackHarvard 2022
[Best Lifehack Hack + Sustainability Prize + Data hack]

## About
Sustainability-focused Computer Vision model on helping women/people identify their correct bra and clothing sizes, then pair them with a tailor who will make the proper fitting garments for them by applying sustainability principles.
<img width="453" alt="image" src="https://user-images.githubusercontent.com/33704683/196038567-f3d0c4b7-3513-4c4a-8d6a-f78b204736a9.png">


## Introduction
80% of women wear the incorrect bra size,with 70% of women wearing ones that are too small and 10% wearing ones that are too big. Fuller bust bra and smaller bra are difficult to find and even if we do they are very expense and cannot assure comfort. Which is why Perfect Fit saw the need and taking on the challenge of making sustainable bra/clothing at affroable price.


## Design
<img width="746" alt="image" src="https://user-images.githubusercontent.com/33704683/196040455-49294e57-ed37-4701-b690-3fbd1daa5b90.png">
<img width="738" alt="image" src="https://user-images.githubusercontent.com/33704683/196040494-326b440b-44b2-442a-aa2a-b74feff8553b.png">

Then, the circumference of the biggest Ellipse is calculated from the the respective recantagles we objected by capturing images above.
![image](https://user-images.githubusercontent.com/33704683/196040734-492abee9-38d3-4f2c-ac46-006debfe8bc9.png)

Then we feed that data back into the data model for Linear regression. 

##Summary of the Methods
The project involves breaking down overwhelmingly technical text into information that can be used to identify clothes for all body like T-shirts, pants and Bra.
To be able to get the actual values in inches, we need to use an object with practically a constant value. We choose a Credit card as this object so we can convert pixels to inches in a more accurate way. Basically we just get the ratio between the values in pixel/inches.

## Visualization of Backend
![Picture1](https://user-images.githubusercontent.com/33704683/196041748-aa05c593-c3e2-4622-84a0-bc5253b4fd4f.png)



## Languages, Packages, and Technologies
• **`Python`**: back end and Natural Language Processing

• **`Flask`**: integrate front end with back end

• **`Visul Studio Code`**: testing, exploratory data analysis, and development

• **`HTML/CSS`**: UX/UI design

• **`Javascript / jquery`**: validations and dynamic elements in HTML/CSS 

• **`Heroku/Netify`**: hosting server

• **`OpenCV`**: Conversion from Pixels to inches

## Link
[PerfectFit](https://perfectfit-website.netlify.app/)


