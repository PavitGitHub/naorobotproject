const multer = require('multer');
const path = require('path');
const fs = require('fs');

// Create directories if they don't exist
const videoDir = path.join(__dirname, 'uploads/videos');
const imageDir = path.join(__dirname, 'uploads/images');
const audioDir = path.join(__dirname, 'uploads/audio');

if (!fs.existsSync(videoDir)) fs.mkdirSync(videoDir, { recursive: true });
if (!fs.existsSync(imageDir)) fs.mkdirSync(imageDir, { recursive: true });
if (!fs.existsSync(audioDir)) fs.mkdirSync(audioDir, { recursive: true });

// Set up storage options
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    const ext = path.extname(file.originalname).toLowerCase();
    if (ext === '.mp4') {
      cb(null, videoDir);
    } else if (ext === '.mp3') {
      cb(null, audioDir);
    } else if (ext === '.png' || ext === '.jpg' || ext === '.jpeg') {
      cb(null, imageDir);
    } else {
      cb(new Error('Invalid file type'));
    }
  },
  filename: function (req, file, cb) {
    cb(null, `${file.originalname}`);
  },
});

// Set up file filter to accept only the desired file types
const fileFilter = function (req, file, cb) {
  const ext = path.extname(file.originalname).toLowerCase();
  if (ext === '.mp4' || ext === '.mp3' || ext === '.png' || ext === '.jpg' || ext === '.jpeg') {
    cb(null, true);
  } else {
    cb(new Error('Only .mp4, .mp3, .png, .jpg, and .jpeg files are allowed'), false);
  }
};

const upload = multer({
  storage: storage,
  fileFilter: fileFilter,
});

module.exports = {upload}