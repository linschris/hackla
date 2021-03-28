# Recovery - LAHacks submission

## Welcome to Recovery!

### Inspiration

Three of our team members had family members who had COVID-19. Concerned with their recovery process, we shared with each other advice on how we could help them. What we found to be a universal piece of advice was maintaining a balanced diet high in nutrients. This notion that well-balanced diet can help accelerate the recovery process is what inspired us to make Recovery, an app that helps users with COVID-19 create a meal plan to aid them in fighting the virus. We want to stress that although vaccines are being distributed and cases are declining, the pandemic is still ongoing, and that COVID-19 can still induce serious symptoms.

### What it does

https://www.hss.edu/guide-COVID-19-nutritional-rehabilitation-restore-replenish.asp

Recovery is a nutrition tracking and analysis progressive web app focused on rehabilitating people from COVID-19 through their diet. Within the app, the user is able to input their weight and sex to create a customized meal plan based on their personal nutrition requirements. Users can scan food items via their barcodes and automatically contribute their meal progress to their nutrition goals. They can alternatively search for the name of their food and select their item from the results

### How we built it

In the backend, we used Python to pull information about a food's nutrients from the OpenFoodFacts and FoodData Central databases. With this data, we built functions to keep track of nutrient intake and also calculate how much a person's needed nutrients based on sex and weight. Since OpenFoodFacts stored barcodes of items in their API, we decided to implement a barcode scanner feature that would enhance the user experience by allowing them to simply scan their item instead of having to manually search for it. All of the data instructions that we have is then sent over to the frontend which is essentially a PWA constructed with React.js. After the data has been parsed, the information is finally sent to the user.

### What we learned

* Front-end and back-end workflow
* How to deploy backend to Google App Engine
* Barcode scanning implementation with Python

### Challenges we faced

* Nutrient unit conversion from differences in APIs
* Managing state in React
* Low success rate for barcode-image recognition
* Handling and sorting from messy databases
* First time making a mobile app

### Accomplishments we're proud of

* Consistent barcode detection through image cropping & post-processing
* Nice design (UI, logo)
* iOS compatibility

### What's next for Recovery

* Ability to share nutrition progress on social media
* Android compatibility
* Allow users to create their own meal plans with custom nutrition quotas
* Addition of more preset meal plans based on other personalized needs (ex: weight loss, muscle gain, diabetics)

### Built with

* Flask
* React.js
* Figma
* Python
* Google Cloud
* Docker
* Postman
* Netlify
* SCSS

#### The team

* Pranav Grover
* Tan Huynh
* Christopher Linscott
* Bowen Tang
* Edmund Zhi
