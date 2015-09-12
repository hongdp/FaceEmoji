from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
from sets import Set

raisebrow = {"faceId":"14a17b1c-3a8c-4369-800e-feb441275e21","faceRectangle":{"top":103,"left":148,"width":144,"height":138},"faceLandmarks":{"pupilLeft":{"x":190.9,"y":139.8},"pupilRight":{"x":248.5,"y":138.2},"noseTip":{"x":221.7,"y":177.2},"mouthLeft":{"x":196,"y":212.1},"mouthRight":{"x":243.6,"y":211.9},"eyebrowLeftOuter":{"x":169.7,"y":113},"eyebrowLeftInner":{"x":206,"y":111.1},"eyeLeftOuter":{"x":179.8,"y":139.2},"eyeLeftTop":{"x":189.6,"y":134.2},"eyeLeftBottom":{"x":189.6,"y":142.9},"eyeLeftInner":{"x":197.8,"y":140.6},"eyebrowRightInner":{"x":231.4,"y":110.4},"eyebrowRightOuter":{"x":265.6,"y":110.4},"eyeRightInner":{"x":241.2,"y":140.4},"eyeRightTop":{"x":249.4,"y":133.5},"eyeRightBottom":{"x":250.2,"y":142.4},"eyeRightOuter":{"x":258.7,"y":138.4},"noseRootLeft":{"x":211.3,"y":142.4},"noseRootRight":{"x":227,"y":141.7},"noseLeftAlarTop":{"x":206.2,"y":164.4},"noseRightAlarTop":{"x":233.6,"y":164.4},"noseLeftAlarOutTip":{"x":199.6,"y":182.2},"noseRightAlarOutTip":{"x":241,"y":181.4},"upperLipTop":{"x":222,"y":202.4},"upperLipBottom":{"x":221.9,"y":210.1},"underLipTop":{"x":221.7,"y":213.8},"underLipBottom":{"x":222,"y":224}},"attributes":{"headPose":{"pitch":0,"roll":-1.3,"yaw":-3.2},"gender":"male","age":36}}
angry = {"faceId":"cd8cef11-07cd-46b7-966b-748ff56addfb","faceRectangle":{"top":85,"left":148,"width":136,"height":136},"faceLandmarks":{"pupilLeft":{"x":187.6,"y":120.1},"pupilRight":{"x":242.7,"y":118.6},"noseTip":{"x":215.5,"y":155.4},"mouthLeft":{"x":194,"y":188.4},"mouthRight":{"x":238.9,"y":187.4},"eyebrowLeftOuter":{"x":167,"y":107.6},"eyebrowLeftInner":{"x":204.2,"y":106},"eyeLeftOuter":{"x":179.2,"y":120.4},"eyeLeftTop":{"x":187.6,"y":118},"eyeLeftBottom":{"x":187,"y":124},"eyeLeftInner":{"x":194.7,"y":121.8},"eyebrowRightInner":{"x":223.9,"y":104.8},"eyebrowRightOuter":{"x":260.9,"y":106.2},"eyeRightInner":{"x":235.2,"y":120.7},"eyeRightTop":{"x":243.2,"y":115.4},"eyeRightBottom":{"x":243.8,"y":123.4},"eyeRightOuter":{"x":251.3,"y":119.6},"noseRootLeft":{"x":208.1,"y":123.3},"noseRootRight":{"x":222.4,"y":123.9},"noseLeftAlarTop":{"x":202.4,"y":144.4},"noseRightAlarTop":{"x":227.6,"y":145.2},"noseLeftAlarOutTip":{"x":196.8,"y":158.8},"noseRightAlarOutTip":{"x":233.9,"y":159.2},"upperLipTop":{"x":216.5,"y":177.7},"upperLipBottom":{"x":216.8,"y":185.5},"underLipTop":{"x":216.4,"y":188.9},"underLipBottom":{"x":216.6,"y":198.3}},"attributes":{"headPose":{"pitch":0,"roll":-1.2,"yaw":-4.1},"gender":"male","age":26}}
normal = {"faceId":"1b82a7ae-8f2a-4669-9b89-3bb85b89f127","faceRectangle":{"top":93,"left":129,"width":134,"height":134},"faceLandmarks":{"pupilLeft":{"x":165.8,"y":129.5},"pupilRight":{"x":222.3,"y":127.5},"noseTip":{"x":194.2,"y":165.2},"mouthLeft":{"x":170.5,"y":191.8},"mouthRight":{"x":221.8,"y":191.5},"eyebrowLeftOuter":{"x":146.7,"y":112.2},"eyebrowLeftInner":{"x":180.8,"y":112.1},"eyeLeftOuter":{"x":158.7,"y":130.4},"eyeLeftTop":{"x":165.9,"y":126.6},"eyeLeftBottom":{"x":165.7,"y":134.1},"eyeLeftInner":{"x":173.3,"y":131.4},"eyebrowRightInner":{"x":205.2,"y":110.6},"eyebrowRightOuter":{"x":237.5,"y":109.3},"eyeRightInner":{"x":215.3,"y":130},"eyeRightTop":{"x":222.1,"y":124.7},"eyeRightBottom":{"x":223.3,"y":132.5},"eyeRightOuter":{"x":230.3,"y":128},"noseRootLeft":{"x":186.2,"y":133.9},"noseRootRight":{"x":202.1,"y":133},"noseLeftAlarTop":{"x":181.1,"y":153.2},"noseRightAlarTop":{"x":207.9,"y":152.6},"noseLeftAlarOutTip":{"x":175.6,"y":166.2},"noseRightAlarOutTip":{"x":214.3,"y":164.1},"upperLipTop":{"x":196.8,"y":185},"upperLipBottom":{"x":197.4,"y":192.1},"underLipTop":{"x":198.6,"y":196.2},"underLipBottom":{"x":198.4,"y":206.4}},"attributes":{"headPose":{"pitch":0,"roll":-2.4,"yaw":-4},"gender":"male","age":24}}
openmouth = {"faceId":"898d42be-b335-4da9-a651-2e8d430aedff","faceRectangle":{"top":92,"left":143,"width":142,"height":142},"faceLandmarks":{"pupilLeft":{"x":186.1,"y":127.5},"pupilRight":{"x":240.6,"y":126},"noseTip":{"x":211.8,"y":161.2},"mouthLeft":{"x":195.1,"y":204.1},"mouthRight":{"x":231.9,"y":202.4},"eyebrowLeftOuter":{"x":161.7,"y":113},"eyebrowLeftInner":{"x":201.5,"y":110.1},"eyeLeftOuter":{"x":175.9,"y":127.7},"eyeLeftTop":{"x":183.8,"y":124.5},"eyeLeftBottom":{"x":184,"y":130.8},"eyeLeftInner":{"x":191.9,"y":128.7},"eyebrowRightInner":{"x":221.6,"y":107},"eyebrowRightOuter":{"x":256.2,"y":110.8},"eyeRightInner":{"x":232.8,"y":127},"eyeRightTop":{"x":241.2,"y":123.5},"eyeRightBottom":{"x":241.3,"y":129.6},"eyeRightOuter":{"x":249.8,"y":127.3},"noseRootLeft":{"x":204.4,"y":128.6},"noseRootRight":{"x":220.6,"y":128},"noseLeftAlarTop":{"x":199.1,"y":149.6},"noseRightAlarTop":{"x":226,"y":148.6},"noseLeftAlarOutTip":{"x":193.5,"y":166.4},"noseRightAlarOutTip":{"x":232.1,"y":164.9},"upperLipTop":{"x":213.4,"y":184.8},"upperLipBottom":{"x":213.9,"y":194.9},"underLipTop":{"x":212.8,"y":214.3},"underLipBottom":{"x":213,"y":226.5}},"attributes":{"headPose":{"pitch":0,"roll":-1.2,"yaw":-4.1},"gender":"male","age":36}}
suprisedLu = {"faceId":"f3b3276f-5907-43b3-af12-de54bbda2b8b","faceRectangle":{"top":72,"left":121,"width":97,"height":97},"faceLandmarks":{"pupilLeft":{"x":155.4,"y":93.6},"pupilRight":{"x":191.3,"y":101.5},"noseTip":{"x":174.9,"y":114.4},"mouthLeft":{"x":148.5,"y":145.1},"mouthRight":{"x":173.4,"y":151.8},"eyebrowLeftOuter":{"x":141.7,"y":80.7},"eyebrowLeftInner":{"x":169,"y":78.1},"eyeLeftOuter":{"x":148.9,"y":92.7},"eyeLeftTop":{"x":155.5,"y":89.4},"eyeLeftBottom":{"x":154.6,"y":96.1},"eyeLeftInner":{"x":160.6,"y":95.1},"eyebrowRightInner":{"x":187.4,"y":83.7},"eyebrowRightOuter":{"x":206.9,"y":93.7},"eyeRightInner":{"x":187.3,"y":101},"eyeRightTop":{"x":193.1,"y":99.4},"eyeRightBottom":{"x":191.7,"y":105.1},"eyeRightOuter":{"x":197.3,"y":104.3},"noseRootLeft":{"x":170.5,"y":98.1},"noseRootRight":{"x":179.6,"y":99.9},"noseLeftAlarTop":{"x":165.2,"y":109.5},"noseRightAlarTop":{"x":180.9,"y":113},"noseLeftAlarOutTip":{"x":157.3,"y":117.2},"noseRightAlarOutTip":{"x":183,"y":123.4},"upperLipTop":{"x":168.1,"y":134},"upperLipBottom":{"x":166.8,"y":139},"underLipTop":{"x":163.4,"y":150.4},"underLipBottom":{"x":161.9,"y":155.3}},"attributes":{"headPose":{"pitch":0,"roll":12,"yaw":12.7},"gender":"female","age":38}}
closeeyes = {"faceId":"79b8ca14-1ee6-4b57-85d3-672b2bb8e64a","faceRectangle":{"top":75,"left":122,"width":135,"height":135},"faceLandmarks":{"pupilLeft":{"x":158.3,"y":112.7},"pupilRight":{"x":217.9,"y":110.3},"noseTip":{"x":188.7,"y":145},"mouthLeft":{"x":165.6,"y":174.4},"mouthRight":{"x":215.8,"y":175.1},"eyebrowLeftOuter":{"x":141.6,"y":92.7},"eyebrowLeftInner":{"x":178.1,"y":90.7},"eyeLeftOuter":{"x":148.8,"y":111.4},"eyeLeftTop":{"x":157.9,"y":113},"eyeLeftBottom":{"x":158.8,"y":112.9},"eyeLeftInner":{"x":168.9,"y":110.5},"eyebrowRightInner":{"x":200.5,"y":89.1},"eyebrowRightOuter":{"x":240.1,"y":91.1},"eyeRightInner":{"x":209.7,"y":109.1},"eyeRightTop":{"x":218.8,"y":109.6},"eyeRightBottom":{"x":219.5,"y":111},"eyeRightOuter":{"x":229.6,"y":109},"noseRootLeft":{"x":180.7,"y":111},"noseRootRight":{"x":198.4,"y":110.8},"noseLeftAlarTop":{"x":175.9,"y":132},"noseRightAlarTop":{"x":202.8,"y":133},"noseLeftAlarOutTip":{"x":169.2,"y":145.1},"noseRightAlarOutTip":{"x":209,"y":144.5},"upperLipTop":{"x":189.9,"y":165.8},"upperLipBottom":{"x":190.3,"y":173.2},"underLipTop":{"x":189.9,"y":177.1},"underLipBottom":{"x":190.3,"y":188.8}},"attributes":{"headPose":{"pitch":0,"roll":-1,"yaw":-1.9},"gender":"male","age":25}}
sad = {"faceId":"d5cc348d-7535-48c3-b2cd-10ff5e09cb38","faceRectangle":{"top":124,"left":130,"width":130,"height":117},"faceLandmarks":{"pupilLeft":{"x":165.5,"y":157.9},"pupilRight":{"x":220.9,"y":156.1},"noseTip":{"x":193.1,"y":191.8},"mouthLeft":{"x":173.5,"y":220.8},"mouthRight":{"x":217.1,"y":220.0},"eyebrowLeftOuter":{"x":146.7,"y":143.2},"eyebrowLeftInner":{"x":180.0,"y":141.2},"eyeLeftOuter":{"x":157.2,"y":159.3},"eyeLeftTop":{"x":164.4,"y":156.2},"eyeLeftBottom":{"x":164.7,"y":162.5},"eyeLeftInner":{"x":172.4,"y":159.8},"eyebrowRightInner":{"x":202.8,"y":140.2},"eyebrowRightOuter":{"x":237.4,"y":140.6},"eyeRightInner":{"x":213.0,"y":158.6},"eyeRightTop":{"x":220.0,"y":154.6},"eyeRightBottom":{"x":220.7,"y":161.1},"eyeRightOuter":{"x":228.5,"y":157.4},"noseRootLeft":{"x":185.5,"y":161.3},"noseRootRight":{"x":199.9,"y":161.0},"noseLeftAlarTop":{"x":181.8,"y":181.0},"noseRightAlarTop":{"x":205.5,"y":181.0},"noseLeftAlarOutTip":{"x":174.6,"y":194.0},"noseRightAlarOutTip":{"x":213.0,"y":193.0},"upperLipTop":{"x":196.0,"y":212.0},"upperLipBottom":{"x":196.5,"y":219.2},"underLipTop":{"x":196.7,"y":221.3},"underLipBottom":{"x":197.2,"y":229.6}},"attributes":{"headPose":{"pitch":0.0,"roll":-2.5,"yaw":-4.5},"gender":"male","age":25}}
smile = {"faceId":"7a660c4e-0de9-4949-877f-aeeeea7f3796","faceRectangle":{"top":97,"left":141,"width":123,"height":123},"faceLandmarks":{"pupilLeft":{"x":175.3,"y":130.8},"pupilRight":{"x":227.7,"y":128.2},"noseTip":{"x":200.1,"y":164.0},"mouthLeft":{"x":177.6,"y":186.6},"mouthRight":{"x":229.1,"y":184.5},"eyebrowLeftOuter":{"x":155.0,"y":115.8},"eyebrowLeftInner":{"x":188.3,"y":114.2},"eyeLeftOuter":{"x":167.8,"y":131.9},"eyeLeftTop":{"x":173.7,"y":128.7},"eyeLeftBottom":{"x":174.2,"y":134.7},"eyeLeftInner":{"x":182.0,"y":132.5},"eyebrowRightInner":{"x":210.0,"y":113.3},"eyebrowRightOuter":{"x":244.3,"y":113.2},"eyeRightInner":{"x":221.1,"y":130.6},"eyeRightTop":{"x":228.0,"y":125.9},"eyeRightBottom":{"x":228.3,"y":132.1},"eyeRightOuter":{"x":235.5,"y":128.9},"noseRootLeft":{"x":194.9,"y":133.6},"noseRootRight":{"x":207.2,"y":133.2},"noseLeftAlarTop":{"x":189.7,"y":152.3},"noseRightAlarTop":{"x":212.9,"y":152.1},"noseLeftAlarOutTip":{"x":183.7,"y":164.9},"noseRightAlarOutTip":{"x":221.3,"y":163.4},"upperLipTop":{"x":202.4,"y":181.7},"upperLipBottom":{"x":202.6,"y":186.1},"underLipTop":{"x":202.4,"y":193.5},"underLipBottom":{"x":202.3,"y":201.0}},"attributes":{"headPose":{"pitch":0.0,"roll":-2.0,"yaw":-6.3},"gender":"male","age":24}}
laugh = {"faceId":"80ba9ca0-5f44-4a60-ba0b-57b60dcf283f","faceRectangle":{"top":101,"left":137,"width":130,"height":130},"faceLandmarks":{"pupilLeft":{"x":172.0,"y":136.0},"pupilRight":{"x":229.4,"y":134.8},"noseTip":{"x":202.1,"y":174.2},"mouthLeft":{"x":174.1,"y":194.7},"mouthRight":{"x":228.3,"y":193.3},"eyebrowLeftOuter":{"x":151.5,"y":120.8},"eyebrowLeftInner":{"x":187.6,"y":117.6},"eyeLeftOuter":{"x":163.6,"y":135.5},"eyeLeftTop":{"x":172.1,"y":133.5},"eyeLeftBottom":{"x":171.5,"y":138.5},"eyeLeftInner":{"x":180.7,"y":137.6},"eyebrowRightInner":{"x":210.1,"y":116.6},"eyebrowRightOuter":{"x":246.6,"y":118.9},"eyeRightInner":{"x":221.7,"y":136.7},"eyeRightTop":{"x":229.3,"y":131.8},"eyeRightBottom":{"x":229.3,"y":137.9},"eyeRightOuter":{"x":237.7,"y":134.7},"noseRootLeft":{"x":193.0,"y":140.6},"noseRootRight":{"x":209.9,"y":139.7},"noseLeftAlarTop":{"x":187.2,"y":160.6},"noseRightAlarTop":{"x":215.5,"y":160.3},"noseLeftAlarOutTip":{"x":180.1,"y":171.8},"noseRightAlarOutTip":{"x":222.6,"y":170.8},"upperLipTop":{"x":202.8,"y":190.6},"upperLipBottom":{"x":202.6,"y":196.8},"underLipTop":{"x":201.1,"y":207.2},"underLipBottom":{"x":201.3,"y":217.1}},"attributes":{"headPose":{"pitch":0.0,"roll":-1.2,"yaw":-4.1},"gender":"male","age":29}}
glare = {"faceId":"02cd24c0-9a06-458a-9058-31220910e0a6","faceRectangle":{"top":105,"left":154,"width":113,"height":113},"faceLandmarks":{"pupilLeft":{"x":188.2,"y":135.3},"pupilRight":{"x":234.5,"y":134.7},"noseTip":{"x":209.0,"y":159.4},"mouthLeft":{"x":187.8,"y":190.5},"mouthRight":{"x":227.6,"y":189.9},"eyebrowLeftOuter":{"x":164.8,"y":126.3},"eyebrowLeftInner":{"x":196.0,"y":119.9},"eyeLeftOuter":{"x":175.2,"y":135.3},"eyeLeftTop":{"x":182.7,"y":133.1},"eyeLeftBottom":{"x":182.8,"y":137.1},"eyeLeftInner":{"x":190.1,"y":135.1},"eyebrowRightInner":{"x":215.0,"y":119.8},"eyebrowRightOuter":{"x":241.7,"y":122.7},"eyeRightInner":{"x":222.5,"y":135.9},"eyeRightTop":{"x":229.7,"y":132.8},"eyeRightBottom":{"x":229.9,"y":137.4},"eyeRightOuter":{"x":237.1,"y":135.1},"noseRootLeft":{"x":199.8,"y":136.2},"noseRootRight":{"x":214.2,"y":136.7},"noseLeftAlarTop":{"x":195.2,"y":152.1},"noseRightAlarTop":{"x":218.7,"y":151.4},"noseLeftAlarOutTip":{"x":190.7,"y":163.4},"noseRightAlarOutTip":{"x":223.5,"y":162.4},"upperLipTop":{"x":209.4,"y":179.4},"upperLipBottom":{"x":209.7,"y":186.5},"underLipTop":{"x":209.1,"y":190.5},"underLipBottom":{"x":208.4,"y":199.6}},"attributes":{"headPose":{"pitch":0.0,"roll":-1.9,"yaw":5.2},"gender":"male","age":27}}
eyeCenter = {"faceId":"760a7ecd-5d5a-4678-94bd-6e01fdf7f8c7","faceRectangle":{"top":85,"left":152,"width":139,"height":139},"faceLandmarks":{"pupilLeft":{"x":192.1,"y":121.7},"pupilRight":{"x":245.3,"y":120.5},"noseTip":{"x":221.2,"y":152.4},"mouthLeft":{"x":197.1,"y":190.6},"mouthRight":{"x":247.2,"y":190.2},"eyebrowLeftOuter":{"x":168.1,"y":100.6},"eyebrowLeftInner":{"x":206.9,"y":97.4},"eyeLeftOuter":{"x":183.3,"y":122.3},"eyeLeftTop":{"x":191.2,"y":120.3},"eyeLeftBottom":{"x":191.0,"y":125.2},"eyeLeftInner":{"x":198.8,"y":122.3},"eyebrowRightInner":{"x":228.9,"y":94.8},"eyebrowRightOuter":{"x":267.3,"y":97.7},"eyeRightInner":{"x":238.5,"y":122.1},"eyeRightTop":{"x":247.6,"y":118.4},"eyeRightBottom":{"x":248.0,"y":124.2},"eyeRightOuter":{"x":256.5,"y":120.8},"noseRootLeft":{"x":212.7,"y":122.0},"noseRootRight":{"x":228.0,"y":122.2},"noseLeftAlarTop":{"x":206.0,"y":143.1},"noseRightAlarTop":{"x":234.0,"y":143.7},"noseLeftAlarOutTip":{"x":199.7,"y":158.7},"noseRightAlarOutTip":{"x":239.4,"y":158.5},"upperLipTop":{"x":221.5,"y":176.7},"upperLipBottom":{"x":222.1,"y":186.4},"underLipTop":{"x":222.4,"y":189.7},"underLipBottom":{"x":222.3,"y":201.5}},"attributes":{"headPose":{"pitch":0.0,"roll":-2.0,"yaw":-3.3},"gender":"male","age":24}}
sample = [
  {
    "faceId": "17e0bd16-e969-4ed1-95e4-08f40bf88c90",
    "faceRectangle": {
      "width": 59,
      "height": 59,
      "left": 276,
      "top": 43
    },
    "faceLandmarks": {
      "pupilLeft": {
        "x": "294.9",
        "y": "57.3"
      },
      "pupilRight": {
        "x": "318.9",
        "y": "60.2"
      },
      "noseTip": {
        "x": "310.4",
        "y": "74.3"
      },
      "mouthLeft": {
        "x": "290.9",
        "y": "86.0"
      },
      "mouthRight": {
        "x": "312.4",
        "y": "87.6"
      },
      "eyebrowLeftOuter": {
        "x": "283.5",
        "y": "49.2"
      },
      "eyebrowLeftInner": {
        "x": "304.7",
        "y": "51.9"
      },
      "eyeLeftOuter": {
        "x": "289.1",
        "y": "57.1"
      },
      "eyeLeftTop": {
        "x": "294.5",
        "y": "54.4"
      },
      "eyeLeftBottom": {
        "x": "293.1",
        "y": "61.3"
      },
      "eyeLeftInner": {
        "x": "298.3",
        "y": "59.5"
      },
      "eyebrowRightInner": {
        "x": "314.6",
        "y": "54.7"
      },
      "eyebrowRightOuter": {
        "x": "326.8",
        "y": "54.2"
      },
      "eyeRightInner": {
        "x": "313.6",
        "y": "61.3"
      },
      "eyeRightTop": {
        "x": "318.6",
        "y": "57.7"
      },
      "eyeRightBottom": {
        "x": "318.8",
        "y": "64.0"
      },
      "eyeRightOuter": {
        "x": "323.0",
        "y": "60.9"
      },
      "noseRootLeft": {
        "x": "304.3",
        "y": "60.6"
      },
      "noseRootRight": {
        "x": "312.4",
        "y": "61.4"
      },
      "noseLeftAlarTop": {
        "x": "302.8",
        "y": "70.0"
      },
      "noseRightAlarTop": {
        "x": "312.6",
        "y": "70.5"
      },
      "noseLeftAlarOutTip": {
        "x": "299.0",
        "y": "75.5"
      },
      "noseRightAlarOutTip": {
        "x": "314.3",
        "y": "77.0"
      },
      "upperLipTop": {
        "x": "307.2",
        "y": "83.8"
      },
      "upperLipBottom": {
        "x": "306.5",
        "y": "86.5"
      },
      "underLipTop": {
        "x": "305.2",
        "y": "88.2"
      },
      "underLipBottom": {
        "x": "304.1",
        "y": "93.0"
      }
    },
    "attributes": {
      "age": 26,
      "gender": "female",
      "headPose": {
        "roll": "5.0",
        "yaw": "25.0",
        "pitch": "0.0"
      }
    }
  }
]
def normalize(facialData):
	normalizedLandmark = {}
	roll = -float(facialData["attributes"]["headPose"]["roll"]) / 180 * pi
	yaw = float(facialData["attributes"]["headPose"]["yaw"]) / 180 * pi
	pitch = float(facialData["attributes"]["headPose"]["pitch"]) / 180 * pi
	height = float(facialData["faceRectangle"]["height"])
	width = float(facialData["faceRectangle"]["width"])
	left = float(facialData["faceRectangle"]["left"])
	top = float(facialData["faceRectangle"]["top"])
	for key, value in facialData["faceLandmarks"].iteritems():
		normalizedLandmark[key] = {}
		tempx = (float(value["x"]) - left - width / 2) / cos(yaw) / width
		tempy = (float(value["y"]) - top - height / 2) / cos(pitch) / height
		normalizedLandmark[key]["x"] = cos(roll)*tempx - sin(roll)*tempy
		normalizedLandmark[key]["y"] = sin(roll)*tempx + cos(roll)*tempy
	return normalizedLandmark

