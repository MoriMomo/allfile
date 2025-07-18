// src/firebase/firebaseinit.js

import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD_qjNwHc-qU6nGI80VEtMp4B_vnA0cR34",
    authDomain: "weathervue-a0dab.firebaseapp.com",
    projectId: "weathervue-a0dab",
    storageBucket: "weathervue-a0dab.appspot.com",
    messagingSenderId: "885227530542",
    appId: "1:885227530542:web:57f232c9584cd331b0b2bf"
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);

// Initialize Firebase services
const auth = getAuth(firebaseApp);
const db = getFirestore(firebaseApp);

export { firebaseApp, auth, db };