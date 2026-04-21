npm install firebase

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCdlgAxAt2PhAF26jbazr1yoDUD_V-wkmU",
  authDomain: "infinite-socrates.firebaseapp.com",
  projectId: "infinite-socrates",
  storageBucket: "infinite-socrates.firebasestorage.app",
  messagingSenderId: "677068126117",
  appId: "1:677068126117:web:20a6774a4bb047deac5a4c",
  measurementId: "G-VN1SYSZN60"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