def plot(landmark):
	x = []
	y = []
	for key, value in landmark.iteritems():
		x.append(value["x"])
		y.append(value["y"])
	plt.plot(x, y, 'ro')
	# print(findCosABC(landmark["mouthLeft"], landmark["underLipTop"], landmark["mouthRight"]))
	print(labelFace(landmark))
	plt.axis([-0.5,0.5,0.5,-0.5])
	plt.show()

def findCosABC(A, B, C):
	vector1 = {}
	vector2 = {}
	normV1 = {}
	normV2 = {}
	vector1["x"] = float(A["x"]) - float(B["x"])
	vector1["y"] = float(A["y"]) - float(B["y"])
	vector2["x"] = float(C["x"]) - float(B["x"])
	vector2["y"] = float(C["y"]) - float(B["y"])
	lenV1 = sqrt(vector1["x"] * vector1["x"] + vector1["y"] * vector1["y"])
	lenV2 = sqrt(vector2["x"] * vector2["x"] + vector2["y"] * vector2["y"])
	normV1["x"] = vector1["x"]/lenV1
	normV1["y"] = vector1["y"]/lenV1
	normV2["x"] = vector2["x"]/lenV2
	normV2["y"] = vector2["y"]/lenV2
	print(normV1, normV2)
	return normV1["x"]*normV2["x"] + normV1["y"]*normV2["y"]

