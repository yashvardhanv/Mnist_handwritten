# Mnist_handwritten
An deep neural network traineed using mnist digits data is deployed on a flask webpage, where you can draw on a canvas and the model will predict the digit.

mnist.keras is a dumped model trained on local machine and another.keras is trained on colab. For front-end canvas is used as a sketchpad which is converted into dataUrl and sent to flask backend using ajax.

I tried deploying it on vercel but it took so long to deploy. Maybe because it uses large libraries such as tensorflow and slug size exceeds 300mb. It might work by only using tensorflow-cpu but that would take another 40 min to deploy . So, here are some snapshots of website.
1.
![pic1](https://github.com/yashvardhanv/Mnist_handwritten/assets/49940157/a2e0131d-234e-4ac8-91db-444690a3c8f1)

2.
![pic2](https://github.com/yashvardhanv/Mnist_handwritten/assets/49940157/c7dbd6cf-9a39-46f2-9e7d-b5284a860ccb)

3.
![pic3](https://github.com/yashvardhanv/Mnist_handwritten/assets/49940157/252d354b-cabe-4b9e-a1c0-85a6b5fc0139)

