const CLASSES = ({ 0: '๐  ใใใฃใฆใใพใ', 1: '๐ฌ ใใใ', 2: '๐จ ใใใ', 3: '๐ ใใใใ', 4: '๐ข ใใชใใ', 5: '๐ฎ ใใฉใใ', 6: '๐ ็ด ' })
const COLORS = ({ 0: 'red', 1: 'green', 2: 'purple', 3: 'yellow', 4: 'blue', 5: 'skyblue', 6: 'white' })

// MediaDevices.getUserMedia() default size 640pxx480px
let originalVideoWidth = 640;

let model;
let emotion = [6, CLASSES[6], 1.000000];
let emotionColor;

//-----------------------
// start button event
//-----------------------

$("#start-button").click(function () {
  loadModel();
  startWebcam();
});

//-----------------------
// load model
//-----------------------

async function loadModel() {
  console.log("model loading..");

  $("#console").html(`<li>ใขใใซใ่ชญใฟ่พผใใงใใพใใใใ</li>`);
  model = await tf.loadModel(`../static/emotion_XCEPTION/model.json`);

  console.log("model loaded.");
  $("#console").html(`<li>ๆๆๅๆใฎๆบๅใใงใใพใใใ</li>`);
};

//-----------------------
// start webcam 
//-----------------------
var video = $('#main-stream-video').get(0);
var tracker = new tracking.LandmarksTracker();

function startWebcam() {
  tracker.setInitialScale(4);
  tracker.setStepSize(2);
  tracker.setEdgesDensity(0.1);
  tracking.track(video, tracker, { camera: true });
};

//-----------------------
// predict button event
//-----------------------

$("#predict-button").click(function () {
  alignment();
});

//-----------------------
// face alignment
//-----------------------

async function alignment() {

  tracker.on('track', function (event) {
    var canvas = $('#main-stream-canvas').get(0);
    var context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);
    if (!event.data) return;
    event.data.faces.forEach(function (rect) {
      predict(rect);
      console.log(emotion[0], emotion[1], emotion[2]);

      emotionColor = COLORS[emotion[0]]

      context.strokeStyle = emotionColor;
      context.lineWidth = 2;
      context.strokeRect(rect.x, rect.y, rect.width, rect.height);
      context.font = '11px Helvetica';
      context.fillStyle = emotionColor;
      context.fillText(emotion[1], rect.x + rect.width + 5, rect.y + 11);
      context.fillText(emotion[2].toFixed(6), rect.x + rect.width + 5, rect.y + 22);

    });

    event.data.landmarks.forEach(function (landmarks) {
      for (var l in landmarks) {
        context.beginPath();
        context.fillStyle = emotionColor;
        context.arc(landmarks[l][0], landmarks[l][1], 2, 0, 2 * Math.PI);
        context.fill();
      }
    });
  });
};

//-----------------------
// TensorFlow.js method
// predict tensor
//-----------------------

async function predict(rect) {

  let tensor = captureWebcam(rect);

  let prediction = await model.predict(tensor).data();
  let results = Array.from(prediction)
    .map(function (p, i) {
      return {
        probability: p,
        className: CLASSES[i],
        classNumber: i
      };
    }).sort(function (a, b) {
      return b.probability - a.probability;
    }).slice(0, 2);

  $("#console").empty();
  results.forEach(function (p) {
    $("#console").append(`<li>${p.className} : ${p.probability.toFixed(3)}</li>`);

    return emotion = [results[0].classNumber, results[0].className, results[0].probability]

  });
};

//------------------------------
// capture streaming video 
// to a canvas object
//------------------------------

function captureWebcam(rect) {
  var faceCanvas = $('#faceCanvas').get(0);
  var faceContext = faceCanvas.getContext('2d');

  //adjust original video size
  var adjust = originalVideoWidth / video.width
  faceContext.drawImage(video, rect.x * adjust, rect.y * adjust, rect.width * adjust, rect.height * adjust, 0, 0, 100, 100);

  tensor_image = preprocessImage(faceCanvas);

  return tensor_image;
}

//-----------------------
// TensorFlow.js method
// image to tensor
//-----------------------

function preprocessImage(image) {
  const channels = 1;
  let tensor = tf.fromPixels(image, channels).resizeNearestNeighbor([64, 64]).toFloat();
  let offset = tf.scalar(255);
  return tensor.div(offset).expandDims();
};


//-----------------------
// clear button event
//-----------------------

$("#clear-button").click(async function clasify() {
  location.reload();
});