def labelFace(normalizedLandmark):
	labels = Set([])
	glareTH = 0.03
	closeEyeTH = 0.02
	smileTH = -0.9
	laughTH = -0.75
	openMouthTH = 0.07
	if normalizedLandmark["underLipTop"]["y"] - normalizedLandmark["upperLipBottom"]["y"] >= openMouthTH :
		labels.add('mouthOpen')
	if normalizedLandmark["eyeLeftBottom"]["y"] - normalizedLandmark["eyeLeftTop"]["y"] <= closeEyeTH :
		labels.add('leftEyeClose')
	if normalizedLandmark["eyeRightBottom"]["y"] - normalizedLandmark["eyeRightTop"]["y"] <= closeEyeTH :
		labels.add('rightEyeClose')
	mouthAngle = findCosABC(normalizedLandmark["mouthLeft"], normalizedLandmark["underLipTop"], normalizedLandmark["mouthRight"])
	if mouthAngle >= laughTH:
		labels.add('laugh')
	elif mouthAngle >= smileTH:
		labels.add('smile')
	if normalizedLandmark['pupilLeft']['x'] - normalizedLandmark['eyeLeftOuter']['x'] <= glareTH :
		labels.add('leftEyeLeft')
	elif normalizedLandmark['eyeLeftInner']['x'] - normalizedLandmark['pupilLeft']['x'] <= glareTH :
		labels.add('leftEyeRight')
	if normalizedLandmark['pupilRight']['x'] - normalizedLandmark['eyeLeftInner']['x'] <= glareTH :
		labels.add('rightEyeLeft')
	elif normalizedLandmark['eyeRightOuter']['x'] - normalizedLandmark['pupilRight']['x'] <= glareTH :
		labels.add('rightEyeRight')
	return labels

def main():
	plot(normalize(glare));

if __name__ == "__main__":
	main()
